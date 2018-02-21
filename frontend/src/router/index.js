import Vue from 'vue'
import Router from 'vue-router'
import HousingSearch from '@/components/HousingSearch'

const routerOptions = [
  { path: '/',
    component: 'Home',
    children: [
      { path: 'housing', component: HousingSearch }
      // { path: 'job', component: 'Job' },
      // { path: 'event', component: 'Event' },
      // { path: 'sale', component: 'Sale' }
    ]
  },
  { path: '/housing/:id', component: 'HousingResult' },
  { path: '/post/housing', component: 'PostHousing' },
  { path: '/register', component: 'Register' },
  { path: '*', component: 'NotFound' }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
