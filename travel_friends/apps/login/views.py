from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . import models
from models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        new_user = User.objects.reg_validation(request.POST)#registering validation 
        if type(new_user) is list:
                for error in new_user:
                    messages.add_message(request, messages.ERROR, error)
                return redirect('/')
        else:
            request.session['user_id'] = new_user.id # set session to newly created user_id
            return redirect("travels/{}".format(new_user.id))
    else:
        return redirect('/')
    

def login(request):
    if request.method == "POST":
        login = User.objects.login_validation(request.POST)
        if type(login) is unicode:
                for error in login:
                    messages.add_message(request, messages.ERROR, error)
                return redirect('/')
        else:
            request.session['user_id'] = login.id
            return redirect("travels/{}".format(login.id))
    else:
        return redirect('/')

def logout(request):
	request.session.clear()	
	return redirect('/')

def travels(request, id):
    if 'user_id' not in request.session:
        print "The user is not in session"
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        print "user.id: " + str(user.id)
        return render(request, "dashboard.html", {'user': user})