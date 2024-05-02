from django.shortcuts import render
from rest_framework import generics
from .models import Tour
from .serializers import TourSerializer


class TourAPIView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
