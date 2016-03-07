# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 19:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0003_auto_20160305_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 6, 19, 42, 41, 139684, tzinfo=utc), verbose_name='Updated at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='function',
            name='uuid',
            field=models.UUIDField(db_index=True, editable=False, null=True),
            preserve_default=False,
        ),
    ]
