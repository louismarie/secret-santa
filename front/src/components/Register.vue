<template>
  <v-container>
    <v-form v-model="valid">
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
              v-model="username"
              label="Username"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row justify="center">
       <v-col cols="6">
          <v-text-field
              v-model="email"
              label="Email"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="6">
          <v-text-field
              v-model="password"
              label="Password"
              :type="'password'"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col>
          <v-row class="mb-5" justify="center">
            <v-btn
                @click="register"
                variant="outlined"
                color="primary">
              Register now
            </v-btn>
          </v-row>
          <v-row justify="center">
            <a>Already have account ?</a>
          </v-row>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios'
import { rootUrl } from '../constants/api';

export default {
  name: 'HelloWorld',

  data: () => ({
    valid: false,
    showPass: false,
    username: '',
    email: '',
    password: '',
  }),

  methods: {
    async register() {
        const res = await axios.post(rootUrl + 'users', {
          username: this.username,
          password: this.password,
          email: this.email
        }, {
          headers: {
            "Content-Type": "application/json"
          }
        });
        console.log(res);
    }
  }
}
</script>
