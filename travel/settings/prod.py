import os

from . import base

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
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ]


}
