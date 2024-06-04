"""Кастомные разрешения"""

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
