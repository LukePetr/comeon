# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20160906_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uloziste',
            name='pznDisplay',
            field=models.BooleanField(default=False, verbose_name='Pzn.'),
        ),
    ]