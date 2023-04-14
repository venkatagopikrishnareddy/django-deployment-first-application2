from django.shortcuts import render
from django.http import HttpResponse
def b (request):
    print('welcome url requestd & display() is executed');
    s='''
        <center>
            <h1 style='color:blue;'>
             Hello students
            </h1>
            <hr/>
        </center>
    ''';
    return HttpResponse(s);
def b1(request):
    print('welcome url requestd & display() is executed');
    s='''
        <center>
            <h1 style='color:Green;'>
             How are You
            </h1>
            <hr/>
        </center>
    ''';
    return HttpResponse(s);
    
import time;	
def senddatetime(request):
    print("dtime/ url is requested & senddatetime() is executed");
    ct = time.ctime()
    print("Client Request Date & time on server :: ",ct);
    ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
    return HttpResponse(ss);

