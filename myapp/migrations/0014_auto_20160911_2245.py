# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20160906_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uloziste',
            name='doctor',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2, verbose_name='Doktor'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='pznDisplay',
            field=models.BooleanField(default=False, verbose_name='Pozn\xe1mka'),
        ),
    ]
