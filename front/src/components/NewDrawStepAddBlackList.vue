<template>
  <v-container>
    <v-form>
      <v-row class="text-center" justify="center">
        <v-col class="mb-3" cols="6">
          <h1 class="display-2 font-weight-bold mb-3">
            <div class="mb-5" >Add to Black List</div>
            <div
                v-for="(relation, i) in blacklist"
                :key="i"
                class="text-fields-row"
            >
              <v-select
                  label="name"
                  :options="creationEvent.participants"
                  v-model="relation.participant"
                  :reduce="p => p.id"
              ></v-select>

              <span>Does not offer a gift to</span>

              <v-select
                  label="name"
                  :options="creationEvent.participants"
                  v-model="relation.cannot_give"
                  :reduce="p => p.id"
              ></v-select>

              <v-btn @click="remove(i)" class="error">delete</v-btn>
            </div>
            <v-btn @click="addBlackListItem" class="primary">Add</v-btn>
            <br/>

            <v-btn @click="submit" class="primary">Submit</v-btn>
          </h1>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script lang="ts">
import {mapActions, mapState} from "pinia";
import {useEventStore} from "@/stores/event";

export default {
  name: 'NewDrawStepAddBlackList',

  data: () => ({
    blacklist: [],
  }),

  methods: {
    ...mapActions(useEventStore, ['addBlackList']),
    addBlackListItem () {
      this.blacklist.push({
        participant: '',
        cannot_give: '',
      })
    },
    submit() {
      this.addBlackList(this.blacklist)
    },
    remove (index) {
      this.blacklist.splice(index, 1)
    }
  },

  computed: {
    ...mapState(useEventStore, ['creationEvent']),
  }
}
</script>
