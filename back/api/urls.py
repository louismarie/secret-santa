from django.urls import include, path
from rest_framework import serializers, viewsets, routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('alive', views.index, name='index'),
    path('auth', include('rest_framework.urls')),
]
