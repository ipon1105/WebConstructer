from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


def home(request):
    # переменная projects - хранит массив всех проектов пользователя

    context = {
        'user': {},
        'title': 'Домашняя страница',
        'projects': []
    }
    return render(request, 'web/home.html', context)

def welcome_register(request):
    context = {
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
        'form': UserCreationForm()
    }
    return render(request, 'web/welcome.html', context)


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
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
    }
    return render(request, 'web/welcome.html', context)


def login(request):

    context = {
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
    }
    return render(request, 'web/login.html', context)


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