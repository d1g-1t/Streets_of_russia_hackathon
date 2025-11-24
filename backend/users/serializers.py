from rest_framework import serializers

from users.models import CustomUser


class ManagementDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'last_name',
            'first_name',
            'third_name',
            'bio',
            'avatar'
        )


class ManagementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'last_name',
            'first_name',
            'third_name',
            'summary_bio',
            'avatar'
        )
