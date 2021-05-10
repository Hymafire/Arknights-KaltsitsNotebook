import Vue from 'vue'
import VueRouter from 'vue-router'

// 懒加载
const Enemy = () => import('../views/Enemy.vue')
const Employee = () => import('../views/Employee.vue')
const CreateEn = () => import('../components/Create/CreateEn.vue')
const CreateEm = () => import('../components/Create/CreateEm.vue')
const Compare = () => import('../views/EmCompare.vue')
const Home = () => import('../views/Home.vue')

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', component: Home },
  { path: '/enemy', component: Enemy },
  { path: '/employee', component: Employee },
  { path: '/createn', component: CreateEn },
  { path: '/createm', component: CreateEm },
  { path: '/compare', component: Compare }
]

export default new VueRouter({
  routes,
  // mode: 'history',
  linkActiveClass: 'active'
})
