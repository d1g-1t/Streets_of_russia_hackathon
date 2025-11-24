from rest_framework import serializers
from .models import Coordinates, EventLocation, Event


class CoordinatesSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Coordinates"""
    class Meta:
        model = Coordinates
        fields = '__all__'


class EventLocationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели EventLocation"""
    coordinates = CoordinatesSerializer(read_only=True)
    
    class Meta:
        model = EventLocation
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Event"""
    place = EventLocationSerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'
