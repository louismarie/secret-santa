<template>
  <v-container>
    <v-form>
      <v-row class="text-center">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            <div>Start new draw</div>
          </h1>
            <v-btn
                @clic="runDraw"
                class="mb-5"
                variant="outlined"
                color="primary">
              Run draw
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
  name: 'Draw',

  data: () => ({
  }),

  methods: {
    ...mapActions(useEventStore, ['runDraw']),
  },
}
</script>
