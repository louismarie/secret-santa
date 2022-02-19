import uuid

from django.db import models
from django.conf import settings

class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')

class BlackList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    blocked_by = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='block')
    block = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='blocked_by')



