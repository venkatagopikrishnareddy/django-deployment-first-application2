from django.urls import path;
from multiview import views;

urlpatterns=[
	path('mrng/',views.f1),
    path('after/',views.f2),
    path('evng/',views.f3),
];