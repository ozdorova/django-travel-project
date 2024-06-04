
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Place, Programm, Tariff, Tour


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = [
            'city',
            'region',
            'country',
        ]


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = [
            'title',
            'conditions',
            'price'
        ]


class ProgrammSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programm
        fields = [
            'title',
            'order',
            'description',
            'photo',
        ]


class TourSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tour
        fields = [
            'id',
            'owner',
            'title',
            'slug',
            'description',
            'places',
            'created',
            'start_date',
            'end_date',
            'is_active',
            'photo',
            # 'programm',
        ]


class TourDetailSerializer(TourSerializer):
    programm = ProgrammSerializer(many=True)
    tariffs = TariffSerializer(many=True)

    class Meta(TourSerializer.Meta):
        fields = TourSerializer.Meta.fields + ['tariffs', 'programm']
