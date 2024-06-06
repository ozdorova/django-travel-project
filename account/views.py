from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import UserProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer


class UserProfileViewSet(mixins.CreateModelMixin,  # Создание
                         mixins.RetrieveModelMixin,  # Выделение
                         mixins.UpdateModelMixin,  # Обновление
                         mixins.DestroyModelMixin,  # Удаление
                         mixins.ListModelMixin,  # Список всех записей
                         viewsets.GenericViewSet):  # viewsets.ModelViewSet

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerProfileOrReadOnly()]
        return super().get_permissions()
