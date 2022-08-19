from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
#from users.froms import UserCreationForm


def home(request):
    context = {
        'user': {},
        'title':'Домашняя страница',
        'projects': []
    }
    return render(request, 'web/home.html', context)


def constructer(request):
    return render(request, 'web/constructor.html')


def welcome(request):
    context = {
        'title': 'Welcome',
        'header_name': 'Здравствуйте.',
    }
    return render(request, 'web/welcome.html', context)


def register(request):
    return render(request, 'web/welcome.html')


def logout(request):

    return render(request, 'web/welcome.html')


def login(request):

    return render(request, 'web/welcome.html')

'''class Register(View):
    template_name = 'registration/register.html'
    def get(self, request):
        context={
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        context={
            'form': form
        }
        return render(request, self.template_name, context)'''