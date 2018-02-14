from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_word(request):
    word = request.POST['word']
    timestamp = request.POST['timestamp']  
    color = request.POST.get('color', '')
    bold = request.POST.get('bold', 'regular')
    

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print "The method is POST"
        if color == 'red':
            print "The color is red"
            request.session['color'] = 'red'
            request.session['word'] = request.POST['word']
            request.session['timestamp'] = datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
            if bold == 'bold':
                print "The text is Bold"
                request.session['bold'] = 'bold'

        elif color == 'green':
            print "The color is green"
            request.session['color'] = 'green'
            request.session['word'] = request.POST['word']
            request.session['timestamp'] = datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
            if bold == 'bold':
                print "The text is bold"
                request.session['bold'] = 'bold'
        elif color == 'blue':
            print "The color is blue"
            request.session['color'] = 'blue'
            request.session['word'] = request.POST['word']
            request.session['timestamp'] = datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
            if bold == 'bold':
                print "The text is bold"
                request.session['bold'] = 'bold'
        else:
            print "There is no color"
            request.session['word'] = request.POST['word']
            request.session['timestamp'] = datetime.datetime.now().strftime('%H:%m%p, %B %d, %Y')
            if bold == 'bold':
                print "The text is Bold"
                request.session['bold'] = 'bold'
    
    context = {
        'word': word, 
        'timestamp': timestamp,
        'color': color,
        'bold': bold,
    }
    print "***********"
    print request.POST

    try:
        request.session['log']
    except:
        request.session['log'] = []

    request.session['log'].append({
        'word': request.POST['word'],
        'timestamp': request.session['timestamp'],
        'color': request.POST.get('color', ''),
        'bold': request.POST.get('bold', 'none'),
    })
     # 'content': '{} - added on {}'.format(word, datetime.now().strftime('%H:%m%p, %B %d, %Y'))
    return redirect('/', context)

def clear_session(request):
    request.session.flush()
    return redirect('/')

def result(request):
    return render(request, 'index.html')