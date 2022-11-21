from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('lucky most iconic fellow')
def loverboy(request):
    return HttpResponse('suresh loves ajay')
    