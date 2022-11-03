<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" class="mt-8">
        <NuxtLink to="/prediction">
          <h2 class="text-center" >
            ورود به صفحه پیش بینی
          </h2>
        </NuxtLink>
      </v-col>
    </v-row>
  </div>
</template>


<script>
export default {
  name: 'IndexPage',
  middleware: 'auth',
  data() {
    return {}
  },

  methods: {},
}
</script>


<style scoped>
a:link {
  text-decoration: none;
}

a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: none;
}

a:active {
  text-decoration: none;
}
</style>