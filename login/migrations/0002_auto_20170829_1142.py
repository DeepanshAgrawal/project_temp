# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='usr',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]