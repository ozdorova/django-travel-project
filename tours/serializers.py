import io

from rest_framework import serializers
from traitlets import default
from .models import Tour
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class TourSerializer(serializers.Serializer):
    """Сериализатор не связанный с моделью"""
    title = serializers.CharField(max_length=250)
    slug = serializers.SlugField(max_length=250)
    description = serializers.CharField()
    place_id = serializers.IntegerField()
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True)
    # photo = serializers.ImageField(allow_empty_file=True)

    def create(self, validated_data):
        return Tour.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.place_id = validated_data.get('place_id', instance.place_id)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.start_date = validated_data.get(
            'start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.save()
        return instance

############################## Примеры ##############################
# class TourModel:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description

# def encode():
#     """Пример кодирования"""
#     model = TourModel('Тестовый тур', 'Описание тестового тура')
#     model_sr = TourSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     return json


# def decode():
#     """Пример декодирование данных"""
#     stream = io.BytesIO(b'{"title":"\xd0\xa2\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x82\xd1\x83\xd1\x80","description":"\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x82\xd1\x83\xd1\x80\xd0\xb0"}')
#     data = JSONParser().parse(stream)
#     serializer = TourSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)


# # class TourSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Tour
# #         fields = [
# #             'title', 'slug', 'description', 'tariff', 'place',
# #             'created', 'start_date', 'end_date', 'is_active', 'photo'
# #         ]
