import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Enemy from '../views/Enemy.vue'
import Employee from '../views/Employee.vue'
import CreateEn from '../views/CreateEn.vue'
import CreateEm from '../views/CreateEm.vue'
import Compare from '../views/EmCompare.vue'
import Login from '../views/Login.vue'
import Test from '../views/Test.vue'
import Test2 from '../views/Test2.vue'

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
    { path: '/compare', component: Compare },
    { path: '/test', component: Test },
    { path: '/test2', component: Test2 }
  ]
})
