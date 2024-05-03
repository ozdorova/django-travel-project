from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import generics
from .models import Tour
from .serializers import TourSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


# class TourAPIView(generics.ListAPIView):
#     queryset = Tour.objects.all()
#     serializer_class = TourSerializer

############################ Пример ############################
class TourAPIView(APIView):
    """Базовое представлене API для всех туров"""

    def get(self, request):
        tour_list = Tour.objects.all()
        return Response({'tours': TourSerializer(tour_list, many=True).data})

    def post(self, request):
        # проверка полученных данных
        serializer = TourSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # создание нового тура
        serializer.save()

        return Response({'tour': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Метод PUT недоступен'})

        try:
            instance = Tour.objects.get(pk=pk)
        except:
            return Response({'error': 'Обьект не найден'})

        serializer = TourSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Метод DELETE недоступен'})

        try:
            instance = Tour.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Обьект не найден'})

        return Response({'tour': f'Удален пост id: {pk}'})
