from django.urls import path;
from a1 import views;


urlpatterns=[
	path('a1/',views.display),
    path('a2/',views.display),
    path('a3/',views.display),
    path('s1/',views.show),
    path('s2/',views.show),
    path('s3/',views.show),
	
];
