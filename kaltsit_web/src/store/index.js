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
    employeeKey: 'char_263_skadi',
    // 目标干员信息是否更新
    isEmParamsUpdate: true,
    // 数据
    employeeData: Object,
    emPretreatedData: Object
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
      for (const em in state.employeeData) {
        if (state.employeeData[em].name === employeeName) {
          state.employeeKey = state.employeeData[em].Key
          break
        }
      }
    },
    // 目标干员信息是否更新
    changeIsEmParamsUpdate (state) {
      state.isEmParamsUpdate = !state.isEmParamsUpdate
    },
    // 数据载入
    inputEmployeeData (state, employeeData) {
      state.employeeData = employeeData
    },
    inputEmPretreatedData (state, emPretreateData) {
      state.emPretreatedData = emPretreateData
    }
  },
  actions: {
  },
  modules: {
  }
})
