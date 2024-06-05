from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from tours import views

# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView, TokenVerifyView)


router = routers.DefaultRouter()
router.register(r'tour', views.TourViewSet, basename='tour')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    # jwt/ (create, refresh, verify)
    re_path(r'^auth/', include('djoser.urls.jwt')),
    # simplejwt
    # path(
    #     'api/token/',
    #     TokenObtainPairView.as_view(),
    #     name='token_obtain_pair'
    # ),
    # path(
    #     'api/token/refresh/',
    #     TokenRefreshView.as_view(),
    #     name='token_refresh'
    # ),
    # path(
    #     'api/token/verify/',
    #     TokenVerifyView.as_view(),
    #     name='token_verify'
    # ),
    # path('api/v1/tour/', views.TourAPIList.as_view()),
    # path('api/v1/tour/<int:pk>/', views.TourAPIUpdate.as_view()),
    # path('api/v1/tourdelete/<int:pk>/', views.TourAPIDestroy.as_view()),
]
