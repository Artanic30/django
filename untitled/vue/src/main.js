// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import '../theme/index.css'
import ElementUI from 'element-ui'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'
import cookies from 'vue-cookie'
import store from './store'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(Vuex)
Vue.use(cookies)
Vue.use(VueAxios, axios)
axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  if (error.response.status === 403) {
    store.commit('logout')
    setTimeout(() => {
      window.location.reload()
    }, 2000)
  }
  return Promise.reject(error)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  cookies,
  components: { App },
  template: '<App/>'
})
