
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
            'id',
            'city',
            'region',
            'country',
        ]


class TariffSerializer(serializers.ModelSerializer):
    '''Сериализатор тарифов'''
    class Meta:
        model = Tariff
        fields = [
            'title',
            'conditions',
            'price'
        ]


class ProgrammSerializer(serializers.ModelSerializer):
    '''Сериализатор программы тура '''
    class Meta:
        model = Programm
        fields = [
            'title',
            'order',
            'description',
            'photo',
        ]


class TourCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tour
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    '''Сериализатор тура'''
    places = PlaceSerializer(many=True)
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tour
        fields = [
            'id',
            # 'owner',
            'title',
            'slug',
            'description',
            'places',
            'created',
            'start_date',
            'end_date',
            'is_active',
            'photo',
        ]


class TourDetailSerializer(TourSerializer):
    '''Сериализатор конретного тура по pk
    включащий в себя программу тура и тарифы'''
    programm = ProgrammSerializer(many=True, required=False)
    tariffs = TariffSerializer(many=True, required=False)

    class Meta(TourSerializer.Meta):
        fields = TourSerializer.Meta.fields + ['programm', 'tariffs']
