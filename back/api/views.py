from rest_framework import viewsets, permissions
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from api.serializers import UserSerializer, EventSerializer, BlackListSerializer, StartDrawSerializer, BlackListItemSerializer, GiftListSerializer
from api.models import Event, BlackList, GiftList
from api.draw.process import RunDraw


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
        queryset = Event.objects.filter(owner=self.request.user).order_by('-created')[:5]
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list':
            return (IsAuthenticated(),)
        elif self.action == 'create':
            return (IsAuthenticated(),)
        return (IsAdminUser(),)

    def get_queryset(self):
        queryset = Event.objects.preftech_related("participants")
        return queryset

class BlackListViewSet(viewsets.ModelViewSet):
    queryset = BlackList.objects.all().order_by('-created')
    serializer_class = BlackListSerializer

    def list(self, request):
        #TODO: filter only one event
        queryset = Event.objects.filter(owner=self.request.user)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, validated_data):
        serializer = BlackListSerializer(data=validated_data.data)
        if serializer.is_valid():
            for block_item in validated_data.data['list']:
                serializerItem = BlackListItemSerializer(data=block_item)
                if serializerItem.is_valid():
                    serializerItem.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == 'list':
            return (IsAuthenticated(),)
        elif self.action == 'create':
            return (IsAuthenticated(),)
        return (IsAdminUser(),)

class StartDraw(viewsets.ModelViewSet):
    queryset = GiftList.objects.all().order_by('-created')
    serializer_class = StartDrawSerializer

    def create(self, request):
        serializer = StartDrawSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            draw_gifts = RunDraw.run(request.data['event'])

            for (participant, should_give) in draw_gifts.items():
                gift = {'participant': participant, 'should_give': should_give}
            serializer = GiftListSerializer(data=gift)
            if serializer.is_valid():
                serializer.save()
            else:
                raise Exception('Unable to store result draw')

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == 'create':
            return (IsAuthenticated(),)
        return (IsAdminUser(),)
