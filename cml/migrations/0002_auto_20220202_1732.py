# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2022-02-02 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cml', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exchange',
            options={'verbose_name': 'Exchange log entry', 'verbose_name_plural': 'Exchange logs'},
        ),
    ]
