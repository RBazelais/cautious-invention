from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    # return render(request, 'index.html')
    return HttpResponse("You're in blogs now")

def new(request):
    pass

def create(request):
    pass

def show(request):
    pass

def edit(request):
    pass

def delete(request):
    pass