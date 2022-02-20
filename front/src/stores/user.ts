import { defineStore } from 'pinia'

export const userStore = defineStore({
  id: 'user',
  state: () => ({
    username: '',
    email: '',
    password: '',
    access: '',
    refresh: '',
  }),
  getters: {
    access: (state) => state.access
  },
  actions: {
  }
})
