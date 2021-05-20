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

export default {
  name: 'App',
  data () {
    return {
      isOpen: false
    }
  },
  components: {
    NavBar,
    NavDrawer
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
