# -*- coding: utf-8 -*-
from colour import Color
import pandas as pd

from django.db import models
from django.apps import apps
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

from ..utils import COLUMNS_TO_AVOID


class Column(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    data_file = models.ForeignKey('data_file.DataFile', on_delete=models.CASCADE)
    min_value = models.DecimalField(max_digits=16, decimal_places=1)
    max_value = models.DecimalField(max_digits=16, decimal_places=1)
    min_color = models.CharField(max_length=7, null=True, blank=True)
    max_color = models.CharField(max_length=7, null=True, blank=True)
    intervals = models.IntegerField(blank=True, null=True)

    def get_color_ranges(self):
        min_col = Color(self.min_color)
        max_col = Color(self.max_color)
        return (c.hex for c in list(min_col.range_to(max_col, self.intervals)))

    def get_value_ranges(self):
        ranges = []
        start_val = self.max_value/self.intervals
        for num in range(self.intervals-1):
            if num == 0:
                ranges.append((0, start_val))
            elif num == 1:
                ranges.append((start_val, start_val*(self.intervals+1)))
            else:
                ranges.append((start_val*num, start_val*(self.intervals+1)))
        return tuple(ranges)

    def ___rep__(self):
        return self.data_file.name + ": " + self.name


class DataFile(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    uploaded_file = models.FileField(upload_to='static/data/', blank=True, null=True)
    time_created = models.DateTimeField(auto_now=True, null=True, blank=False)

    class Meta:
        get_latest_by = 'time_created'

    def as_dataframe(self):
        return pd.read_csv(self.uploaded_file.path)

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

    def __repr__(self):
        return 'DataFile: ' + self.name


@receiver(post_save, sender=DataFile)
def create_columns(sender, instance, **kwargs):
    instance.create_all_columns()
