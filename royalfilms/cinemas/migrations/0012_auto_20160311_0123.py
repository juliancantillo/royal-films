# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0011_auto_20160311_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtimes',
            name='auditorium',
        ),
        migrations.RemoveField(
            model_name='showtimes',
            name='function',
        ),
        migrations.RemoveField(
            model_name='function',
            name='showtimes',
        ),
        migrations.RemoveField(
            model_name='show',
            name='showtime',
        ),
        migrations.DeleteModel(
            name='Showtimes',
        ),
    ]
