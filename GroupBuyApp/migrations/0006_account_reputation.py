# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupBuyApp', '0005_auto_20171207_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
    ]