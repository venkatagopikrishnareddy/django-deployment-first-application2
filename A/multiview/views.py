from django.shortcuts import render
from django.http import HttpResponse
def f1(request):
    return HttpResponse('<h1>Good Morning User...!!</h1><hr/>');
def f2(request):
    return HttpResponse('<h1>Good AfterNoon User...!!</h1><hr/>');
def f3(request):
    return HttpResponse('<h1>Good Evening User...!!</h1><hr/>');