export const state = () => ({
    login: 'No'
  })
  
  // contains your actions
//   export const actions = {
//     entering({ state, commit }){
//       commit('enter', state.counter + 1)
//     }
//   }
  // contains your mutations
  export const mutations = {
    enter(state){
      state.login = "Yes"
    },
    exit(state){
        state.login = "No"
      },

  }
//   your root getters
//   export const getters = {
//       myGetter(state){ return state.counter + 1000}
//   }