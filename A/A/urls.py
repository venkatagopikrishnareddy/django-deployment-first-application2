"""A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

#model-1(approch)
from APP1.views import f11
from APP2.views import f22
#model-2 (alias)
from APP1 import views as v11
from APP2 import views as v22







urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/',include('a1.urls')),
    path('b/',include('B.urls')),
    path('multiview1/',include('multiview.urls')),
    #model-1
    path('hello/',f11),
    path('datetime2/',f22),
    #model-2
    path('hello3/',v11.f11),
    path('datetime3/',v22.f22),
    
    
   
    
]
