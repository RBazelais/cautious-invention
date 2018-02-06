from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/result')

def process(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print request.POST
        print request.POST['name']
        print request.POST['location']
        print request.POST['language']
        print request.POST['comment']

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

    # context = {
    #     'count': count,
    #     # 'name': name,
    #     # 'location': location,
    #     # 'langauge': language,
    #     # 'comment': comment
    # }
    return redirect('/result')

def result(request):
    count = 0
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    return render(request, 'display.html', { 'count' : count })

def go_back(request):
    return redirect('/')