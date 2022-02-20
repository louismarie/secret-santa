from django.urls import include, path
from rest_framework import serializers, viewsets, routers
from rest_framework.documentation import include_docs_urls

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'blacklist', views.BlackListViewSet)
router.register(r'startdraw', views.StartDraw)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs', include_docs_urls(title='Secret Santa API'))
]
