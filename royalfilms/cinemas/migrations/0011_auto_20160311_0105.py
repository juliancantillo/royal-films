# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0010_cinema_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='auditorium',
        ),
        migrations.RemoveField(
            model_name='showtimes',
            name='show',
        ),
        migrations.AddField(
            model_name='show',
            name='showtime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinemas.Showtimes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='showtimes',
            name='auditorium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinemas.Auditorium'),
        ),
        migrations.AlterField(
            model_name='function',
            name='showtimes',
            field=models.ManyToManyField(related_name='functions_auditoriums', through='cinemas.Showtimes', to='cinemas.Auditorium'),
        ),
    ]