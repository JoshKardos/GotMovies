# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_remove_movie_western'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='fn',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='imdbRating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='movie',
            name='nrOfNewsArticles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='nrOfNominations',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='nrOfPhotos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='nrOfUserReviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='nrOfWins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratingCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='tid',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.CharField(default=0, max_length=75),
        ),
        migrations.AddField(
            model_name='movie',
            name='url',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='wordsInTitle',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]