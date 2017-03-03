# -*- coding: utf-8 -*-
import geopandas as gpd

from django.db import models

from ..utils import (DC_GEOJSON_BLOCKS, DC_GEOJSON_TRACTS,
                     GEO_LEVEL_CHOICES, MATCH_KEY_CHOICES)

class MapMaker(models.Model):
    geo_level = models.CharField(choices=GEO_LEVEL_CHOICES, max_length=24)
    match_key = models.CharField(choices=MATCH_KEY_CHOICES, max_length=24)
    data_file = models.ForeignKey('data_file.DataFile', on_delete=models.CASCADE)

    @property
    def geojson_file_name(self):
        if self.geo_level == 'tracts':
            return DC_GEOJSON_TRACTS
        elif self.geo_level == 'blocks':
            return DC_GEOJSON_BLOCKS
        else:
            raise Exception('not valid or supported geo level')

    def as_dataframe(self):
        return gpd.read_file(self.geojson_file_name)

    def data_file_prepped(self):
        columns = self.match_key + self.data_file.columns_to_create
        return self.data_file.as_dataframe().ix[:, columns]

    def merge_data(self):
        return self.as_dataframe().merge(self.data_file_prepped, on=self.match_key)

    def final_json(self):
        return self.merge_data().to_json()
