from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Error 404<h4>')

def about(request):
    return HttpResponse('<h4>Привет<h4>')
