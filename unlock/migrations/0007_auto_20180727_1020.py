# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-27 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unlock', '0006_auto_20180727_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botao',
            name='situacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='unlock.Status'),
        ),
    ]
