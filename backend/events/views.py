from rest_framework import viewsets
from events.models import Event, Coordinates, EventLocation
from events.serializers import (EventSerializer,
                                CoordinatesSerializer,
                                EventLocationSerializer)


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Event"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CoordinatesViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Coordinates"""
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


class EventLocationViewSet(viewsets.ModelViewSet):
    """ViewSet для модели EventLocation"""
    queryset = EventLocation.objects.all()
    serializer_class = EventLocationSerializer
