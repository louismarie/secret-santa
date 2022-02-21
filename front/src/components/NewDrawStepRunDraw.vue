<template>
  <v-container>
    <v-form>
      <v-row class="text-center">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            <div>Almost finished !</div>
          </h1>
            <v-btn
                @click="startDraw"
                class="mb-5"
                variant="outlined"
                color="primary">
              Start Random Draw
            </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script lang="ts">

import {mapActions} from "pinia";
import {useEventStore} from "@/stores/event";

export default {
  name: 'NewDrawStepRunDraw',

  data: () => ({
  }),

  methods: {
    ...mapActions(useEventStore, ['startDraw']),
  },
}
</script>
