from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from . import models
# from models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    results = User.objects.register_valdiation(request.POST)
    if results[0]:
        request.session['user_id'] = results[1].id
        print "******* New User registered ******"
        return redirect("/pokes/")
    else:
        for err in results[1]:
            messages.error(request, err)
        print "******* Registration Failed, see errors ******"
        return redirect('/lr_app')

def login(request):
    results = User.objects.login_validation(request.POST)
    
    if results[0]:
        request.session['user_id'] = results[1].id 
        print "******* logged in yo! ******"
        print request.session['user_id']
        return redirect("/pokes")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/lr_app')

def logout(request):
	request.session.clear()	
	return redirect('/lr_app')