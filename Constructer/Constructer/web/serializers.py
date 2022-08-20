# serializers.py
from rest_framework import serializers

from .models import Widget


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Widget
        fields = ('id', 'title', 'name', 'single')
        pass

    pass

# TODO: Создать сериализация для таблицы WidgetProperty


# TODO: Создать сериализация для таблицы Project
