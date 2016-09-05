# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Uloziste(models.Model):
    name = models.CharField('Jméno', max_length=100)
    birthNumber = models.CharField('Rodné číslo', max_length=10)
    diagnosis = models.CharField('Diagnóza', max_length=100)
    radAs = models.CharField('Rad. As.', max_length=100)
    doctor = models.CharField('Lékař', max_length=100)
    resimulTime = models.DateTimeField('Datum a čas resimulace', default=timezone.now)
    drawingTime = models.DateTimeField('Datum zakreslení', default=timezone.now)
    drawingDoctor = models.CharField('Zakreslení stav/lékař', max_length=100)
    planningTime = models.DateTimeField('Datum plánování', default=timezone.now)
    planningDoctor = models.CharField('Plánování stav/plánovač', max_length=100)
    ok1 = models.CharField('Schválení lékař 1', max_length=100)
    ok2 = models.CharField('Schválení lékař 2', max_length=100)
    tisk = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Pacient'
        verbose_name_plural = 'Pacienti'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
