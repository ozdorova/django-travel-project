from account.views import UserProfileViewSet
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from tours.views import TourViewSet

from .swagger import urlpatterns as swagger_urls

router = routers.DefaultRouter()
router.register(r'tour', TourViewSet, basename='tour')
router.register(r'account', UserProfileViewSet, basename='account')

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # apps
    path('api/v1/', include(router.urls,)),
    path('api/v1/', include(swagger_urls)),
    # Session Auth
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # djoser
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    # jwt/ (create, refresh, verify)
]
