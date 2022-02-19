from django.urls import include,path
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from . import views

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('alive', views.index, name='index'),
]
