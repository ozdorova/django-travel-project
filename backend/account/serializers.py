from rest_framework import serializers
from rest_framework.reverse import reverse

from tours.models import Tour

from .models import UserProfile


class ToursOwnByUserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='tour-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Tour
        fields = [
            'id',
            'url',
            'title'
        ]


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    '''Сериализатор пользователя'''
    url = serializers.HyperlinkedIdentityField(
        view_name='account-detail',
        lookup_field='pk',
    )
    user = serializers.StringRelatedField(read_only=True)
    full_name = serializers.CharField(
        source='user.get_full_name', read_only=True)
    email = serializers.CharField(
        source='user.email', read_only=True)
    tours = ToursOwnByUserSerializer(source='user.tour_owner', many=True)

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'url',
            'user',
            'full_name',
            'email',
            'description',
            'location',
            'date_of_birth',
            'tours',
        ]
