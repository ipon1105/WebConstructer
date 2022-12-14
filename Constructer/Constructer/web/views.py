from django.contrib import messages
from django.views import View

from .serializers import WidgetSerializer, WidgetPropertySerializer, ProjectSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Project, Widget, WidgetProperty
from .forms import UserCreationForm, NewProjectForm
from django.shortcuts import render, redirect
from rest_framework import viewsets

import json



class WidgetViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all().order_by('id')
    serializer_class = WidgetSerializer


class WidgetPropertyViewSet(viewsets.ModelViewSet):
    queryset = WidgetProperty.objects.all().order_by('id')
    serializer_class = WidgetPropertySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer


def getProjectsById(id):
    return Project.objects.filter(user_id=id)


def delete(request, id):
    getProjectsById(request.user.id).filter(id=id).delete()
    return redirect('home')
    pass


# TODO: Изменение проектов
def edit(request, id):
    context = {
        'title': 'Домашняя страница',
        'projects': getProjectsById(request.user.id),
        'form': NewProjectForm
    }
    return render(request, 'web/home.html', context)
    pass

def home(request):
    if request.user.id == None:
        return redirect('welcome')

    if request.method == 'GET':
        post = request.GET

    context = {
        'title': 'Домашняя страница',
        'projects': getProjectsById(request.user.id),
        'form': NewProjectForm
    }
    return render(request, 'web/home.html', context)


def home_new(request):
    if request.user.id == None:
        return redirect('welcome')

    if request.method == 'POST':
        col = Project(
            user_id=request.user.id,
            title=request.POST['title'],
            data={"div": "div"}
        )
        col.save()
        pass
    return redirect('home')


def my_logout(request):
    logout(request)
    return welcome(request)


def welcome_register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    context = {
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
        'form_reg': form
    }

    return render(request, 'web/welcome.html', context)


def welcome_login(request):
    form = AuthenticationForm(request)
    if request.POST:

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
        pass

    context = {
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
        'form_log': form
    }

    return render(request, 'web/welcome.html', context)
    pass


def constructer(request):
    if request.user.id is None:
        return redirect('welcome')

    context = {
        'title': 'Конструктор',
        'header_name': 'Конструктор'
    }
    return render(request, 'web/constructer.html', context)


def welcome(request):
    context = {
        'user': request.user,
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
    }
    return render(request, 'web/welcome.html', context)


class FrontendTemplateView(View):
    def post(self, request):
        # Собираем все параметры запроса в контекст
        context = {
            'post_data': request.body,
            'get_data': json.dumps(request.GET)  # Сериализуем в JSON
        }

        # Отправляем клиенту отрендеренный с контекстом шаблон
        return render(request, 'index.html', context)
    pass

