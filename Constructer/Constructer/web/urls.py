from django.urls import path, include

from . import views
from .views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.welcome, name="welcome"),
    path('welcome', views.welcome, name="welcome"),
    path('home', views.home, name="home"),
    path('constructer', views.constructer, name="constructer"),
    path('register', views.welcome_register, name="register"),
    #path('register', Register.as_view(), name="register"),
    path('login', views.login, name="login")
]