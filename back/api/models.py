from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    participants = models.ForeignKey(Participant, on_delete=models.CASCADE)




