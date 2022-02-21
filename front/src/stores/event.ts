import { defineStore } from 'pinia'
import { apiPost, apiGet } from '@/plugins/api';

type TypeParticipant = {
  email: string,
  name: string
}

type TypeEvent = {
  title: string,
  participants: TypeParticipant[]
}

export type TypeEvents = {
  events: TypeEvent[];
};

export const useEventStore = defineStore({
  id: 'event',
  state: () =>
      ({
        events: [],
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
        // now go to draw page
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
