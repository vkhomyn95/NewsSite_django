# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from news.models import  News


def home(request):
    news = News.objects.all()
    return render(request, 'main.html', {'news': news})