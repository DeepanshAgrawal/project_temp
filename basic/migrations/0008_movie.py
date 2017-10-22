# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0007_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_director', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('romance', 'romance'), ('drama', 'drama'), ('comedy', 'comedy'), ('fiction', 'fiction')], max_length=100)),
            ],
        ),
    ]