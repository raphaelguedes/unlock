# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-28 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlock', '0007_auto_20180727_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='botao',
            name='key_botao',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
