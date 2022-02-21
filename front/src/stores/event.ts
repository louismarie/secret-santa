import { defineStore } from 'pinia'
import { apiPost, apiGet } from '@/plugins/api';

type TypeParticipant = {
  email: string,
  name: string
}

type TypeEvent = {
  id: string,
  title: string,
  participants: TypeParticipant[]
}

export type TypeEvents = {
  events: TypeEvent[];
  creationEvent: TypeEvent;
};

export type TypeBlackListItem = {
  participant: string,
  cannot_give: string
}

export type TypeBlackList = TypeBlackListItem[]

export const useEventStore = defineStore({
  id: 'event',
  state: () =>
      ({
        events: [],
        creationEvent: {
          id: '',
          title: '',
          participants: []
        },
        eventCreationSteps:
          [{
            text: 'Add Participants',
            disabled: false,
            href: 'breadcrumbs_dashboard',
          },
          {
            text: 'Add Black List',
            disabled: true,
            href: 'breadcrumbs_link_1',
          }],
        eventCreationStep: 1,
      } as TypeEvents),
  // @ts-ignore
  persist: true,
  actions: {
    async addEvent(title:string, participants:TypeParticipant[]) {
      try {
        const newEvent = await apiPost('events', {
          title,
          participants: participants.map((p) => {
            return {
              email: p.email,
              name: p.name
            }
          })
        })
        // now go to step black list
        // @ts-ignore
        this.creationEvent = newEvent
        // @ts-ignore
        this.eventCreationStep = 2
        // @ts-ignore
        this.eventCreationSteps[0].disabled = true
        // @ts-ignore
        this.eventCreationSteps[1].disabled = false
      } catch (error) {
        console.error(error)
        return error
      }
    },
    async addBlackList(blackList:TypeBlackList) {
      try {
        if (blackList.length > 0) {
          await apiPost('blacklist', {list: blackList})
        }
        // rest step black list
        // @ts-ignore
        this.eventCreationStep = 1
        // @ts-ignore
        this.eventCreationSteps[0].disabled = false
        // @ts-ignore
        this.eventCreationSteps[1].disabled = true
        await apiPost('startdraw', {
          // @ts-ignore
          event: this.creationEvent.id
        })
        // @ts-ignore
        this.router.push({name: 'draw'})
      } catch (error) {
        console.error(error)
        return error
      }
    },
    async getEvents() {
      try {
        // @ts-ignore
        this.events = await apiGet('events')
      } catch (error) {
        console.error(error)
        return error
      }
    },
  }
})
