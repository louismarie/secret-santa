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
            <div>Last 5 draws</div>
          </h1>
          <div v-for="event, idxEvent in events">
            <v-col >
              <v-row cols="6" justify="center" class="mb-4">
                <v-card
                    min-width="500px"
                    rounded
                    elevation="10"
                    shaped
                >
                  <v-list-item>
                    <v-list-item-header>
                      <v-list-item-title><strong>{{event.title}}</strong></v-list-item-title>
                    </v-list-item-header>
                  </v-list-item>

                  <v-list-item>
                    <v-list-item-header>
                      <v-list-item-title>Participants</v-list-item-title>
                      <v-list-item-subtitle v-for="p in event.participants">
                        <p>{{p.name}}</p>
                        <p>Blacklist settings :</p>
                        <p v-if="p.blacklist.length === 0">-</p>
                        <p v-for="b in p.blacklist">
                          {{nameFromUUID(b.participant, idxEvent)}} will not offer a gift to {{ nameFromUUID(b.cannot_give, idxEvent) }}
                        </p>
                        <p>Result random draw :</p>
                        <p v-for="g in p.gift">
                          {{nameFromUUID(g.participant, idxEvent)}} should offer a gift to {{ nameFromUUID(g.should_give, idxEvent) }}
                        </p>
                        <br/>
                      </v-list-item-subtitle>
                    </v-list-item-header>
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

<script lang="ts">

import {mapActions, mapState} from "pinia";
import {useEventStore} from "@/stores/event";

export default {
  name: 'Draw',

  data: () => ({
  }),

  mounted() {
    this.getEvents();
  },

  methods: {
    ...mapActions(useEventStore, ['getEvents']),
    nameFromUUID(uuid:string, idxEvent:number): string {
      console.log("store : ", this.events)
      const event = this.events[idxEvent];
      if (event) {
        return event.participants.find((p) => p.id === uuid).name
      }
      return ''
    }
  },

  computed: {
    ...mapState(useEventStore, ['events']),
  }
}
</script>
