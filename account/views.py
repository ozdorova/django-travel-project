from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer, UserProfileUpdateSerializer


class UserProfileViewSet(
        mixins.RetrieveModelMixin,  # Выделение
        mixins.UpdateModelMixin,  # Обновление
        mixins.ListModelMixin,  # Список всех записей
        viewsets.GenericViewSet):  # viewsets.ModelViewSet

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return UserProfileUpdateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerProfileOrReadOnly()]
        return super().get_permissions()
