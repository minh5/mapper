# -*- coding: utf-8 -*-
import pandas as pd

from django.db import models
from django.apps import apps

from ..utils import COLUMNS_TO_AVOID

class Column(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    data_file = models.ForeignKey('data_file.DataFile', on_delete=models.CASCADE)
    min_value = models.DecimalField(max_digits=16, decimal_places=1)
    max_value = models.DecimalField(max_digits=16, decimal_places=1)
    min_color = models.CharField(max_length=7, null=True, blank=True)
    max_color = models.CharField(max_length=7, null=True, blank=True)
    intervals = models.IntegerField(blank=True, null=True)

    def ___str__(self):
        return self.name

class DataFile(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    uploaded_file = models.FileField(upload_to='static/data/', blank=True, null=True)

    def as_dataframe(self):
        return pd.read_csv(self.filepath.__str__())

    @property
    def data_columns(self):
        data = self.as_dataframe()
        return data.columns.values.tolist()

    def create_column(self, column_name):
        Column = apps.get_model('data_file.Column')
        data = self.as_dataframe()
        subset = data.ix[:, column_name]
        max_value = float(subset.max())
        min_value = float(subset.min())
        column = Column(name=column_name, data_file=self, min_value=min_value,
                        max_value=max_value)
        column.save()

    @property
    def columns_to_create(self):
        return [c for c in self.as_dataframe().columns.values.tolist() if c not in COLUMNS_TO_AVOID]

    def create_all_columns(self):
        for column in self.columns_to_create:
            self.create_column(column)
