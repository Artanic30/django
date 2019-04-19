import VuexPersistence from 'vuex-persist'
import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

const store = new Vuex.Store({
  state: {
    isAuthorized: false
  },
  mutations: {
    login (state) {
      state.isAuthorized = true
    },
    logout (state) {
      state.isAuthorized = false
    }
  },
  plugins: [vuexLocal.plugin]
})

export default store
