from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return (AllowAny(),)
        return (IsAdminUser(),)

