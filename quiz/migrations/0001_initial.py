# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, unique=True)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_1', models.IntegerField()),
                ('value_2', models.IntegerField()),
                ('value_3', models.IntegerField()),
                ('value_4', models.IntegerField()),
                ('value_5', models.IntegerField()),
                ('interest_1', models.BooleanField(default=False)),
                ('interest_2', models.BooleanField(default=False)),
                ('interest_3', models.BooleanField(default=False)),
                ('interest_4', models.BooleanField(default=False)),
                ('interest_5', models.BooleanField(default=False)),
                ('adjective_1', models.BooleanField(default=False)),
                ('adjective_2', models.BooleanField(default=False)),
                ('adjective_3', models.BooleanField(default=False)),
                ('adjective_4', models.BooleanField(default=False)),
                ('adjective_5', models.BooleanField(default=False)),
                ('metric_1', models.CharField(max_length=50)),
                ('metric_2', models.CharField(max_length=50)),
                ('metric_3', models.CharField(max_length=50)),
                ('metric_4', models.CharField(max_length=50)),
                ('metric_5', models.CharField(max_length=50)),
                ('metric_6', models.CharField(max_length=50)),
                ('metric_7', models.CharField(max_length=50)),
                ('metric_8', models.CharField(max_length=50)),
                ('metric_9', models.CharField(max_length=50)),
                ('metric_10', models.CharField(max_length=50)),
                ('major_1', models.CharField(max_length=50)),
                ('major_2', models.CharField(max_length=50)),
                ('major_3', models.CharField(max_length=50)),
                ('major_4', models.CharField(max_length=50)),
                ('major_5', models.CharField(max_length=50)),
                ('email_1', models.EmailField(max_length=254)),
                ('email_2', models.EmailField(max_length=254)),
                ('email_3', models.EmailField(max_length=254)),
                ('email_4', models.EmailField(max_length=254)),
                ('email_5', models.EmailField(max_length=254)),
                ('email_6', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.MyUser')),
            ],
        ),
    ]
