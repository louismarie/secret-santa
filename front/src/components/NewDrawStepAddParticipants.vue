<template>
  <v-container>
    <v-form>
      <v-row class="text-center" justify="center">
        <v-col class="mb-4" cols="6">
          <h1 class="display-2 font-weight-bold mb-3">
            <div>Create New Draw</div>
                <v-text-field
                    label="Event title"
                    v-model="title"
                ></v-text-field>

                <div
                    v-for="(participant, i) in participants"
                    :key="i"
                    class="text-fields-row"
                >
                  <v-text-field
                      :label="participant.labelName"
                      v-model="participant.name"
                  ></v-text-field>

                  <v-text-field
                      :label="participant.labelEmail"
                      v-model="participant.email"
                  ></v-text-field>

                  <v-btn @click="remove(i)" class="error">delete</v-btn>
                </div>
                <v-btn @click="addParticipant" class="primary">Add Participant</v-btn>
                <br/>
                <v-btn @click="submit" class="primary">Submit</v-btn>
          </h1>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script lang="ts">

import {mapActions} from "pinia";
import {useEventStore} from "@/stores/event";

export default {
  name: 'NewDrawStepAddParticipants',

  data: () => ({
    title: '',
    participants: [{
      labelEmail: "email",
      email: "",
      labelName: "name",
      name: ""
    }]
  }),

  methods: {
    ...mapActions(useEventStore, ['addEvent']),
    addParticipant () {
      this.participants.push({
        labelEmail: "email",
        email: "",
        labelName: "name",
        name: ""
      })
    },
    submit() {
      this.addEvent(this.title, this.participants)
    },
    remove (index) {
      this.participants.splice(index, 1)
    }
  }
}
</script>
