import Vue from 'vue'
import VueRouter from 'vue-router'
// 导入模块
import Home from '@/components/Home.vue'
import Enemy from '@/components/Enemy.vue'
import Employee from '@/components/Employee.vue'
import CreateEn from '@/components/Create/CreateEn.vue'
import CreateEm from '@/components/Create/CreateEm.vue'
import Compare from '@/components/EmCompare.vue'
import Welcome from '@/components/Welcome.vue'
import Login from '@/views/Login.vue'
import Learn from '@/views/learn.vue'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    { path: '/', redirect: 'Home' },
    { path: '/login', component: Login },
    { path: '/learn', component: Learn },
    {
      path: '/home',
      component: Home,
      redirect: '/welcome',
      children: [
        { path: '/welcome', component: Welcome },
        { path: '/enemy', component: Enemy },
        { path: '/employee', component: Employee },
        { path: '/createn', component: CreateEn },
        { path: '/createm', component: CreateEm },
        { path: '/compare', component: Compare }
      ]
    }
  ]
})
