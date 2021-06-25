<template>
  <div id="app">
    <el-container>
      <el-header class="base-style header-height">
        <NavBar />
      </el-header>
      <el-main class="base-style">
        <router-view />
      </el-main>
    </el-container>
    <NavDrawer />
    <ControlPanel />
  </div>
</template>

<script>
import NavBar from './components/Common/NavBar.vue'
import NavDrawer from './components/Common/NavDrawer.vue'
import ControlPanel from './components/Common/ControlPanel.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    NavDrawer,
    ControlPanel
  },
  created () {
    this.initEmployeeData()
    this.initEnemyData()
    this.initLocales()
  },
  methods: {
    initEmployeeData () {
      const employeeData = require('./assets/data/employeedata.json')
      this.$store.commit('em/inputEmployeeData', employeeData)
      const skillsData = require('./assets/data/skill_table.json')
      this.$store.commit('em/inputEmSkillsData', skillsData)
    },
    initEnemyData () {
      const enemyData = require('./assets/data/enemydata.json')
      this.$store.commit('en/inputEnemyData', enemyData)
    },
    initLocales () {
      const localesId = 'cn'
      this.$store.commit('loc/initLocales', localesId)
    }
  }
}
</script>

<style lang="scss" scoped>
@media only screen and (max-width:767px) {
  .header-height {
    height: 42px !important;
  }
}
@media only screen and (min-width:768px) {
  .header-height {
    height: 48px !important;
  }
}
.base-style {
  padding: 0px;
  margin: 0px;
  height: 100%;
}
.el-container {
  height: 100%;
}
</style>
