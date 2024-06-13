from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from djoser.serializers import TokenCreateSerializer, UserCreateSerializer
from rest_framework import serializers

User = get_user_model()


class CustomTokenCreateSerializer(TokenCreateSerializer):

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        print(self.user)
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        if self.user:
            return attrs
        self.fail("invalid_credentials")


class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор пользователя'''
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'location',
            'email',
            'description',
        ]


class UserRegistrationSerializer(serializers.ModelSerializer):
    '''
    Сериализатор регистрации пользователя
    '''
    password = serializers.CharField(
        style={'input_type': 'password'},
        label='Пароль',
        write_only=True,
    )
    confirm_password = serializers.CharField(
        style={'input_type': 'password'},
        label='Подтвердите пароль',
        write_only=True,
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'location',
            'date_of_birth',
            'description',
            'password',
            'confirm_password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):

        password = self.validated_data['password']
        confirm_password = self.validated_data.pop('confirm_password')

        new_user = User(**self.validated_data)

        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают'}, code='authorization'
            )
        else:
            new_user.set_password(password)
            new_user.save()
            return new_user
