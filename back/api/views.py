from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from api.serializers import UserSerializer, EventSerializer
from api.models import Event

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return (AllowAny(),)
        return (IsAdminUser(),)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-created')
    serializer_class = EventSerializer

    def list(self, request):
        queryset = Event.objects.filter(owner=self.request.user)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list':
            return (IsAuthenticated(),)
        return (IsAdminUser(),)