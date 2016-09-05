# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160905_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uloziste',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=100, verbose_name='Diagn\xf3za'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='doctor',
            field=models.CharField(blank=True, max_length=100, verbose_name='L\xe9ka\u0159'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='drawingDoctor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Zakreslen\xed stav/l\xe9ka\u0159'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='drawingTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Datum zakreslen\xed'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='ok1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Schv\xe1len\xed l\xe9ka\u0159 1'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='ok2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Schv\xe1len\xed l\xe9ka\u0159 2'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='planningDoctor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Pl\xe1nov\xe1n\xed stav/pl\xe1nova\u010d'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='planningTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Datum pl\xe1nov\xe1n\xed'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='pzn',
            field=models.TextField(blank=True, default='', verbose_name='Pozn\xe1mka'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='radAs',
            field=models.CharField(blank=True, max_length=100, verbose_name='Rad. As.'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='resimulTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Datum a \u010das resimulace'),
        ),
    ]
