<template>
  <div>
    <v-row justify="center" align="center" class="mt-8">
      <v-col md="6" sm="12" xs="12" class="mt-8">
        <label for="username">نام کاربری</label>
        <v-text-field
          id="username"
          v-model="user_name"
          solo
          full-width
          outlined
          reverse
          class="username mt-2"
          background-color="grey lighten-4"
          color="primary"
        >
          <template slot="append">
            <v-icon class="mdi mdi-account-circle"></v-icon>
          </template>
        </v-text-field>
        <label for="password">رمز عبور</label>
        <v-text-field
          id="password"
          v-model="pass_word"
          solo
          full-width
          outlined
          reverse
          class="password mt-2"
          :type="show ? 'text' : 'password'"
          color="primary"
          background-color="grey lighten-4"
        >
          <template slot="append">
            <v-icon class="mdi mdi-lock"></v-icon>
            <v-icon
              :class="show ? 'mdi mdi-eye mr-2' : 'mdi mdi-eye-off mr-2'"
              @click="show = !show"
            ></v-icon>
          </template>
        </v-text-field>
        <v-btn
          block
          color="secondary"
          class="mt-2 font-weight-black black--text"
          elevation="2"
          x-large
          @click="login()"
          >ورود</v-btn
        >
        <h4 v-if="show_login_message" class="red--text mt-6 text-center">
          {{ login_message }}
        </h4>
      </v-col>
    </v-row>
  </div>
</template>


<script>
// import { mapGetters } from 'vuex';

export default {
  name: 'LoginPage',
  middleware: 'auth',
  data() {
    return {
      username: null,
      password: null,
      show: false,
      url: process.env.myurl,
      user_name: null,
      pass_word: null,
      login_state: false,
      login_message: null,
      show_login_message: false,
    }
  },

  // computed: {
  //   ...mapGetters('getloginstate'),
  // },

  methods: {
    login() {
      console.log(this.url)
      const url = this.url + '/login'
      const headers = {
        accept: 'application/json',
        'Content-Type': 'application/json',
      }
      const body = {
        username: this.user_name,
        password: this.pass_word,
      }

      this.$axios
        .post(url, body, { headers })
        .then((response) => response.data)
        .then((data) => {
          this.login_state = data.login
          this.login_message = data.message
          if (this.login_state) {
            console.log(this.$store.state.login)
            this.show_login_message = false
            this.$store.commit('enter')
            this.$router.push('/prediction')
            console.log(this.$store.state.login)
          } else {
            this.show_login_message = true
          }
        })
        .catch((error) => console.log('error', error))
    },
  },
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');

* {
  font-family: 'Vazir';
}

.username,
.password {
  font-family: 'Rubik', sans-serif !important;
  font-size: 1.2em;
}
</style>