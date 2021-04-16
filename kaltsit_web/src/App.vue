<template>
  <div id="App" class="app-div">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      router
    >
      <el-menu-item>
        <span>Kal'tsit's Notebook</span>
      </el-menu-item>
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
    <el-main>
      <!-- 路由占位 -->
      <router-view />
    </el-main>
  </div>
</template>

<script>
export default {
  name: 'App',
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
.app-div {
  position:fixed;
  top: 0px;
  height: 100%;
  width: 100%;
}
.el-menu {
  padding-left: 12px;
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
