# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uloziste',
            options={'verbose_name': 'Pacient', 'verbose_name_plural': 'Pacienti'},
        ),
        migrations.AddField(
            model_name='uloziste',
            name='pzn',
            field=models.CharField(default='NULL', max_length=100, verbose_name='Pozn\xe1mka'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='planningDoctor',
            field=models.CharField(max_length=100, verbose_name='Pl\xe1nov\xe1n\xed stav/pl\xe1nova\u010d'),
        ),
    ]