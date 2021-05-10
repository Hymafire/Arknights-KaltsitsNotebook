<template>
  <el-container>
    <el-header class="search-header">
      <el-input prefix-icon="el-icon-user" placeholder="输入查询名称" v-model="objName" class="search-input">
        <el-button slot="append" icon="el-icon-search" @click="searchName" />
      </el-input>
    </el-header>
    <el-main class="list-main">
      <el-tree :data="listData" :props="proplist" @node-click="handleNodeClick" highlight-current accordion />
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'SearchList',
  data () {
    return {
      proplist: {
        label: 'name',
        children: 'children'
      },
      objName: ''
    }
  },
  props: {
    listData: Array
  },
  methods: {
    handleNodeClick (data) {
      this.$emit('objChanged', data.name)
    },
    searchName () {
      this.$emit('objChanged', this.objName)
    }
  }
}
</script>

<style lang="scss" scoped>
.search-input {
  margin: 10px 0px;
}
.search-header {
  height: 60px;
  padding: 5px;
}
.list-main {
  height: 100%;
  padding: 5px;
}
</style>
