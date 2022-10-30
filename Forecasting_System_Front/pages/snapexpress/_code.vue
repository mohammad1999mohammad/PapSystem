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
          :items-per-page="1000"
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
  name: 'SnapexpressstorePage',
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
          text: 'نمره',
          align: 'center',
          sortable: false,
          value: 'product_rating',
        },
        {
          text: 'مقدار تخفیف',
          align: 'center',
          sortable: true,
          value: 'product_discount',
        },
        {
          text: 'درصد تخفیف',
          align: 'center',
          sortable: true,
          value: 'product_discount_rate',
        },
        {
          text: 'حجم',
          align: 'center',
          sortable: false,
          value: 'product_volume',
        },
        {
          text: 'قیمت',
          align: 'center',
          sortable: true,
          value: 'product_price',
        },
        // {
        //   text: 'تعداد کامنت',
        //   align: 'center',
        //   sortable: false,
        //   value: 'product_comment_count',
        // },
        {
          text: 'برند',
          align: 'center',
          sortable: true,
          value: 'product_brand',
        },
        {
          text: 'موجودی',
          align: 'center',
          sortable: true,
          value: 'product_stock',
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
        '/sxstoreproducts' +
        '?' +
        `storecode=${this.code}` +
        '&' +
        `latitude=${this.$store.state.center.lat}` +
        '&' +
        `longitude=${this.$store.state.center.lng}`

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