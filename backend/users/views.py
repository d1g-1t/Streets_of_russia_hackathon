from rest_framework import permissions, viewsets

from users.models import CustomUser
from users.serializers import (
    ManagementDetailSerializer,
    ManagementListSerializer
)


class ManagementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.filter(role='fed manager')
    permission_classes = (permissions.AllowAny,)
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return ManagementListSerializer
        return ManagementDetailSerializer
