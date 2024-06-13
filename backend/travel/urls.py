from django.contrib import admin
from django.urls import include, path
from djoser import views as djoser_views
from rest_framework import routers
from tours.views import TourViewSet

from .swagger import urlpatterns as swagger_urls

router = routers.DefaultRouter()
router.register(r'tour', TourViewSet, basename='tour')

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # apps
    path('api/v1/', include(router.urls,)),
    path('api/v1/', include(swagger_urls)),
    # djoser
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/users/logout', djoser_views.TokenDestroyView.as_view(), name='logout')
    # jwt/ (create, refresh, verify)
]
# urlpatterns += [re_path('auth/activate/', TemplateView.as_view(template_name='index.html'))]
