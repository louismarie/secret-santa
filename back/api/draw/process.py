import random
import uuid
from api.models import Participant, BlackList, GiftList
from api.serializers import GiftListSerializer

class RunDraw():

    def run(event):
        # add all participants
        draw_participants = []
        # add all blacklist participants
        draw_blacklist = {}

        participants = Participant.objects.filter(event=event)
        for e in participants:
            draw_participants.append(str(e.id))
            black_list = e.black_list_participant.all()
            for i in black_list:
                draw_blacklist['e.id'] = str(i.cannot_give.id)

        random.shuffle(draw_participants)

        found = False
        max_try = 10000
        nb_try = 1

        # result of draw
        draw_gifts = {}

        while (found is False) and (nb_try < max_try):
            for idx, e in enumerate(draw_participants):
                given_gift = draw_participants[(idx + 1) % len(draw_participants)]
                draw_gifts[e] = given_gift
                if (e in draw_blacklist) and (draw_blacklist[e] == given_gift):
                    # try again
                    nb_try = nb_try + 1
                    draw_gifts = []
                    break

                if len(draw_gifts) == len(draw_participants):
                    found = True

        if found is False:
            raise Exception('Unable to make draw')

        for (participant,should_give) in draw_gifts.items():
            uuid_participant = uuid.UUID(participant)
            uuid_should_give = uuid.UUID(should_give)
            gift = {}
            gift['participant'] = participant
            gift['should_give'] = should_give
            serializer = GiftListSerializer(data=gift)
            if serializer.is_valid():
                serializer.save()
            else:
                raise Exception('Unable to store result draw')

