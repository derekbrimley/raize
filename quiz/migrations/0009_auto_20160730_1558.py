# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-30 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alumniscores'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumniscores',
            name='VLP_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userscore',
            name='VLP_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
