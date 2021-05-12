<template>
  <div id="app">
    <el-container>
      <el-header height="52px" class="base-style">
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
.base-style {
  padding: 0px;
  margin: 0px;
}
.el-container {
  height: 100%;
}
</style>
