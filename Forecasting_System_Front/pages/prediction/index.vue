<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" class="mt-8">
        <v-autocomplete
          id="product"
          v-model="product_name"
          deletable-chips
          chips
          :items="products_list"
          item-text="persian_name"
          item-value="english_name"
          label="نام محصول"
          solo
          full-width
          background-color="grey lighten-4"
          @change="abc()"
        ></v-autocomplete>
        <v-select
          v-model="area"
          :items="areas_list"
          item-text="persian_name"
          item-value="id"
          label="نام منطقه"
          solo
          full-width
          background-color="grey lighten-4"
          @change="abc()"
        ></v-select>
        <v-text-field
          v-model="promotion"
          label="درصد تخفیف"
          solo
          clearable
          full-width
          background-color="grey lighten-4"
          @change="abc()"
        ></v-text-field>
        <v-select
          v-model="month"
          :items="months_list"
          item-text="persian_name"
          item-value="id"
          label="ماه"
          solo
          full-width
          background-color="grey lighten-4"
          @change="abc()"
        ></v-select>
        <v-select
          v-model="week"
          :items="weeks_list"
          item-text="persian_name"
          item-value="id"
          label="هفته"
          solo
          full-width
          background-color="grey lighten-4"
          @change="abc()"
        ></v-select>
        <v-select
          v-model="day"
          :items="days_list"
          item-text="persian_name"
          item-value="id"
          label="روز"
          solo
          full-width
          background-color="grey lighten-4"
          @change="abc()"
        ></v-select>
        <v-btn
          block
          color="primary"
          class="mt-2 font-weight-black"
          elevation="2"
          x-large
          @click="send_inputs()"
          >ارسال اطلاعات</v-btn
        >
        <v-btn
          block
          color="secondary"
          class="mt-8 font-weight-black black--text"
          elevation="2"
          x-large
          @click="receive_result()"
          >دریافت نتایج</v-btn
        >
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12">
        <h4
          v-if="results_list.length > 0"
          class="mt-8"
          align="center"
          justify="center"
        >
          نتایج پیش بینی به شرح زیر میباشد
        </h4>
        <v-simple-table
          v-for="result in results_list"
          :key="result.center"
          class="mt-8 table"
        >
          <template #default>
            <thead>
              <tr>
                <th>مرکز فروش</th>
                <th>حدود عملکرد</th>
                <th>تعداد فروش الگوریتم اول</th>
                <th>تعداد فروش الگوریتم دوم</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="0">{{ result.center }}</td>
                <td>حد بالا</td>
                <td>{{ result.linear.up }}</td>
                <td>{{ result.xgboost.up }}</td>
              </tr>
              <tr>
                <td>حد متوسط</td>
                <td>{{ result.linear.mid }}</td>
                <td>{{ result.xgboost.mid }}</td>
              </tr>
              <tr>
                <td>حد پایین</td>
                <td>{{ result.linear.low }}</td>
                <td>{{ result.xgboost.low }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-col>
    </v-row>
  </div>
</template>


<script>
export default {
  name: 'PredictionPage',
  middleware: 'auth',
  data() {
    return {
      product_name: null,
      product_persian_name: null,
      area: null,
      promotion: null,
      month: null,
      week: null,
      day: null,
      url: process.env.myurl,
      products_list: [
        {
          persian_name: 'ماست سبوی 1800 پر چرب',
          english_name: 'mast-saboo-por-1800',
          id: 1,
        },
        {
          persian_name: 'ماست سبوی 1800 کم چرب',
          english_name: 'mast-saboo-kam-1800',
          id: 2,
        },
      ],
      areas_list: [
        { persian_name: 'شمال غرب', english_name: 'shomal-gharb', id: 0 },
        { persian_name: 'شمال مرکز', english_name: 'shomal-markaz', id: 1 },
        { persian_name: 'جنوب', english_name: 'jonoob', id: 2 },
        { persian_name: 'غرب', english_name: 'gharb', id: 3 },
        { persian_name: 'مرکز', english_name: 'markaz', id: 4 },
        { persian_name: 'شرق', english_name: 'shargh', id: 5 },
      ],
      months_list: [
        { persian_name: 'فروردین', english_name: 'farvardin', id: 1 },
        { persian_name: 'اردیبهشت', english_name: 'ordibehesht', id: 2 },
        { persian_name: 'خرداد', english_name: 'khordad', id: 3 },
        { persian_name: 'تیر', english_name: 'tir', id: 4 },
        { persian_name: 'مرداد', english_name: 'mordad', id: 5 },
        { persian_name: 'شهریور', english_name: 'shahrivar', id: 6 },
        { persian_name: 'مهر', english_name: 'mehr', id: 7 },
        { persian_name: 'آبان', english_name: 'aban', id: 8 },
        { persian_name: 'آذر', english_name: 'azar', id: 9 },
        { persian_name: 'دی', english_name: 'dey', id: 10 },
        { persian_name: 'بهمن', english_name: 'bahman', id: 11 },
        { persian_name: 'اسفند', english_name: 'esfand', id: 12 },
      ],
      weeks_list: [
        { persian_name: 'هفته اول ماه', english_name: 'first-week', id: 1 },
        { persian_name: 'هفته دوم ماه', english_name: 'second-week', id: 2 },
        { persian_name: 'هفته سوم ماه', english_name: 'third-week', id: 3 },
        { persian_name: 'هفته چهارم ماه', english_name: 'fourth-week', id: 4 },
      ],
      days_list: [
        { persian_name: 'شنبه', english_name: 'saturday', id: 1 },
        { persian_name: 'یکشنبه', english_name: 'sunday', id: 2 },
        { persian_name: 'دوشنبه', english_name: 'monday', id: 3 },
        { persian_name: 'سه شنبه', english_name: 'tuesday', id: 4 },
        { persian_name: 'چهارشنبه', english_name: 'wednesday', id: 5 },
        { persian_name: 'پنجشنبه', english_name: 'thursday', id: 6 },
        { persian_name: 'جمعه', english_name: 'friday', id: 7 },
      ],
      results_list: [],
    }
  },
  methods: {
    abc() {
      // eslint-disable-next-line no-console
      console.log(
        this.product_name,
        this.area,
        parseFloat(this.promotion) / 100,
        this.month,
        this.week,
        this.day
      )
    },
    send_inputs() {
      const url = this.url + '/add-item'
      const headers = {
        accept: 'application/json',
        'Content-Type': 'application/json',
      }
      const body = {
        product: this.product_name,
        area: parseInt(this.area),
        promotion: parseFloat(this.promotion) / 100, // parsing is important just for promotion
        month: parseInt(this.month),
        week: parseInt(this.week),
        day: parseInt(this.day),
      }

      this.$axios
        .post(url, body, { headers })
        .then((response) => response.data)
        .then((data) => {
          console.log(data)
        })
        .catch(console.log('error'))
    },
    receive_result() {
      const url = this.url + '/get-result'
      this.$axios
        .get(url)
        .then((response) => {
          console.log('success')
          this.results_list = response.data.forecast
        })
        .catch(console.log('error'))
    },
  },
}
</script>


<style scoped>
* {
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
}
</style>