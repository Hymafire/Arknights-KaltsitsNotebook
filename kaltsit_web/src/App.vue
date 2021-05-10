<template>
  <div id="app">
    <el-container>
      <el-header>
        <NavBar />
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script>
import NavBar from './components/Common/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style lang="scss" scoped>
.el-container {
  // 用于固定 navbar
  height: 100%;
}
.el-header {
  width: 100%;
  padding: 0px;
}
.el-main {
  height: 100%;
  padding: 0px;
  margin: 0px;
}
</style>
