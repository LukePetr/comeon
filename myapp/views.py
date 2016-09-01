# -*- coding: utf-8 -*-
from django.shortcuts import render
from myapp.models import Uloziste

# Create your views here.
def zobrazeni(request):
    objekt = Uloziste.objects.all().order_by('name')
    return render(request, 'myapp/index.html', {'objekt': objekt})
