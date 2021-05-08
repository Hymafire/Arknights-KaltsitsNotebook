<template>
  <el-container>
    <el-header class="search-header">
      <el-input prefix-icon="el-icon-user" placeholder="输入敌方名称" v-model="enemyName" class="search-input">
        <el-button slot="append" icon="el-icon-search" @click="findName"/>
      </el-input>
    </el-header>
    <el-main class="list-main">
      <el-tree :data="enemyList" :props="propslist" @node-click="handleNodeClick($event)" highlight-current accordion/>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      propslist: {
        label: 'name',
        children: 'children'
      },
      enemyList: [],
      enemyName: ''
    }
  },
  mounted () {
    this.getEnemyList()
  },
  methods: {
    getEnemyList () {
      this.enemyList = require('@/assets/data/enemylist.json')
    },
    handleNodeClick (data) {
      this.$emit('enemyChanged', data.name)
    },
    findName () {
      this.$emit('enemyChanged', this.enemyName)
    }
  }
}
</script>

<style lang="scss" scoped>
// 搜索框
.search-input {
  margin: 10px 0px;
}
// 搜索栏
.search-header {
  padding: 5px;
  height: 60px;
}
// 列表栏
.list-main {
  padding: 5px;
  height: 100%;
}
</style>
