<template>
  <!-- 头部导航栏  -->
  <el-container class="home-container">
    <el-header>
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        router
      >
        <!-- 网站名称 不做跳转 -->
        <el-menu-item>
          <span>Kal'tsit's Notebook</span>
        </el-menu-item>
        <!-- 导航跳转 -->
        <el-menu-item index="/home">
          首页
        </el-menu-item>
        <el-menu-item index="/employee">
          干员分析
        </el-menu-item>
        <el-menu-item disabled index="/compare">
          干员对比
        </el-menu-item>
        <el-menu-item index="/enemy">
          敌人分析
        </el-menu-item>
        <el-menu-item disabled index="/createm">
          简历编辑
        </el-menu-item>
        <el-menu-item disabled index="/createn">
          敌人登记
        </el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <!-- 路由占位 -->
      <router-view />
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      activeIndex: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style lang="scss" scoped>
.home-container {
  height: 100%;
}
.el-header {
  padding: 0px;
  width: 100%;
}
.el-menu {
  width: 100%;
  padding-left: 0px;
  span {
    font-size: 30px;
  }
}
.el-main {
  padding: 0px;
  margin: 0px;
  height: 100%;
}
</style>
