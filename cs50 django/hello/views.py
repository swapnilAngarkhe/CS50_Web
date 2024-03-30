from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"hello/index.html")

def nikhil(request):
    return HttpResponse("Hey, nikhil")

def david(request):
    return HttpResponse("Hello, david")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}" , {
        "name":name.capitalize()
    }
)