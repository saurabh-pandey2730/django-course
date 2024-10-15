from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse('this works january!')

def february(request):
    return HttpResponse('this works! february')
