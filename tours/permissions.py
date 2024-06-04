"""Кастомные разрешения"""

from logging import warn

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Чтение для всех пользователей,
    редактирование только для администратора"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Редактирование только для организатора тура"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class UserPermission(permissions.BasePermission):
    """Разрешение для ViewSet
    list: Все 
    Create: Все авторизованные
    Retrieve: owner, staff
    Update, Partial update: owner, staff
    Destroy: admin
    """

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
            # return request.user.is_authenticated or request.user.is_staff
        elif view.action == 'create':
            return request.user.is_authenticated

        # посмотреть потом работу ограничения
        elif view.action in [
            'retrieve',
            'update',
            'partial_update',
            'destroy'
        ]:
            return True

        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return True
        elif view.action in [
            'update',
            'partial_update'
        ]:
            return obj.owner == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False
