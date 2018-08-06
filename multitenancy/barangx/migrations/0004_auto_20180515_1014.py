# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 03:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0003_auto_20180515_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='deskripsi',
            field=models.CharField(max_length=100),
        ),
    ]
