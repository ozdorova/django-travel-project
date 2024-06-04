
# from rest_framework import mixins, viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Tour
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TourDetailSerializer, TourSerializer


class TourAPIList(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]


class TourAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer
    permission_classes = [
        IsOwnerOrReadOnly,
    ]


class TourAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourDetailSerializer
    permission_classes = [
        IsAdminOrReadOnly,
    ]


# class TourViewSet(mixins.CreateModelMixin,  # Создание
#                   mixins.RetrieveModelMixin,  # Выделение
#                   mixins.UpdateModelMixin,  # Обновление
#                   mixins.DestroyModelMixin,  # Удаление
#                   mixins.ListModelMixin,  # Список всех записей
#                   viewsets.GenericViewSet):  # viewsets.ModelViewSet
#
#     """ModelViewSet всех доступных туров"""
#     queryset = Tour.active_tours.all()
#     serializer_class = TourSerializer
#
#     actions = ['retrieve', 'create', 'update']
#
#     def get_serializer_class(self):
#         if self.action in self.actions:
#             return TourDetailSerializer
#         return super().get_serializer_class()
#
#     # def get_queryset(self):
#     #     return Tour.objects.all()[:2]
#
#     @action(methods=['get'], detail=False)
#     def cities(self, request):
#         """Маршрут: список городов"""
#         cities = self.get_queryset().values_list(
#             'places__city', flat=True
#         ).distinct().exclude(places__city='')
#         return Response(cities)
