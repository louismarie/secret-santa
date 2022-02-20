<template>
  <v-app>
    <v-main>
      <RouterView />
    </v-main>
  </v-app>
</template>

<script>
import Register from './components/Register.vue'

export default {
  name: 'App',

  components: {
    Register,
  },

  data: () => ({
    //
  }),
}
</script>
