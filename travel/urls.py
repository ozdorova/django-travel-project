from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from account.views import UserProfileViewSet
from tours.views import TourViewSet, travel_app

# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView, TokenVerifyView)


router = routers.DefaultRouter()
router.register(r'tour', TourViewSet, basename='tour')
router.register(r'account', UserProfileViewSet, basename='account')

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # apps
    path('api/v1/', include(router.urls)),
    # Session Auth
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # djoser
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    # jwt/ (create, refresh, verify)
]
urlpatterns += [path('', travel_app)]

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
