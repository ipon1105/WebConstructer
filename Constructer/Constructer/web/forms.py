from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput

from .models import Project

User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title"]

        widgets = {
            "title": TextInput(attrs={
                'id': 'title',
                'type': 'text',
                'size': '25',
                'placeholder': 'Введите имя проекта'
            })
        }
        pass
    pass
