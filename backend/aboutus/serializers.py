from rest_framework import serializers

from aboutus.models import (AboutUs, FederalTeam,
                            RegionalTeam, PartnerType, 
                            Partner, Gallery, Media, Region)


class AboutUsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели AboutUs"""
    class Meta:
        model = AboutUs
        fields = ['mission', 'history']


class FederalTeamSerializer(serializers.ModelSerializer):
    """Сериализатор для модели FederalTeam"""
    class Meta:
        model = FederalTeam
        fields = ['name', 'description']


class RegionalTeamSerializer(serializers.ModelSerializer):
    """Сериализатор для модели RegionalTeam"""
    class Meta:
        model = RegionalTeam
        fields = ['name', 'description', 'region']


class PartnerTypeSerializer(serializers.ModelSerializer):
    """Сериализатор для модели PartnerType"""
    class Meta:
        model = PartnerType
        fields = ['type']


class PartnerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Partner"""
    type = serializers.StringRelatedField()

    class Meta:
        model = Partner
        fields = ['name', 'description', 'type']


class GallerySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Gallery"""
    class Meta:
        model = Gallery
        fields = ['name', 'description']


class MediaSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Media"""
    gallery = serializers.StringRelatedField()

    class Meta:
        model = Media
        fields = ['gallery', 'file']


class RegionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Region"""
    class Meta:
        model = Region
        fields = ['name']
