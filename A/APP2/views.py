from django.shortcuts import render
from django.http import HttpResponse
import datetime;
def f22(request):
    time=datetime.datetime.now();
    msg='<center><h1><h1 style=color:red;background-color:lightblue;/h1> Hello User..!<br/><br/>Server Date&Time::'+str(time)+'</h1></center><hr/>'
    return HttpResponse(msg);