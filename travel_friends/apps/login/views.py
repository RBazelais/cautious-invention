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
        return redirect("/travels/")
    else:
        for err in results[1]:
            messages.error(request, err)
        print "******* Registration Failed, see errors ******"
        return redirect('/lr_app')
    # if request.method == "POST":
    #     new_user = User.objects.reg_validation(request.POST)#registering validation 
    #     if type(new_user) is list:
    #             for error in new_user:
    #                 messages.add_message(request, messages.ERROR, error)
    #             return redirect('/')
    #     else:
    #         request.session['user_id'] = new_user.id # set session to newly created user_id
    #         return redirect("/travels/")
    # else:
    #     return redirect('/') 

def login(request):
    results = User.objects.login_validation(request.POST)
    
    if results[0]:
        request.session['user_id'] = results[1].id 
        print "******* logged in yo! ******"
        print request.session['user_id']
        return redirect("/travels")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect('/lr_app')

def logout(request):
	request.session.clear()	
	return redirect('/lr_app')

# def travels(request, id):
#     if 'user_id' not in request.session:
#         print "The user is not in session"
#         return redirect('/lr_app')
#     else:
#         user = User.objects.get(id=request.session['user_id'])
#         print "user.id: " + str(user.id)
#         return render(request, "travel_app/", {'user': user})