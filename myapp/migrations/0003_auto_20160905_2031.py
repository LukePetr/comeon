# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160905_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uloziste',
            name='pzn',
            field=models.CharField(default='', max_length=100, verbose_name='Pozn\xe1mka'),
        ),
    ]
