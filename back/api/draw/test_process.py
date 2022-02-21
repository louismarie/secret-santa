from rest_framework.test import APITestCase
from api.models import Event, Participant, BlackList
from django.contrib.auth.models import User
from faker import Faker

from api.draw.process import RunDraw

# Create your tests here.
class SecretSantaTestCase(APITestCase):
    def setUp(self):
        fake = Faker()
        user_fake = fake.profile(fields=None, sex=None)
        user = User.objects.create(username=user_fake['username'], email=user_fake['mail'])
        self.event = Event.objects.create(title="test", owner=user)
        self.participant1 = Participant.objects.create(name="1", email="1", event=self.event)
        self.participant2 = Participant.objects.create(name="2", email="2", event=self.event)
        self.participant3 = Participant.objects.create(name="3", email="3", event=self.event)
        BlackList.objects.create(participant=self.participant1, cannot_give=self.participant2)
        BlackList.objects.create(participant=self.participant2, cannot_give=self.participant3)
        BlackList.objects.create(participant=self.participant3, cannot_give=self.participant1)

    def test_check_draw_handle_blacklist(self):
        for _ in range(100):
            gifts = RunDraw.run(self.event)
            for participant, should_give in gifts.items():
                if participant == self.participant1.id:
                    self.assertNotEqual(should_give, self.participant2.id)
                elif participant == self.participant2.id:
                    self.assertNotEqual(should_give, self.participant3.id)
                elif participant == self.participant3.id:
                    self.assertNotEqual(should_give, self.participant1.id)

