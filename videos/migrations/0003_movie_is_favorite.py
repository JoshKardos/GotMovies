# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_remove_trailer_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]