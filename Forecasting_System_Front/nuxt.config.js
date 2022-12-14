import colors from 'vuetify/es5/util/colors'

export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  router: {
    // ran before every route on both client and server
    middleware: ['direction']
  },

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  loading: {
    color: 'primary',
    height: '5px',
    rtl: true,
  },

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s ',
    title: 'سامانه پاپ',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', href: '/Haraz_dairy.ico' }],
  },



  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/assets/css/main.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
    // https://ngrok.nuxtjs.org/
    // '@nuxtjs/ngrok',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    // https://go.nuxtjs.dev/content
    '@nuxt/content',
    // https://www.npmjs.com/package/nuxt-leaflet
    'nuxt-leaflet',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/',
  },

  // router: {
  //   base: '/',

  // },

  env: {
    myurl: process.env.BASE_URL
  },


  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    icon:{
      fileName:'icon.png',
      sizes:[64, 120, 144, 152, 192, 384, 512],
    },
    meta: {
      title: 'Pap',
      author: 'MohammadHosein',
      theme_color:'#AEEA00',
    },
    manifest: {
      name: 'پلتفرم ارائه پروژه',
      short_name: 'پاپ هراز',
      description: 'پلتفرم ارائه پروژه',
      lang: 'en',   
      start_url:'/login',
      orientation:'portrait',  // landscape
      background_color:'#AEEA00',
      theme_color:'#AEEA00',
      display: 'standalone',
    },
  },

  // Content module configuration: https://go.nuxtjs.dev/config-content
  content: {},

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    rtl: true,
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
        light: {
          primary: colors.indigo.darken4,
          secondary: colors.lime.accent4,
          accent: colors.grey.lighten3,
          info: colors.teal.darken1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend(config, ctx) {

    }
  },

  server: {
    host: "0.0.0.0"
  }

}
