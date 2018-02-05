from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

# Create your views here.
def index(request):
    # return HttpResponse("It's Alive!!!")
    count = 0
    word = ''

    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    context = {
        'word': get_random_string(length=8),
        'count': count
    }
    return render(request, 'index.html', context)

def reset(request):
    request.session.flush()
    return redirect('/')
