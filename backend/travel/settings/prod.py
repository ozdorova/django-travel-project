import os

from base import *

# export DJANGO_SETTINGS_MODULE=travel.settings.prod


DEBUG = False

ALLOWED_HOSTS = ['komrad_travel.ru']


ADMINS = [
    ('Mikhail B.', 'haxboxmiha@gmail.com'),
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DATETIME_FORMAT': '%d %B, %Y',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ]


}

CORS_ALLOWED_ORIGINS = ["https://example.com", "http://localhost:8080"]
CORS_ALLOW_CREDENTIALS = True
