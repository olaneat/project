# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0007_auto_20171110_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucketlist',
            name='items',
        ),
        migrations.AddField(
            model_name='bucketlistitem',
            name='bucketlist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rest_api.Bucketlist'),
            preserve_default=False,
        ),
    ]
