from rest_framework import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User

from api.models import Event, Participant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(validated_data["password"])
            return super().create(validated_data)
        return JsonResponse(status=400)

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['name', 'email']

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.RelatedField(many=True, required=True, queryset=Participant.objects.none())

    class Meta:
        model = Event
        fields = ['title', 'participants']

    def create(self, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants')
        validated_data['owner'] = self.context['request'].user
        event = Event.objects.create(**validated_data)
        for participant in participants:
            Participant.objects.create(event=event, **participant)
        return event

    def to_internal_value(self, data):
        return data

    def to_representation(self, obj):
        return {
            'title': obj.title,
        }