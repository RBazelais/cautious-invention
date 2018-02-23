from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . import models
from models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    results = User.objects.register_valdiation(request.POST)
    if results[0]:
        request.session['user_id'] = results[1].id
        print "******* New User registered ******"
        return redirect("/success")
    else:
        for err in results[1]:
            messages.error(request, err)
        print "******* Registration failed, see errors ******"
        return redirect('/')

def login(request):
    results = User.objects.login_validation(request.POST)
    
    if results[0]:
        request.session['user_id'] = results[1][0].id 
        print "******* User is logged in! ******"
        print request.session['user_id']
        return redirect("/success")
    else:
        for err in results[1]:
            messages.error(request, err)
        print "******* Login failed, see errors ******"
        return redirect('/')

def success(request):
    user = User.objects.get(id = request.session['user_id'])
    return render(request, 'success.html', {'user': user})

def logout(request):
	request.session.flush()	
	return redirect('/')