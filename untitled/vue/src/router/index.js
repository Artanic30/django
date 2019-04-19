import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import register from '@/components/register'
import store from '../store'

Vue.use(Router)
const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '',
      name: 'login',
      component: index
    },
    {
      path: '/register',
      name: 'register',
      component: register,
      meta: { requiresAuth: true }
    }
  ]
})

router.beforeEach((to, from, next) => {
  const auth = store.state.isAuthorized
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!auth) {
      next({
        path: '/'
      })
    } else {
      next()
    }
  } else {
    next()
  }
})
export default router
