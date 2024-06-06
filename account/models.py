from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    '''Профиль пользователя'''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Профиль',
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
    date_of_join = models.DateField(
        auto_now_add=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
    )

    def __str__(self):
        return self.user.username
