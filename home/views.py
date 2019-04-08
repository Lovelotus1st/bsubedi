from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Using Statig Url method: <br><a href="/home1">App1</a><br><a href="/home2">App2</a><br><a href="/home3">App3</a><br><br>Using Url Mapping<br><a href="/first">First App</a><br><a href="/second">Second App</a><br><a href="/third">Third App</a> </h1>')
def index1(request):
    return HttpResponse('<h1>Hello Home 1 using static URL!! <a href="/">Back to Home</a></h1>')
def index2(request):
    return HttpResponse('<h1>Hello Home 2 using static URL!! <a href="/">Back to Home</a></h1>')
def index3(request):
    return HttpResponse('<h1>Hello Home 3 using static URL!! <a href="/">Back to Home</a></h1>')
# Create your views here.