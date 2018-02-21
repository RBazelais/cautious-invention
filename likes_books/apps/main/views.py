from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
# from django.contrib import messages
from . import models
# from models import User

def index(request):
    return render(request, 'index.html')