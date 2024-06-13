from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
    ]

    ordering = ["first_name"]

    fieldsets = [
        ("Информация о пользователе", {
            "fields": [
                'username',
                'email',
                'first_name',
                'last_name',
                'date_of_birth',
                'location',
                'description',
            ]
        }),

        (
            "Статусы пользователя",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ],
                "classes": ["collapse"],
            },
        ),

        (
            None,
            {
                "fields": [
                    "last_login",
                ]
            },
        ),

        (None, {"fields": ["groups", "user_permissions"]}),
    ]

    add_fieldsets = (
        (
            "User Personal Details",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),

        (
            "User status",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
