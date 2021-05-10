<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    router
  >
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
    <el-menu-item
      disabled
      index="/compare"
    >
      干员对比
    </el-menu-item>
    <el-menu-item index="/enemy">
      敌人分析
    </el-menu-item>
    <el-menu-item
      disabled
      index="/createm"
    >
      简历编辑
    </el-menu-item>
    <el-menu-item
      disabled
      index="/createn"
    >
      敌人登记
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: 'NavBar',
  data () {
    return {
      activeIndex: '/home'
    }
  }
}
</script>

<style lang="scss" scoped>
.el-menu {
  width: 100%;
  padding-left: 0px
}
.el-menu-item {
  font-size: 15px;
  font-weight: 700
}
span {
  font-size: 32px;
  font-weight: 500;
  color: #303133;
  text-shadow: 1px 1px .5px rgba(100, 100, 100, 0.1)
}
</style>
