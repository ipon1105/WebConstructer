from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home', views.home, name='register'),
    path('constructer', views.constructer, name='constructer'),
    #path('register', Register.as_view())
]