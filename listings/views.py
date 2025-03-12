from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>nous aimons merch</p>')
def listing(request):
    return HttpResponse('<h1>Ma liste</h1> <p>nous aimons merch</p>')
def contacts(request):
    return HttpResponse('<h1>Nos contact</h1> <p>nous aimons merch</p>')