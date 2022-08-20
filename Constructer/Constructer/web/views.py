from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from .forms import UserCreationForm, NewProjectForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .models import Project

# views.py
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Widget


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all().order_by('id')
    serializer_class = HeroSerializer

# TODO: Добавить обработчик сериализированных данных для WidgetProperty


# TODO: Добавить обработчик сериализированных данных для Project


def getProjectsById(id):
    return Project.objects.filter(user_id=id)

# TODO: Удаление проектов

# TODO: Изменение проектов

# TODO: Перенаправлять на новую страницу

def home(request):
    if request.user.id == None:
        return redirect('welcome')

    print("-> HOME")
    # переменная projects - хранит массив всех проектов пользователя

    context = {
        'title': 'Домашняя страница',
        'projects': getProjectsById(request.user.id),
        'form': NewProjectForm
    }
    return render(request, 'web/home.html', context)


def home_new(request):
    if request.user.id == None:
        return redirect('welcome')

    print("-> HOME_NEW")
    # переменная projects - хранит массив всех проектов пользователя

    # TODO: Сделать добавление элементов в Базу данных
    if request.method == 'POST':
        col = Project(
            user_id=request.user.id,
            title=request.POST['title'],
            data={"div": "div"}
        )
        col.save()
        pass
    form = NewProjectForm()

    context = {
        'title': 'Домашняя страница',
        'projects': getProjectsById(request.user.id),
        'form': form
    }
    return render(request, 'web/home.html', context)


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
    # TODO: Разобраться с корректностью вводимых данных
    # myForm = AuthenticationForm(request.POST)
    # if myForm.is_valid():
    #    return welcome(request)

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('home')
        pass

    context = {
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
        'form_log': AuthenticationForm()
    }

    return render(request, 'web/welcome.html', context)
    pass


def constructer(request):
    if request.user.id == None:
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
