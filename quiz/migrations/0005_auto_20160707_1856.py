# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20160707_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='email_10',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='email_6',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='email_7',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='email_8',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='email_9',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
