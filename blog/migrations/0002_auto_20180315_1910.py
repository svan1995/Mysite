# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-15 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
