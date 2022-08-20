from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View


def home(request):
    # переменная projects - хранит массив всех проектов пользователя

    context = {
        'user': request.user,
        'title': 'Домашняя страница',
        'projects': []
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

    myForm = AuthenticationForm(request.POST)

    if request.POST:
        #return welcome(request)
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


class Register(View):
    template_name = 'web/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)