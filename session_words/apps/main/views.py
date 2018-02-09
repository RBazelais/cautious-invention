from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_word(request):
    word = request.POST['word']
    timestamp = request.POST['timestamp']
    # red = request.POST['red']
    # green = request.POST['green']
    # blue = request.POST['blue']
    # bigger_font = request.POST['bold']
    
    print word
    # print request.POST['red']
    # print request.POST['green']
    # print request.POST['blue']
    # print bigger_font

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        request.session['word'] = request.POST['word']
        request.session['timestamp'] = datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
        # request.session['red'] = request.POST['red']
        # request.session['green'] = request.POST['green']
        # request.session['blue'] = request.POST['blue']
        # request.session['bold'] = request.POST['bold']

    try:
        request.session['stuff']
    except:
        request.session['stuff'] = []

    context = {
        'word': word, 
        'timestamp': timestamp,
        # 'red' : red,
        # 'green' : green,
        # 'blue' : blue,
        # 'bold' : bigger_font
    }

    # if request.POST == request.session['red']:
    #     request.session['stuff'].append({
    #         'word':request.POST['word'], 
    #         'timestamp' : datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y'),
    #         # 'red': request.POST['red'], 
    #     })
    # elif request.POST == request.session['green']:
    #     request.session['stuff'].append({
    #         'green': request.POST['green'], 
    #         'word':request.POST['word'], 
    #         'timestamp' : datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
    #     })
    # elif request.POST == request.session['blue']:
    #     request.session['stuff'].append({
    #         'blue': request.POST['blue'], 
    #         'word':request.POST['word'], 
    #         'timestamp' : datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
    #     })
    # else:
    #     request.session['stuff'].append({
    #         'word': request.POST['word'], 
    #         'timestamp' : datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
    #     })

    return redirect('/', context)

def clear_session(request):
    request.session.flush()
    return redirect('/')

def result(request):
    return render(request, 'index.html')