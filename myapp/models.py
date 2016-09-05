# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta


# Create your models here.

class Uloziste(models.Model):
    name = models.CharField('Jméno', max_length=100)
    birthNumber = models.CharField('Rodné číslo', max_length=10)
    diagnosis = models.CharField('Diagnóza', max_length=100, blank=True)
    radAs = models.CharField('Rad. As.', max_length=100, blank=True)
    doctor = models.CharField('Lékař', max_length=100, blank=True)
    resimulTime = models.DateTimeField('Datum a čas resimulace', default=timezone.now, blank=True)
    drawingTime = models.DateTimeField('Datum zakreslení', default=timezone.now, blank=True)
    drawingDoctor = models.CharField('Zakreslení stav/lékař', max_length=100, blank=True)
    planningTime = models.DateTimeField('Datum plánování', default=timezone.now, blank=True)
    planningDoctor = models.CharField('Plánování stav/plánovač', max_length=100, blank=True)
    ok1 = models.CharField('Schválení lékař 1', max_length=100, blank=True)
    ok2 = models.CharField('Schválení lékař 2', max_length=100, blank=True)
    tisk = models.BooleanField(default=True)
    pzn = models.TextField('Poznámka', default='',blank=True)

    class Meta:
        verbose_name = 'Pacient'
        verbose_name_plural = 'Pacienti'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
