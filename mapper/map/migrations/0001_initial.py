# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapMaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_level', models.CharField(choices=[('tracts', 'Census Tracts'), ('blocks', 'Census Blocks')], max_length=24)),
                ('match_key', models.CharField(choices=[('geoid', 'GEO ID'), ('tract', 'CENSUS TRACT'), ('blkgrp', 'CENSUS BLOCK GROUP')], max_length=24)),
                ('data_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_file.DataFile')),
            ],
        ),
    ]
