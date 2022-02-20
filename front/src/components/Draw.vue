<template>
  <v-container>
    <v-form>
      <v-row class="text-center">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            <div>Draw Page</div>
            <RouterLink to="/newdraw">
              <v-btn
                  variant="outlined"
                  color="primary">
                New random draw
              </v-btn>
            </RouterLink>
          </h1>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>

export default {
  name: 'Draw',

  data: () => ({
  }),

  methods: {
  }
}
</script>
