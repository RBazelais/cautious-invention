from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    pass

def login(request):
    pass

def new(request):
    pass

def users(request):
    pass
