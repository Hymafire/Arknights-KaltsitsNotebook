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
      state.emData = Object.assign({}, state.employeeTable[state.emKey])
      this.commit('em/updateEmSkillsData')
      state.emPretData = Object.assign({}, emDataPretreate(state.emData, state.emSkillsData))
      this.commit('em/updateEmParam')
      this.commit('em/changeIsEmUpdate')
    },
    // 数据更新
    updateEmInputParam (state, inputParam) {
      state.emInputParam = Object.assign({}, inputParam)
      this.commit('em/updateEmParam')
      this.commit('em/changeIsEmUpdate')
    },
    updateEmParam (state) {
      state.emParam = Object.assign({}, emParamCalc(state.emData, state.emInputParam))
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
      state.emSkillsLevel = Object.assign({}, skillsLevel)
    },
    updateSkillsFlag (state, skillsFlag) {
      state.emSkillsFlag = Object.assign({}, skillsFlag)
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
    enLevel: 0,
    enemyTable: Object,
    enemyList: null,
    enPretreateData: Object
  },
  mutations: {
    changeEnemyName (state, enName) {
      for (const en in state.enemyTable) {
        if (state.enemyTable[en].name === enName) {
          state.enKey = en
          state.enName = enName
          state.enData = Object.assign({}, state.enemyTable[en])
          break
        }
      }
    },
    inputEnemyData (state, enemyTable) {
      state.enemyTable = enemyTable
    },
    updateEnLevel (state, enLevel) {
      state.enLevel = enLevel
    },
    setEnemyList (state, enemyList) {
      state.enemyList = enemyList
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
      if (!this.state.cp.isCompareNumLimit || state.emNameList.length < 5) {
        if (state.emNameList.indexOf(emName) === -1) {
          for (const emKey in this.state.em.employeeTable) {
            if (this.state.em.employeeTable[emKey].name === emName) {
              Vue.set(state.emNameList, state.emNameList.length, emName)
              Vue.set(state.emKeyList, state.emKeyList.length, emKey)
            }
          }
        }
      }
    },
    subEmployee (state, index) {
      Vue.delete(state.emNameList, index)
      Vue.delete(state.emKeyList, index)
    },
    limitEmployeeList (state) {
      while (state.emNameList.length > 5) {
        Vue.delete(state.emNameList, 5)
        Vue.delete(state.emKeyList, 5)
      }
    }
  }
}

// locales
const Locales = {
  namespaced: true,
  state: {
    localeId: 'cn',
    profList: Object,
    posList: Object
  },
  mutations: {
    initLocales (state, id) {
      state.localesId = id
      const profList = require('../assets/locales/prof_list.json')
      state.profList = Object.assign({}, profList[state.localesId])
      const posList = require('../assets/locales/pos_list.json')
      state.posList = Object.assign({}, posList[state.localesId])
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

// control panel
const ControlPanel = {
  namespaced: true,
  state: {
    isControlPanelOpen: false,
    isEnemyAnalysis: false,
    isCollapseAccordion: true,
    isDevFuncApply: false,
    isCompareNumLimit: true
  },
  mutations: {
    openControlPanel (state) {
      state.isControlPanelOpen = true
    },
    closeControlPanel (state) {
      state.isControlPanelOpen = false
    },
    changeIsEnemyAnalysis (state, bool) {
      state.isEnemyAnalysis = bool
    },
    changeIsCollapseAccordion (state, bool) {
      state.isCollapseAccordion = bool
    },
    changeIsDevFuncApply (state, bool) {
      state.isDevFuncApply = bool
    },
    changeIsCompareNumLimit (state, bool) {
      state.isCompareNumLimit = bool
    }
  }
}

// collapse
const CollapseItem = {
  namespaced: true,
  state: {
    activeNameList: ['null', 'null', 'null', 'null', 'null']
  },
  mutations: {
    changeActiveName (state, changeData) {
      Vue.set(state.activeNameList, changeData.index, changeData.activeName)
    }
  }
}

export default new Vuex.Store({
  state: {
    version: 'v0.10.2'
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
    dal: DrawerAndLists,
    cp: ControlPanel,
    ci: CollapseItem
  }
})
