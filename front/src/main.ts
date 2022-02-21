import { createApp } from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import { loadFonts } from '@/plugins/webfontloader'
import { createPinia } from 'pinia'
// @ts-ignore
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { markRaw } from 'vue'
import router from './router'
// @ts-ignore
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';

loadFonts()

const pinia = createPinia()

const app = createApp(App)
  .use(vuetify)
  .use(router)
  .use(pinia)
  .component('v-select', vSelect)
  .mount('#app')

// @ts-ignore
pinia.use(({ store }) => {
    store.router = markRaw(router)
})
pinia.use(piniaPluginPersistedstate)

