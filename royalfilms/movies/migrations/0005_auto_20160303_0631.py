# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 06:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_synopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 3, 6, 31, 11, 175748, tzinfo=utc), verbose_name='Updated at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]