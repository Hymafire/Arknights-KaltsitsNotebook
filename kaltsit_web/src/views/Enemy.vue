<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="220px" class="home-aside" >
      <el-input prefix-icon="el-icon-user" />
      <el-tree :props="props" :load="loadNode" lazy show-checkbox> </el-tree>
    </el-aside>
    <!--  主体  -->
    <el-main>Main</el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      menulist: []
    }
  },
  created () {
    this.getMenuList()
  },
  methods: {
    async getMenu () {
      const { data: res } = await this.$http.get('menus')
      this.menulist = res.data
      console.log(res)
    }
  }
}
</script>

<style lang="scss" scoped>
.home-container {
  height: 100%;
}
.home-aside {
}
.el-aside {
  background-color: #fcfcff;
}
.el-main {
  background-color: #eaedf1;
}
</style>
