from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome),
    path('home', views.home),
    path('constructer', views.constructer),
    #path('register', Register.as_view())
]