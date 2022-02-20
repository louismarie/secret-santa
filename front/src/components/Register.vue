<template>
  <v-container>
    <v-row class="text-center">
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          <div>Welcome to Secret Santa</div>
        </h1>
      </v-col>

      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-5">
          Register
        </h2>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="6">
        <v-text-field
            label="Username"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center">
     <v-col cols="6">
        <v-text-field
            label="Email"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="6">
        <v-text-field
            label="Password"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col>
        <v-row class="mb-5" justify="center">
          <v-btn variant="outlined"
                 color="primary">
            Register now
          </v-btn>
        </v-row>
        <v-row justify="center">
          <a>Already have account ?</a>
        </v-row>
      </v-col>


    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'HelloWorld',

  data: () => ({

  }),
}
</script>
