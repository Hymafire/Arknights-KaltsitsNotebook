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
  </div>
</template>

<script>
import NavBar from './components/Common/NavBar.vue'
import NavDrawer from './components/Common/NavDrawer.vue'
import { emDataPretreate } from './components/utils/pretreatedCalc.js'

export default {
  name: 'App',
  components: {
    NavBar,
    NavDrawer
  },
  created () {
    this.initData()
  },
  methods: {
    initData () {
      const employeeData = require('./assets/data/employeedata.json')
      this.$store.commit('inputEmployeeData', employeeData)
      this.$store.commit('inputEmPretreatedData', emDataPretreate(employeeData))
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
}
.el-container {
  height: 100%;
}
</style>
