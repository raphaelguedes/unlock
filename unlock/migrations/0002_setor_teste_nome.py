# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setor',
            name='teste_nome',
            field=models.CharField(default=7, max_length=50),
            preserve_default=False,
        ),
    ]