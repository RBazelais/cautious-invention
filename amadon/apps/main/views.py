from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/checkout')

def process(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        shirt = request.POST.get('shirt', False)
        sweater = request.POST.get('sweater', False)
        mug = request.POST.get('mug', False)
        algo_book = request.POST.get('algo_book', False)

        print request.POST
        # print request.POST['shirt']
        # print request.POST['sweater']
        # print request.POST['mug']
        # print request.POST['algo_book']

        context = {
            'shirt' : shirt,
            'sweater' : sweater,
            'mug' : mug,
            'algo_book' : algo_book
        }

    return redirect('/checkout', context)

def checkout(request):
    productDict ={
        'shirt' : 20,
        'sweater': 30,
        'mug': 5,
        'algo_book': 50
    }
    count = 0
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    total = 0
    total = request.POST.get(['shirt'].val())
    print total

    if 'total' in request.session:
        if 'shirt' in request.session:
            total = shirt.value 
        elif 'sweater' in request.session:
            request.session['total'] += 30
        elif 'mug' in request.session:
            request.session['total'] += 5
        elif 'algo_book' in request.session:
            request.session['total'] += 50
    else:
        request.session['total'] = 0

    return render(request, 'display.html', { 'count' : count, 'total': total })

def go_back(request):
    return redirect('/')