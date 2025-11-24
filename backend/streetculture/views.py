from rest_framework import viewsets

from streetculture.models import StreetCulture
from streetculture.serializers import StreetCultureSerializer


class StreetCultureViewSet(viewsets.ModelViewSet):
    """ViewSet для модели StreetCulture"""
    queryset = StreetCulture.objects.all()
    serializer_class = StreetCultureSerializer
