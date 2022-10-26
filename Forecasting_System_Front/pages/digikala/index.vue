<template>
  <div>
    <v-row justify="center" align="center">
      <v-col cols="12" class="mt-8">
        <h4>تست</h4>
      </v-col>
    </v-row>
  </div>
</template>


<script>
export default {
  name: 'DigikalaPage',
//   middleware: 'auth',
  data() {
    return {}
  },
  methods: {},
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