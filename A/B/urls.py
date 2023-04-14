from django.urls import path;
from B import views;


urlpatterns=[
	path('b/',views.b),
    path('b1/',views.b1),
    path('time/',views.senddatetime),
];