from api.models import Participant, BlackList, GiftList

class RunDraw():
    def run(event):
        participants = Participant.objects.filter(event=event)
        blackList = BlackList.objects.filter(event=event)
        print(participants)
