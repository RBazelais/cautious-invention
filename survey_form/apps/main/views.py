from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/')

def process(request):
    count = 0
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    context = {
        'count': count,
        'name': request.POST['name'],
        'location': request.POST['location'],
        'langauge': request.POST['langauge']
    }
    return redirect('/result')

def result(request):
    return render(request, 'display.html', context)
    
def go_back(request):
    return redirect('/')