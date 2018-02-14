from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 

# Create your views here.
def index(request):
    if not 'total' in request.session:
        request.session['total'] = 0
    if not 'price' in request.session:
        request.session['price'] = 0
    request.session['buy'] = []
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
    
    buy = request.POST['buy']
    total = request.session['total']
    count = request.session['count']
    price = request.session['price']

    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    print "init total: ", total

    def purchase():
        pass

    # if shirt clicked do a thing
    if buy == 'shirt':
        # does it work?
        print "Buying a shirt..."
        shirt = 19.99
        request.session['price'] = shirt
        #send total to session, then increment session total
        request.session['total'] = total + shirt
        print "New total: ", total
        print "New count: ", count

    elif buy == 'sweater':
        # does it work?
        print "Buying a sweater..."
        sweater = 29.99
        request.session['price'] = sweater
        #send total to session, then increment session total
        request.session['total'] = total + sweater 

        print "New total: ", total
        print "New count: ", count

    elif buy == 'mug':
        # does it work?
        print "Buying a mug..."
        mug = 4.99
        request.session['price'] = mug
        #send total to session, then increment session total
        request.session['total'] = total + mug 

        print "New total: ", total
        print "New count: ", count

    elif buy == 'algo_book':
        # does it work?
        print "Buying an algorithm book..."
        algo_book = 29.99
        request.session['price'] = algo_book
        #send total to session, then increment session total
        request.session['total'] = total + algo_book 

        print "New total: ", total
        print "New count: ", count

    else:
        request.session['total'] = 'null'
   
    return render(request, 'display.html', { 'count' : count, 'total': total, 'price': price })

def go_back(request):
    return redirect('/')