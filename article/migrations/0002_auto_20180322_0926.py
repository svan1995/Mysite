# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-22 01:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AritcleColumn',
            new_name='ArticleColumn',
        ),
    ]
