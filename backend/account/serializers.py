from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserProfile

User = get_user_model


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
