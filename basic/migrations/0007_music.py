# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_auto_20170906_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('songs_name', models.CharField(max_length=100)),
                ('songs_singer', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('rock', 'rock'), ('pop', 'pop'), ('classical', 'classical'), ('hardcore', 'hardcore')], max_length=100)),
            ],
        ),
    ]