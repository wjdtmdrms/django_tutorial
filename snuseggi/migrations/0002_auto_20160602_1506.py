# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snuseggi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='restuarant',
            new_name='restaurant',
        ),
    ]
