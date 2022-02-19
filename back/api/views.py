from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from api.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]