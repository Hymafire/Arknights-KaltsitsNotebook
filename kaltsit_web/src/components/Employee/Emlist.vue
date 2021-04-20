<template>
  <el-container>
    <el-header class="search-header">
      <el-input prefix-icon="el-icon-user" placeholder="输入干员名称" v-model="this.employee_name" class="search-input">
        <el-button slot="append" icon="el-icon-search" />
      </el-input>
    </el-header>
    <el-main class="list-main">
      <el-tree :data="employeeList" :props="proplist" @node-click="handleNodeClick" highlight-current accordion/>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'Emaside',
  data () {
    return {
      proplist: {
        label: 'name',
        children: 'children'
      },
      employeeList: []
    }
  },
  mounted () {
    this.getemployeeList()
  },
  props: ['employee_name'],
  methods: {
    getemployeeList () {
      const employeeList = require('@/assets/data/employeelist.json')
      this.employeeList = employeeList
    },
    handleNodeClick (data) {
      this.$emit('employeeChanged', data.name)
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
