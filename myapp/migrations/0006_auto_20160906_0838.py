# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20160905_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='uloziste',
            name='pomucky',
            field=models.CharField(blank=True, max_length=100, verbose_name='Pom\u016fcky'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='doctor',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='drawingDoctor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Zakreslen\xed stav'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='drawingTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Zakreslen\xed'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='ok1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Schv\xe1len\xed 1'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='ok2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Schv\xe1len\xed 2'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='planningDoctor',
            field=models.CharField(blank=True, max_length=100, verbose_name='Pl\xe1nov\xe1n\xed stav'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='planningTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Pl\xe1nov\xe1n\xed'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='pzn',
            field=models.TextField(blank=True, default='NULL', verbose_name='Pozn\xe1mka'),
        ),
        migrations.AlterField(
            model_name='uloziste',
            name='resimulTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Resimulace'),
        ),
    ]