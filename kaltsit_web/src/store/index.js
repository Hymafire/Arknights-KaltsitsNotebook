import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // 抽屉是否打开
    isDrawerOpen: false,
    // 列表是否折叠
    isListCollapse: false,
    // 目标敌人
    enemyName: '源石虫',
    // 目标干员信息
    employeeName: '斯卡蒂',
    // 目标干员信息是否更新
    isEmParamsUpdate: true
  },
  mutations: {
    // 抽屉开关
    openDrawer (state) {
      state.isDrawerOpen = true
    },
    closeDrawer (state) {
      state.isDrawerOpen = false
    },
    // 列表开关
    changeCollapse (state) {
      state.isListCollapse = !state.isListCollapse
    },
    initCollapse (state) {
      if (window.innerWidth < 768) {
        state.isListCollapse = true
      } else {
        state.isListCollapse = false
      }
    },
    // 目标名改变
    changeEnemyName (state, enemyName) {
      state.enemyName = enemyName
    },
    changeEmployeeName (state, employeeName) {
      state.employeeName = employeeName
    },
    // 目标干员信息是否更新
    changeIsEmParamsUpdate (state) {
      state.isEmParamsUpdate = !state.isEmParamsUpdate
    }
  },
  actions: {
  },
  modules: {
  }
})
