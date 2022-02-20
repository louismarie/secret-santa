import { defineStore } from 'pinia'
import { apiPost } from '@/plugins/api';

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    userData: {
      username: '',
      password: '',
      email: '',
    },
    userCreds: {
      access: '',
      refresh: '',
    },
  }),
  persist: true,
  getters: {
    loggedIn: (state) => state.userCreds.access !== '',
    accessToken: (state) => state.userCreds.access
  },
  actions: {
    async register(email:string, password:string) {
      try {
        this.userData = await apiPost('users', {
          username: email,
          password,
          email
        })
        // now login
        this.userCreds = await apiPost('auth', {
          username: email,
          password,
        })
        // now go to draw page
        this.router.push({name: 'draw'})
        console.log('done')
      } catch (error) {
        return error
      }
    },
  }
})
