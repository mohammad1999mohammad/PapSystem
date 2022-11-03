<template>
  <v-row justify="center" align="center">
    <v-col cols="12" lg="10" class="mt-4">
      <h4 class="text-center mb-8">لطفا موقعیت مکانی مورد نظر خود را انتخاب کنید</h4>
      <div style="height: 70vh">
        <l-map
          id="map"
          style="height: 100%; width: 100%"
          :zoom="zoom"
          :center="$store.state.center"
          @update:zoom="zoomUpdated"
          @update:center="centerUpdated"
        >
          <l-tile-layer :url="url"></l-tile-layer>
          <l-marker :lat-lng="$store.state.center"></l-marker>
        </l-map>
      </div>
      <v-btn
        block
        x-large
        color="primary"
        class="mt-6 font-weight-black"
        @click="fetchstores()"
      >مشاهده فروشگاه های منطقه</v-btn>
      <v-row>
        <v-col
          v-for="store in $store.state.sx_location_stores"
          :key="store.store_id"
          cols="12"
          lg="4"
        >
          <v-card
            id="card"
            :nuxt="true"
            :to="$route.path + '/' + store.store_code"
            rounded
            hover
            height="600"
            class="mx-auto mt-6"
          >
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >نام فروشگاه : {{ store.store_name }}</v-card-subtitle>
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >نوع فروشگاه : {{ store.store_type }}</v-card-subtitle>
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >منطقه فروشگاه : {{ store.store_area }}</v-card-subtitle>
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >تلفن فروشگاه : {{ store.store_phone }}</v-card-subtitle>
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >امتیاز فروشگاه : {{ store.store_rate_five }}</v-card-subtitle>
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >تعداد کامنت های فروشگاه : {{ store.store_comment_count }}</v-card-subtitle>
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >تعداد رای به فروشگاه : {{ store.store_vote_count }}</v-card-subtitle>
            <v-card-subtitle
              class="primary--text font-weight-bold"
            >هزینه ارسال فروشگاه : {{ store.store_delivery_fee }} تومان</v-card-subtitle>
            <v-card-subtitle class="primary--text font-weight-bold">
              حداقل مقدار خرید فروشگاه :
              {{ store.store_min_price_order }} تومان
            </v-card-subtitle>
            <v-card-subtitle class="primary--text font-weight-bold">
              وضعیت باز بودن فروشگاه :
              {{ store.store_open ? 'باز' : 'بسته' }}
            </v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>


<script>
export default {
  name: 'SnapexpressPage',
  middleware: 'auth',
  data() {
    return {
      base_url: process.env.myurl,
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      zoom: 6,
      number: 350,
    }
  },

  computed: {
    dynamicSize() {
      return [this.iconSize, this.iconSize * 1.15]
    },
    dynamicAnchor() {
      return [this.iconSize / 2, this.iconSize * 1.15]
    },
    target() {
      const value = this.number
      if (!isNaN(value)) return Number(value)
      else return value
    }
  },

  mounted() {},

  methods: {
    zoomUpdated(zoom) {
      this.zoom = zoom
    },
    centerUpdated(center) {
      this.$store.commit('changecenter', center)
      // console.log(this.center)
    },
    fetchstores() {
      const url =
        this.base_url +
        '/sxlocationstores' +
        '?' +
        `latitude=${this.$store.state.center.lat}` +
        '&' +
        `longitude=${this.$store.state.center.lng}`

      this.$axios
        .get(url)
        .then(response => {
          console.log('success')
          // this.location_stores = response.data.location_stores
          this.$store.commit('sx_getstores', response.data.location_stores)
          this.$vuetify.goTo(this.target)
        })
        .catch(error => {
          console.log(error)
        })

      console.log('lat ', this.$store.state.center.lat)
      console.log('lon ', this.$store.state.center.lng)
    }
  }
}
</script>


<style scoped>
#map {
  z-index: 0 !important;
  border: 1px solid black;
  margin-left: auto;
  margin-right: auto;
}

#card {
  border: 1px solid #aeea00;
}
</style>