from rest_framework import serializers
from streetculture.models import StreetCulture


class StreetCultureSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели StreetCulture'''
 
    class Meta:
        model = StreetCulture
        fields = [
            'name', 'description', 'photo', 'video', 'culture_type'
        ]
