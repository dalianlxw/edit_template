from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def upload(request):
    return HttpResponse("hello world")
