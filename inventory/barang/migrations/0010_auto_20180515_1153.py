# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0009_auto_20180515_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]