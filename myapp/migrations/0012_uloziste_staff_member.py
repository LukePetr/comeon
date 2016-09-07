# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 09:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0011_remove_uloziste_pzndisplay'),
    ]

    operations = [
        migrations.AddField(
            model_name='uloziste',
            name='staff_member',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
