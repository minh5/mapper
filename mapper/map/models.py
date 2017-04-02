# -*- coding: utf-8 -*-
import geopandas as gpd

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

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
        data = gpd.read_file(self.geojson_file_name)
        data['GEOID'] = data['GEOID'].astype(float)
        return data

    def df_dataframe(self):
        columns = [self.match_key] + self.data_file.columns_to_create
        df = self.data_file.as_dataframe()
        df[self.match_key] = df[self.match_key].astype(int)
        return self.data_file.as_dataframe().ix[:, columns]

    def merged_data(self):
        return self.as_dataframe().merge(self.df_dataframe(),
                                         left_on='GEOID',
                                         right_on=self.match_key)

    def to_json(self):
        return self.merged_data().to_json()

    def save_json(self):
        with open('mapper/static/geojson/mapData.geojson', 'w') as f:
            f.write(self.to_json())


@receiver(post_save, sender=MapMaker)
def create_columns(sender, instance, **kwargs):
    instance.save_json()
