<template>
  <el-container>
    <el-header class="search-header">
      <el-input prefix-icon="el-icon-user" placeholder="输入敌方名称" v-model="this.enemy_name" class="search-input">
        <el-button slot="append" icon="el-icon-search" />
      </el-input>
    </el-header>
    <el-main class="list-main">
      <el-tree :data="enemyList" :props="proplist" @node-click="handleNodeClick" highlight-current accordion/>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'Enaside',
  data () {
    return {
      proplist: {
        label: 'name',
        children: 'children'
      },
      enemyList: []
    }
  },
  mounted () {
    this.getEnemyList()
  },
  props: ['enemy_name'],
  methods: {
    getEnemyList () {
      const enemylist = require('@/assets/data/enemylist.json')
      this.enemyList = enemylist
    },
    handleNodeClick (data) {
      this.$emit('enemyChanged', data.name)
    }
  }
}
</script>

<style lang="scss" scoped>
.search-input {
  margin: 10px 0px;
}
.search-header {
  padding: 5px;
  height: 60px;
}
.list-main {
  padding: 5px;
}
</style>
