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
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
