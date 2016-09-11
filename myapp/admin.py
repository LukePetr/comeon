# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Uloziste
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
import sys

def make_active(modeladmin, news, queryset):
    queryset.update(is_active=True)
make_active.short_description = u"Aktivovat vybraného uživatele"

class Media:
    css = {'all': ('static/css/admin/.css',)}

class CustomUserAdmin(UserAdmin):
    actions = [make_active]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.site_header = 'Správa pacientů'

def Pzn(obj):
    return obj.pzn!=""
Pzn.boolean = True

class adminUloziste(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('name', 'birthNumber'), ('diagnosis', 'radAs'), 'doctor', 'resimulTime', ('drawingTime', 'drawingDoctor'), ('planningTime', 'planningDoctor'), ('ok1', 'ok2'), ('pomucky', 'tisk'), 'pzn')
        }),
       )

    list_display = ('name', 'birthNumber', 'diagnosis', 'radAs', 'doctor', 'resimulTime', 'drawingTime', 'drawingDoctor', 'planningTime', 'planningDoctor', 'ok1', 'ok2', 'pomucky', 'tisk', Pzn)

    #list_editable = ('doctor', 'resimulTime', 'drawingTime', 'drawingDoctor', 'planningTime', 'planningDoctor', 'ok1', 'ok2', 'pomucky')

    #readonly_fields = ('pznDisplay',)
    #list_display = ('name', 'birthNumber', 'diagnosis', 'radAs', 'doctor', 'resimulTime', 'drawingTime', 'drawingDoctor', 'planningTime', 'planningDoctor', 'ok1', 'ok2', 'pomucky', 'tisk', 'pznDisplay')
    #list_filter = ['name', 'birthNumber', 'diagnosis', 'radAs', 'doctor', 'resimulTime', 'drawingTime', 'drawingDoctor', 'planningTime', 'planningDoctor', 'ok1', 'ok2', 'tisk']
    search_fields = ['name', 'birthNumber', 'diagnosis', 'radAs', 'doctor', 'resimulTime', 'drawingTime', 'drawingDoctor', 'planningTime', 'planningDoctor', 'ok1', 'ok2', 'pomucky', 'tisk', 'pzn']
    date_hierarchy = 'resimulTime'
    list_per_page = 50



admin.site.register(Uloziste, adminUloziste)

