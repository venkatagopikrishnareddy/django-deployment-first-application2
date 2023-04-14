from django.shortcuts import render
from django.http import HttpResponse
def f11(request):
    s='''
    <h1 style=color:blue;background-color:lightgreen;text-align:center;>
    Hello Good Morning User..!Have A Nice Day..!!
    </h1>
    <hr/>
    ''';
    return HttpResponse(s);