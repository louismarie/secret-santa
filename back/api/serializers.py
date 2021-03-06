from rest_framework import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User

from api.models import Event, Participant, GiftList, BlackList, StartDraw

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

    def to_representation(self, obj):
        return {
            'name': obj.name,
            'email': obj.email,
            'id': obj.id,
            'blacklist': BlackListItemSerializer(obj.black_list_participant, many=True).data,
            'gift': GiftListSerializer(obj.gift_list_participant, many=True).data
        }

class EventSerializer(serializers.ModelSerializer):
    participants = serializers.RelatedField(many=True, required=True, queryset=Participant.objects.none())

    class Meta:
        model = Event
        fields = ['title', 'participants']

    def create(self, validated_data):
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
            'id': obj.id,
            'participants': ParticipantSerializer(obj.participants, many=True).data
        }

class BlackListItemSerializer(serializers.ModelSerializer):
    participant = serializers.PrimaryKeyRelatedField(queryset=Participant.objects.all())
    cannot_give = serializers.PrimaryKeyRelatedField(queryset=Participant.objects.all())

    class Meta:
        model = BlackList
        fields = ['participant', 'cannot_give']

class BlackListSerializer(serializers.ModelSerializer):
    list = BlackListItemSerializer(many=True)

    class Meta:
        model = BlackList
        fields = ['list']

class GiftListSerializer(serializers.ModelSerializer):
    participant = serializers.PrimaryKeyRelatedField(queryset=Participant.objects.all())
    should_give = serializers.PrimaryKeyRelatedField(queryset=Participant.objects.all())

    class Meta:
        model = GiftList
        fields = ['participant', 'should_give']

class StartDrawSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    class Meta:
        model = StartDraw
        fields = ['event']