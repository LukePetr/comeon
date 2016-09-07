# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta


# Create your models here.

class Uloziste(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    DOCTOR = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )

    name = models.CharField('Jméno', max_length=100)
    birthNumber = models.CharField('Rodné číslo', max_length=10)
    diagnosis = models.CharField('Diagnóza', max_length=100, blank=True)
    radAs = models.CharField('Rad. As.', max_length=100, blank=True)
    doctor = models.CharField(max_length=2, choices=DOCTOR, default=FRESHMAN,)
    resimulTime = models.DateTimeField('Resimulace', default=timezone.now, blank=True)
    drawingTime = models.DateField('Zakreslení', default=timezone.now, blank=True)
    drawingDoctor = models.CharField('Zakreslení stav', max_length=100, blank=True)
    planningTime = models.DateField('Plánování', default=timezone.now, blank=True)
    planningDoctor = models.CharField('Plánování stav', max_length=100, blank=True)
    ok1 = models.CharField('Schválení 1', max_length=100, blank=True)
    ok2 = models.CharField('Schválení 2', max_length=100, blank=True)
    pomucky = models.CharField('Pomůcky', max_length=100, blank=True)
    tisk = models.BooleanField(default=True)
    pzn = models.TextField('Poznámka', blank=True,)
    pznDisplay = models.BooleanField('Poznámka', default=False)

    class Meta:
        verbose_name = 'Pacient'
        verbose_name_plural = 'Pacienti'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

