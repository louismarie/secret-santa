from rest_framework import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User

from api.models import Event, Participant

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

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ['name', 'email']

    def to_representation(self, obj):
        return {
            'name': obj.name,
            'email': obj.email,
        }

    def to_internal_value(self, data):
        return data

class EventSerializer(serializers.HyperlinkedModelSerializer):
    participants = serializers.RelatedField(many=True, required=True, queryset=Participant.objects.none())

    class Meta:
        model = Event
        fields = ['title', 'participants']

    def create(self, validated_data):
        print(validated_data)

        validated_data['owner'] = self.context['request'].user
        validated_data.pop('participants')
        return Event.objects.create(**validated_data)

    def to_internal_value(self, data):
        return data