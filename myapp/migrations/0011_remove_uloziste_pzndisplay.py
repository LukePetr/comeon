# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20160906_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uloziste',
            name='pznDisplay',
        ),
    ]
