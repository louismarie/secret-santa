<script lang="ts">
import {mapState} from "pinia";
import {useEventStore} from "@/stores/event";

import NewDrawStepAddParticipants from '@/components/NewDrawStepAddParticipants.vue'
import NewDrawStepAddBlackList from '@/components/NewDrawStepAddBlackList.vue'
import NewDrawStepRunDraw from '@/components/NewDrawStepRunDraw.vue'

import NewDrawStepper from '@/components/NewDrawStepper.vue'

export default {
  name: 'NewDrawView',
  components: {
    NewDrawStepAddParticipants,
    NewDrawStepAddBlackList,
    NewDrawStepRunDraw,
    NewDrawStepper
  },
  computed: {
    ...mapState(useEventStore, ['eventCreationStep']),
  }
}
</script>

<template>
  <main>
    <NewDrawStepper />
    <NewDrawStepAddParticipants v-if="eventCreationStep === 1"/>
    <NewDrawStepAddBlackList v-if="eventCreationStep === 2" />
    <NewDrawStepRunDraw v-if="eventCreationStep === 3" />
  </main>
</template>


