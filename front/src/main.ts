import { createApp } from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import { loadFonts } from '@/plugins/webfontloader'
import { createPinia } from 'pinia'
// @ts-ignore
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { markRaw } from 'vue'
import router from './router'

loadFonts()

const pinia = createPinia()

createApp(App)
  .use(vuetify)
  .use(router)
  .use(pinia)
  .mount('#app')


// @ts-ignore
pinia.use(({ store }) => {
    store.router = markRaw(router)
})
pinia.use(piniaPluginPersistedstate)

