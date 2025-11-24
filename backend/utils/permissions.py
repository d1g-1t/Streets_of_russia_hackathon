from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Права доступа к объекту в зависимости от запроса:
    GET, LIST - всем пользователям
    POST - аутентифицированным
    PATCH, DESTROY - автору экземпляра
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
            )
