# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snuseggi', '0004_auto_20160602_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='all',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
