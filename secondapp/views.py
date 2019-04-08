from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello Second APP !! <a href="/">Back to Home</a></h1>')

# Create your views here.
