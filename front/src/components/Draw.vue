<template>
  <v-container>
    <v-form>
      <v-row class="text-center">
        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3">
            <div>Create new draw</div>
          </h1>
          <RouterLink to="/newdraw">
            <v-btn
                class="mb-5"
                variant="outlined"
                color="primary">
              New random draw
            </v-btn>
          </RouterLink>
          <v-divider />
          <h1 class="display-2 font-weight-bold mb-3 mt-5">
            <div>Last 5 Draws</div>
          </h1>
          <div v-for="event in events">
            <v-col >
              <v-row cols="6" justify="center" class="mb-4">
                <v-card>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>{{event.title}}</v-list-item-title>
                      <v-list-item-subtitle>Participants</v-list-item-subtitle>
                      <v-list-item-subtitle v-for="p in event.participants">{{p.name}} - {{ p.email }}</v-list-item-subtitle>
                      <v-list-item-subtitle>BlackList</v-list-item-subtitle>
                      <v-list-item-subtitle v-for="p in event.participants">{{p.name}} - {{ p.email }}</v-list-item-subtitle>
                      <v-list-item-subtitle>Gifts</v-list-item-subtitle>
                      <v-list-item-subtitle v-for="p in event.participants">{{p.name}} - {{ p.email }}</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-card>
              </v-row>
            </v-col>
          </div>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>

import {mapActions, mapState} from "pinia";
import {useEventStore} from "../stores/event";

export default {
  name: 'Draw',

  data: () => ({
  }),

  mounted() {
    this.getEvents();
  },

  methods: {
    ...mapActions(useEventStore, ['getEvents']),
  },

  computed: {
    ...mapState(useEventStore, ['events']),
  }
}
</script>
