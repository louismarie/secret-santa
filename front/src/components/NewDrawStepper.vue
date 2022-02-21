<template>
  <v-container>
    <v-row class="text-center">
      <v-col col="12">
        <div class="justify-center">
          <v-breadcrumbs :items="eventCreationSteps">
            <template v-slot:divider>
              <v-icon icon="mdi-forward"></v-icon>
            </template>
          </v-breadcrumbs>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import {mapState} from "pinia";
import {useEventStore} from "../stores/event";

export default {
  name: 'NewDrawStepper',

  data: () => ({
  }),

  methods: {
  },

  computed: {
    ...mapState(useEventStore, ['eventCreationSteps']),
  }
}
</script>
