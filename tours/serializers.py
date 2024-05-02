from rest_framework import serializers
from .models import Tour


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = [
            'title', 'slug', 'description', 'tariff', 'place',
            'created', 'start_date', 'end_date', 'is_active', 'photo'
        ]
