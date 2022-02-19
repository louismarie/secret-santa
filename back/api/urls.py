from django.urls import include, path
from rest_framework import serializers, viewsets, routers

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'blacklist', views.BlackListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
