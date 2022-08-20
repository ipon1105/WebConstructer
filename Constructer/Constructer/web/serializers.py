# serializers.py
from rest_framework import serializers

from .models import Widget


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Widget
        fields = ('id', 'title', 'name', 'single')
