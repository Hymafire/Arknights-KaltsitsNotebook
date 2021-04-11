<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="220px" class="home-aside" >
      <el-input prefix-icon="el-icon-user" placeholder="输入干员名称" v-model="filterText"/>
      <el-tree :props="props" :load="loadNode" lazy> </el-tree>
    </el-aside>
    <!--  主体  -->
    <el-main>Main</el-main>
  </el-container>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      props: {
        label: 'name',
        children: 'zones'
      },
      count: 1
    }
  },
  methods: {
    loadNode (node, resolve) {
      if (node.level === 0) {
        return resolve([{ name: '★★★★★★' }, { name: '★★★★★' }, { name: '★★★★' }, { name: '★★★' }, { name: '★★' }, { name: '★' }])
      }
      if (node.level === 1) {
        return resolve([{ name: '近卫' }, { name: '医疗' }, { name: '狙击' }, { name: '特种' }, { name: '术师' }, { name: '重装' }, { name: '辅助' }, { name: '先锋' }])
      }
      if (node.level >= 3) {
        return resolve([])
      }
      if (node.level === 2) {
        return resolve([{ name: '测试干员' }])
      }
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
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  color: #fff;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}
.el-aside {
  background-color: #fcfcff;
}
.el-main {
  background-color: #eaedf1;
}
.toggle-button {
  font-size: 10px;
  line-height: 24px;
  color: #000;
  text-align: center
}
.reset-button {
  display: flex;
  justify-content: flex-end;
}
</style>
