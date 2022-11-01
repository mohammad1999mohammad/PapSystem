<template>
  <v-row justify="center" align="center">
    <v-col cols="12" class="mt-4">
      <div>
        <v-data-table
          :headers="headers"
          :items="products"
          :item-key="Math.random().toString()"
          class="elevation-1"
          hide-default-footer
          :items-per-page="3000"
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
  name: 'DigikalaProducts',
  middleware: 'auth',
  data() {
    return {
      base_url: process.env.myurl,
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
          value: 'product_persian_title',
          width: "400px"
        },
        {
          text: 'نمره',
          align: 'center',
          sortable: true,
          value: 'product_star_rate',
        },
        {
          text: 'تعداد آرا نمره',
          align: 'center',
          sortable: true,
          value: 'product_star_number_of_scorer',
          width: "100px"
        },
        {
          text: 'وضعیت موجودی',
          align: 'center',
          sortable: true,
          value: 'product_status',
          width: "150px"
        },
        {
          text: 'برند',
          align: 'center',
          sortable: true,
          value: 'product_brand',
          width: "150px"
        },
        {
          text: 'پیشنهاد فروش',
          align: 'center',
          sortable: true,
          value: 'product_offer',
          width: "150px"
        },
        {
          text: 'کمترین قیمت در ماه گذشته',
          align: 'center',
          sortable: true,
          value: 'product_min_price_last_month',
          width: "200px"
        },
        {
          text: 'نرخ رضایت',
          align: 'center',
          sortable: true,
          value: 'product_satisfy_rate',
          width: "100px"
        },
        {
          text: 'تعداد آرا رضایت',
          align: 'center',
          sortable: true,
          value: 'product_satisfy_number_of_scorer',
          width: "150px"
        },
        {
          text: 'هدیه دیجی پلاس',
          align: 'center',
          sortable: true,
          value: 'product_digiplus_cashback',
          width: "150px"
        },
        {
          text: 'امتیاز دیجی کلاب',
          align: 'center',
          sortable: true,
          value: 'product_digiclub_point',
          width: "150px"
        },
        {
          text: 'قیمت فروش',
          align: 'center',
          sortable: true,
          value: 'product_selling_price',
          width: "150px"
        },
        {
          text: 'درصد تخفیف',
          align: 'center',
          sortable: true,
          value: 'product_discount_percent',
          width: "150px"
        },
        {
          text: 'قیمت اصلی',
          align: 'center',
          sortable: true,
          value: 'product_rrp_price',
          width: "150px"
        },
        {
          text: 'حداکثر سفارش',
          align: 'center',
          sortable: true,
          value: 'product_order_limit',
          width: "150px"
        },
        {
          text: 'گروه محصول',
          align: 'center',
          sortable: true,
          filterable:true,
          value: 'product_group',
          width: "150px"
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
      const url = this.base_url + '/dkproducts'

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

.v-data-table { 
  overflow-x: auto !important;
}
</style>