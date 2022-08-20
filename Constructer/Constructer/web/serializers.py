from .models import Widget, Project, WidgetProperty
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализация проекта"""
    class Meta:
        model = Project
        fields = ('id', 'user_id', 'title', 'data')
        pass
    pass


class WidgetSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализация виджета"""
    class Meta:
        model = Widget
        fields = ('id', 'title', 'name', 'single')
        pass
    pass


class WidgetPropertySerializer(serializers.HyperlinkedModelSerializer):
    """Сериализация свойств виджета"""
    class Meta:
        model = WidgetProperty
        fields = ('id', 'parentId', 'title', 'field', 'type', 'measure', 'defaultValue', 'values', 'additionalData')
        pass
    pass
