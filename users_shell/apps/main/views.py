from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("It's Alive!!!")
