import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DrawView from '@/views/DrawView.vue'
import NewDrawView from '@/views/NewDrawView.vue'

import {useUserStore} from "@/stores/user";
import {useEventStore} from "@/stores/event";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/draw',
      name: 'draw',
      component: DrawView
    },
    {
      path: '/newdraw',
      name: 'newdraw',
      component: NewDrawView
    },
  ]
})

router.beforeEach((to) => {
  useUserStore()
  useEventStore()
  return true
})

export default router
