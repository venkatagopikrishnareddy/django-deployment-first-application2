from django.shortcuts import render
from django.http import HttpResponse 
def display(request):
    s='''
        <center>
            <h1 style='color:blue;'>
             HI STUDENTS WELCOME TO DJANGO
            </h1>
            <hr/>
        </center>
     ''';
    return HttpResponse(s);
def show(re):
    s='''
        <html>
            <head>
                <title>**KRISHNA**</title>
                <style>
                    h1{
                        color:blue;
                    }
                    h2{
                        color:red;
                    }
                    h3{
                        color:orange;
                    }
                    h4{
                        color:green;
                    }
                    h5{
                        color:red;
                    }
                    h2,h5{
                        background-color:lightcyan;
                    }
                    h1,h4{
                        background-color:cyan;
                    }
                    h3{
                        background-color:green;
                    }
                    h6{
                        color:black;
                        background-color:orange;
                    }
                </style>
                <body>
                    <center>
                        <h1>VENKATA</h1>
                        <hr color='black', width='95%'/>
                        <h2>GOPI</h2>
                        <hr color='black', width='90%'/>
                        <h3>KRISHNA</h3>
                        <hr color='black', width='85%'/>
                        <h4>REDDY</h4>
                        <hr color='black', width='80%'/>
                        <h5>EVURI</h5>
                        <hr color='black', width='75%'/>
                        <h6>Java Script(Programing in Webpage) <br/>
                            <script>
                                a=50
                                b=20
                                document.writeln(a+'<br/>')
                                document.writeln(b+'<br/>')
                                document.writeln(a+b+'<br/>')
                                document.writeln(a-b+'<br/>')
                                document.writeln(a*b+'<br/>')
                                document.writeln(a/b+'<br/>')
                                document.writeln(a%b+'<br/>')
                            </script>
                        </h6>
                    </center>
                </body>
            </head>
        </html>
     ''';
    return HttpResponse(s);

def homepage(request):
    htmldata='''<center>
                <style>
                    h1,h2,h3{
                        color:red;
                        background-color:lightgreen;
                    }
                </style>
        <h1>welcome to default homepage..!</h1>
        <hr/>
        <h1>your request page is not found...!</h1>
        <hr/>
        <h1>plz try other url or links!!!</h3>
        <hr/>
    </center>''';
    return HttpResponse(htmldata);
    