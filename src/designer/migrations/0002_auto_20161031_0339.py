# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-31 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='data',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='data_cap',
            field=models.BigIntegerField(default=100000000),
        ),
    ]
