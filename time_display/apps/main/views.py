from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    # return HttpResponse("It's Alive!!!")
   
    context = {
        'time': datetime.datetime.now()
    }
    return render(request, 'index.html', context)