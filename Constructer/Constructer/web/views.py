from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


def home(request):
    context = {
        'user': {},
        'title': 'Домашняя страница',
        'projects': []
    }
    return render(request, 'web/home.html', context)


def constructer(request):
    # TODO: Если пользователь не вошёл, то переслать на страницу welcome.html
    context = {
        'user': {},
        'title': 'Конструктор',
        'projects': []
    }
    return render(request, 'web/constructor.html', context)


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