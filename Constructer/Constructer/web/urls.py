from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('home', views.home, name="home"),
    path('constructer', views.constructer, name="constructer"),
    path('logout', views.logout, name="logout")
    #path('register', Register.as_view())
]