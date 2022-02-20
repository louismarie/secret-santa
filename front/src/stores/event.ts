import { defineStore } from 'pinia'
import { apiPost } from '@/plugins/api';

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
  getters: {
    getEvents: (state) => state.events
  },
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
        this.events.push(newEvent)
        // now go to draw page
        this.router.push({name: 'draw'})
      } catch (error) {
        console.error(error)
        return error
      }
    },
  }
})
