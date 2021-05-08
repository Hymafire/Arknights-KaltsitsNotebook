<template>
  <el-container>
    <!-- 导航栏 -->
    <el-header>
      <NavBar />
    </el-header>
    <!-- 主体 -->
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<script>
import NavBar from '../components/Home/NavBar.vue'

export default {
  name: 'Home',
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
  padding: 0px;
  width: 100%;
}
.el-main {
  height: 100%;
  padding: 0px;
  margin: 0px;
}
</style>
