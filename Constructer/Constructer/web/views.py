from .serializers import WidgetSerializer, WidgetPropertySerializer, ProjectSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Project, Widget, WidgetProperty
from .forms import UserCreationForm, NewProjectForm
from django.shortcuts import render, redirect
from rest_framework import viewsets


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
