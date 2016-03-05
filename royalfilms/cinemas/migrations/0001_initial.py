# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0004_movie_synopsis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('lat', models.FloatField(default=0.0, verbose_name='Latitude')),
                ('lng', models.FloatField(default=0.0, verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('published_at', models.DateField(auto_now_add=True, verbose_name='Published at')),
                ('published_until', models.DateField(verbose_name='Published until')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.Cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='functions',
            field=models.ManyToManyField(through='cinemas.Function', to='movies.Movie'),
        ),
    ]
