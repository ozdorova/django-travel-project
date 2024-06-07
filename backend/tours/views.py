from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Place, Tour
from .permissions import UserPermission
from .serializers import (TourCreateUpdateSerializer, TourDetailSerializer,
                          TourSerializer)


class TourViewSet(
        mixins.CreateModelMixin,  # Создание
        mixins.RetrieveModelMixin,  # Выделение
        mixins.UpdateModelMixin,  # Обновление
        mixins.DestroyModelMixin,  # Удаление
        mixins.ListModelMixin,  # Список всех записей
        viewsets.GenericViewSet):  # viewsets.ModelViewSet

    '''ModelViewSet всех доступных туров'''
    queryset = Tour.active_tours.all()
    serializer_class = TourSerializer
    # permission_classes = [
    #     UserPermission,
    # ]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TourDetailSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return TourCreateUpdateSerializer
        return super().get_serializer_class()

    # def get_queryset(self):
    #     return Tour.objects.all()[:2]

    @action(
        methods=['get'],
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def places(self, request):
        '''Маршрут: список городов'''
        places = Place.objects.values().distinct()
        return Response(places)
