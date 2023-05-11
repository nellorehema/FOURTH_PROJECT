from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def aa(request):
    return HttpResponse('<h1><marquee>alluarjun is the best dancer</marquee></h1>')
