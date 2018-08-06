# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 03:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_auto_20180515_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='kodebarang',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='namabarang',
            field=models.CharField(max_length=30),
        ),
    ]
