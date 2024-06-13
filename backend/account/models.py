from django.contrib.auth.models import (AbstractUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from tours import models as tour_models


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        username,
        email,
        first_name,
        last_name,
        password,
        **extra_fields
    ):
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_verified', False)

        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        username,
        email,
        first_name,
        last_name,
        password,
        **extra_fields
    ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(
            username,
            email,
            first_name,
            last_name,
            password,
            **extra_fields
        )


class User(AbstractUser, PermissionsMixin):
    '''Профиль пользователя'''
    is_active = models.BooleanField(
        default=False,
    )
    email = models.EmailField(
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Место проживания',
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
    )

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name',
    ]

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name.title()} {self.last_name.title()} - {self.email}'

    def get_tours_own(self):
        return tour_models.Tour.objects.filter(owner=self)
