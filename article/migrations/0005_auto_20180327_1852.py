# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-27 10:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180327_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepost',
            old_name='user_like',
            new_name='users_like',
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 27, 10, 52, 39, 348102, tzinfo=utc)),
        ),
    ]
