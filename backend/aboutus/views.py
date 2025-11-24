from rest_framework import viewsets

from aboutus.serializers import (AboutUsSerializer,
                                 FederalTeamSerializer, 
                                 RegionalTeamSerializer, 
                                 PartnerTypeSerializer,
                                 PartnerSerializer,
                                 GallerySerializer,
                                 MediaSerializer,
                                 RegionSerializer)
from aboutus.models import (AboutUs, FederalTeam,
                            RegionalTeam, PartnerType, 
                            Partner, Gallery, Media, Region)


class AboutUsViewSet(viewsets.ModelViewSet):
    """ViewSet для модели AboutUs"""
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class FederalTeamViewSet(viewsets.ModelViewSet):
    """ViewSet для модели FederalTeam"""
    queryset = FederalTeam.objects.all()
    serializer_class = FederalTeamSerializer


class RegionalTeamViewSet(viewsets.ModelViewSet):
    """ViewSet для модели RegionalTeam"""
    queryset = RegionalTeam.objects.all()
    serializer_class = RegionalTeamSerializer


class PartnerTypeViewSet(viewsets.ModelViewSet):
    """ViewSet для модели PartnerType"""
    queryset = PartnerType.objects.all()
    serializer_class = PartnerTypeSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Partner"""
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Gallery"""
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class MediaViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Media"""
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class RegionViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Region"""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
