from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import views


# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import FrontendTemplateView

router = routers.DefaultRouter()
router.register(r'widgets', views.WidgetViewSet)
router.register(r'widgets_property', views.WidgetPropertyViewSet)
router.register(r'project', views.ProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


urlpatterns = urlpatterns + [
    path('', FrontendTemplateView.as_view()),
    #path('', views.welcome, name="welcome"),
    path('welcome', views.welcome, name="welcome"),
    path('home', views.home, name="home"),
    path('home/new', views.home_new, name="home_new"),
    path('constructer', views.constructer, name="constructer"),
    path('welcome/register', views.welcome_register, name="welcome_register"),
    path('welcome/login', views.welcome_login, name="welcome_login"),
    path('logout', views.my_logout, name="logout"),
    path('home/del/<int:id>', views.delete),

    path('home/edit/<int:id>', views.edit)
]
urlpatterns += staticfiles_urlpatterns()