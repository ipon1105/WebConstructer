from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField
from django.db import models


class CustomJsonField(models.JSONField):
    """Собственный парсер в JSON"""
    def from_db_value(self, value, expression, connection):
        if isinstance(value, dict):
            return value
        return super().from_db_value(value, expression, connection)


class User(AbstractUser):
    """Пользователь"""
    pass


class Project(models.Model):
    """Проект"""
    user_id = models.BigIntegerField(primary_key=False)
    title = models.CharField(max_length=25)
    data = CustomJsonField(default={'div':'div'})

    def __str__(self):
        return self.user_id
        pass
    pass


class Widget(models.Model):
    """Виджет"""
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    single = models.BooleanField()

    def __str__(self):
        return self.title
        pass
    pass


class WidgetProperty(models.Model):
    """Свойства Виджета"""
    parentId = models.BigIntegerField()
    title = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    measure = models.CharField(max_length=10)
    defaultValue = models.CharField(max_length=25)
    values = CustomJsonField(default=["none", ""])
    additionalData = CustomJsonField(default=['#ffffff', '#000000', 'rgb(255, 120, 0)'])

    def __str__(self):
        return self.title
        pass
    pass
