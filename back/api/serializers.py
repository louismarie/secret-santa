from rest_framework import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User, Group

from api.models import Event

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(validated_data["password"])
            return super().create(validated_data)
        return JsonResponse(status=400)


class EventSerializer(serializers.Serializer):
    participants = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='participants'
    )

    class Meta:
        model = Event
        fields = ['title', 'participants']