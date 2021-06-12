import Vue from 'vue'
import Vuex from 'vuex'
import { emParamCalc } from '../components/utils/baseCalc.js'
import { emDataPretreate, emTablePretreate } from '../components/utils/pretreatedCalc.js'

Vue.use(Vuex)

// employee-store
const Employee = {
  namespaced: true,
  state: {
    emName: String,
    emKey: String,
    emData: Object,
    // 参数
    emParam: Object,
    emInputParam: Object,
    // 技能
    emSkillsData: Object,
    emSkillsLevel: Array,
    emSkillsFlag: Array,
    // 杂项
    emPretData: Object,
    isEmUpdated: false,
    // 数据(不动)
    employeeTable: Object,
    emPretreatedData: Object,
    emSkillsTable: Object
  },
  mutations: {
    // 改变目标干员
    changeEmployeeName (state, emName) {
      for (const em in state.employeeTable) {
        if (state.employeeTable[em].name === emName) {
          state.emName = emName
          state.emKey = state.employeeTable[em].Key
          break
        }
      }
      state.emData = Object.assign({}, state.emData, state.employeeTable[state.emKey])
      this.commit('em/updateEmSkillsData')
      state.emPretData = Object.assign({}, state.emPretData, emDataPretreate(state.emData, state.emSkillsData))
      this.commit('em/updateEmParam')
      this.commit('em/changeIsEmUpdate')
    },
    // 数据更新
    updateEmInputParam (state, inputParam) {
      state.emInputParam = Object.assign({}, state.emInputParam, inputParam)
      this.commit('em/updateEmParam')
      this.commit('em/changeIsEmUpdate')
    },
    updateEmParam (state) {
      state.emParam = Object.assign({}, state.emParam, emParamCalc(state.emData, state.emInputParam))
    },
    // 技能
    updateEmSkillsData (state) {
      const emSkillsList = state.emData.skills
      const emSkillsData = {}
      for (const i in emSkillsList) {
        emSkillsData[emSkillsList[i]] = state.emSkillsTable[emSkillsList[i]]
      }
      state.emSkillsData = emSkillsData
    },
    updateSkillsLevel (state, skillsLevel) {
      state.emSkillsLevel = Object.assign({}, state.emSkillsLevel, skillsLevel)
    },
    updateSkillsFlag (state, skillsFlag) {
      state.emSkillsFlag = Object.assign({}, state.emSkillsFlag, skillsFlag)
    },
    // 数据载入
    inputEmployeeData (state, employeeTable) {
      state.employeeTable = employeeTable
      state.emPretreatedData = emTablePretreate(state.employeeTable)
    },
    inputEmSkillsData (state, skillsTable) {
      state.emSkillsTable = skillsTable
    },
    //
    changeIsEmUpdate (state) {
      state.isEmUpdated = !state.isEmUpdated
    }
  }
}

// enemy-store
const Enemy = {
  namespaced: true,
  state: {
    enName: String,
    enKey: String,
    enData: Object,
    enLevel: Number,
    enemyTable: Object,
    enPretreateData: Object
  },
  mutations: {
    changeEnemyName (state, enName) {
      state.enName = enName
    }
  }
}

// compare
const EmCompare = {
  namespaced: true,
  state: {
    emNameList: [],
    emKeyList: [],
    emInputParam: Object,
    eachInputParam: Object
  },
  mutations: {
    addEmployee (state, emName) {
      for (const emKey in this.state.em.employeeTable) {
        if (this.state.em.employeeTable[emKey].name === emName) {
          const isIn = state.emNameList.indexOf(emName)
          if (isIn === -1) {
            Vue.set(state.emNameList, state.emNameList.length, emName)
            Vue.set(state.emKeyList, state.emKeyList.length, emKey)
          }
        }
      }
    },
    subEmployee (state, index) {
      Vue.delete(state.emNameList, index)
      Vue.delete(state.emKeyList, index)
    }
  }
}

// locales
const Locales = {
  namespaced: true,
  state: {
    localesId: 'cn',
    profList: Object,
    posList: Object
  },
  mutations: {
    initLocales (state, id) {
      state.localesId = id
      const profList = require('../assets/locales/prof_list.json')
      state.profList = Object.assign({}, state.profList, profList[state.localesId])
      const posList = require('../assets/locales/pos_list.json')
      state.posList = Object.assign({}, state.posList, posList[state.localesId])
    }
  }
}

// drawer and lists
const DrawerAndLists = {
  namespaced: true,
  state: {
    // 抽屉是否打开
    isDrawerOpen: false,
    // 列表是否折叠
    isListCollapse: false
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
    }
  }
}

export default new Vuex.Store({
  state: {
    version: 'v0.10.1'
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    em: Employee,
    en: Enemy,
    emc: EmCompare,
    loc: Locales,
    dal: DrawerAndLists
  }
})
