# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20160219_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(max_length=1000, null=True, verbose_name='Synopsis'),
        ),
    ]
