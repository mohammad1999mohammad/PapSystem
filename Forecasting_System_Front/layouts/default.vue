<template>
  <v-app dark>
    <v-app-bar color="primary" dark fixed app>
      <v-app-bar-nav-icon
        v-if="$store.state.login === 'Yes'"
        @click="drawer = true"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>سامانه پاپ</v-toolbar-title>
      <v-spacer></v-spacer>
      <img
        src="../static/Haraz_dairy.png"
        height="60"
        width="60"
        class="mb-1"
      />
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" right app temporary>
      <v-list nav>
        <v-list-item-group
          v-model="group"
          active-class="indigo--text text--darken-4 lime accent-4"
        >
          <!-- <NuxtLink to="/"> -->
          <v-list-item to="/prediction">
            <v-list-item-icon>
              <v-icon>mdi-calendar-clock</v-icon>
            </v-list-item-icon>
            <v-list-item-title>پیش بینی</v-list-item-title>
          </v-list-item>
          <!-- </NuxtLink> -->
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>

    <v-footer class="mt-8">
      <span class="copy black--text"
        >&copy; کلیه حقوق این وب‌سایت متعلق به شرکت فرآورده‌های لبنی دوشه آمل
        (هراز) است.</span
      >
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
      drawer: false,
      group: null,
    }
  },
}
</script>
<style scoped>
.copy {
  font-size: 0.8em !important ;
}
* {
  font-family: 'Vazir' !important;
}
</style>