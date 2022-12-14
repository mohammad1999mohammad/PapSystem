export const state = () => ({
  login: null,
  sx_location_stores: [],
  sm_location_stores: [],
  center: { lat: 35.85344, lng: 51.462669 },
})

// contains your actions
//   export const actions = {
//     entering({ state, commit }){
//       commit('enter', state.counter + 1)
//     }
//   }
// contains your mutations
export const mutations = {
  enter(state) {
    localStorage.setItem('login', 'Yes')
    state.login = 'Yes'
  },
  exit(state) {
    localStorage.setItem('login', 'No')
    state.login = 'No'
    if (this.$router.fullPath !== '/login') {
      this.$router.push('/login')
    }
  },
  assign(state) {
    state.login = localStorage.getItem('login')
  },

  sx_getstores(state, arr) {
    state.sx_location_stores = arr
    console.log('done')
    console.log(arr)


  },

  sm_getstores(state, arr) {
    state.sm_location_stores = arr
    console.log('done')
    console.log(arr)


  },

  changecenter(state, cen) {
    state.center = cen
    console.log('cen', cen)
  }


}
  // your root getters
  // export const getters = {
  //     getlogin(state){ return state.login }
  // }