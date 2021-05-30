import Vue from 'vue'
import VueRouter from 'vue-router'

// 懒加载
const Enemy = () => import('../views/Enemy.vue')
const Employee = () => import('../views/Employee.vue')
const CreateEn = () => import('../components/Create/CreateEn.vue')
const CreateEm = () => import('../components/Create/CreateEm.vue')
const Compare = () => import('../views/EmCompare.vue')
const Home = () => import('../views/Home.vue')
const Test = () => import('../views/TestTable.vue')

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/home' },
  { path: '/home', name: '首页', component: Home },
  { path: '/enemy', name: '敌人分析', component: Enemy },
  { path: '/employee', name: '干员分析', component: Employee },
  { path: '/createn', name: '敌人等级', component: CreateEn },
  { path: '/createm', name: '简历编辑', component: CreateEm },
  { path: '/compare', name: '干员比较', component: Compare },
  { path: '/test', name: 'Test', component: Test }
]

export default new VueRouter({
  routes,
  // mode: 'history',
  linkActiveClass: 'active'
})
