# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0006_auto_20160307_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditorium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.Cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Showtimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelManagers(
            name='function',
            managers=[
                ('now_playing', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='show',
            name='function',
        ),
        migrations.AddField(
            model_name='showtimes',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='showtimes_function', to='cinemas.Function'),
        ),
        migrations.AddField(
            model_name='showtimes',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.Show'),
        ),
        migrations.AddField(
            model_name='function',
            name='showtimes',
            field=models.ManyToManyField(related_name='functions_showtimes', through='cinemas.Showtimes', to='cinemas.Show'),
        ),
        migrations.AddField(
            model_name='show',
            name='auditorium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinemas.Auditorium'),
        ),
    ]