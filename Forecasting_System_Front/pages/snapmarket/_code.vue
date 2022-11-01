<template>
  <v-row justify="center" align="center">
    <v-col cols="12" class="mt-4">
      <div>
        <v-data-table
          :headers="headers"
          :items="products"
          item-key="product_id"
          class="elevation-1"
          hide-default-footer
          :items-per-page="2000"
          :loading="loading"
          :multi-sort="true"
          loading-text="در حال دریافت اطلاعات"
          no-data-text="اطلاعاتی یافت نشد"
          no-results-text="نتیجه یافت نشد"
        >
        </v-data-table>
      </div>
    </v-col>
  </v-row>
</template>


<script>
export default {
  name: 'SnapmarketstorePage',
  middleware: 'auth',
  data() {
    return {
      base_url: process.env.myurl,
      code: this.$route.params.code,
      products: [],
      loading: false,
    }
  },

  computed: {
    headers() {
      return [
        // {
        //   text: 'کد',
        //   align: 'center',
        //   sortable: false,
        //   value: 'product_id',
        // },
        {
          text: 'نام',
          align: 'center',
          sortable: false,
          value: 'product_name',
        },
        {
          text: 'ماکسیمم سفارش',
          align: 'center',
          sortable: true,
          value: 'product_max_order',
        },
        {
          text: 'قیمت فروش',
          align: 'center',
          sortable: true,
          value: 'product_selling_price',
        },
        {
          text: 'قیمت اصلی',
          align: 'center',
          sortable: true,
          value: 'product_main_price',
        },
        {
          text: 'درصد تخفیف',
          align: 'center',
          sortable: true,
          value: 'product_discount_percent',
        },
        {
          text: 'برند',
          align: 'center',
          sortable: true,
          value: 'product_brand_name',
        },
        {
          text: 'گروه',
          align: 'center',
          sortable: true,
          value: 'product_category',
        },
        
      ]
    },
  },

  created() {
    this.fetchproducts()
  },

  mounted() {},

  methods: {
    fetchproducts() {
      this.loading = true
      console.log('start')
      const url =
        this.base_url +
        '/smstoreproducts' +
        '?' +
        `storecode=${this.code}` 
        // '&' +
        // `latitude=${this.$store.state.center.lat}` +
        // '&' +
        // `longitude=${this.$store.state.center.lng}`

      this.$axios
        .get(url)
        .then((response) => {
          console.log('success')
          this.products = response.data.products
          this.loading = false
        })
        .catch((error) => {
          console.log('error', error)
        })

      console.log('lat ', this.$store.state.center.lat)
      console.log('lon ', this.$store.state.center.lng)
    },
  },
}
</script>


<style scoped>
/* * {
  font-family: 'Vazir' !important;
}

tbody tr:hover {
  background-color: transparent !important;
}

.table {
  box-shadow: 0 0 10px rgba(22, 0, 82, 0.856);
  border-radius: 10;
}

th {
  color: white !important;
  text-align: center !important;
  background-color: #1a237e;
}

td {
  color: #000000;
  text-align: center !important;
  background-color: #f5f5f5;
} */
</style>