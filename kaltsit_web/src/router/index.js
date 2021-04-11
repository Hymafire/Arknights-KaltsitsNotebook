import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Enemy from '../views/Enemy.vue'
import Employee from '../views/Employee.vue'
import CreateEn from '../views/CreateEn.vue'
import CreateEm from '../views/CreateEm.vue'
import Compare from '../views/EmCompare.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    { path: '/', redirect: 'Home' },
    { path: '/home', component: Home },
    { path: '/login', component: Login },
    { path: '/enemy', component: Enemy },
    { path: '/employee', component: Employee },
    { path: '/createn', component: CreateEn },
    { path: '/createm', component: CreateEm },
    { path: '/compare', component: Compare }
  ]
})
