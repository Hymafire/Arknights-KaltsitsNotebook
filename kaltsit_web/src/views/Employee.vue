<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="220px" class="home-aside" >
      <el-input prefix-icon="el-icon-user" placeholder="输入干员名称" v-model="filterText" class="search-input">
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
      <el-tree :props="props" :load="loadNode" lazy highlight-current> </el-tree>
    </el-aside>
    <!--  主体  -->
    <el-main>
      <!-- 卡片区 -->
      <el-card class="box-card">
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="employeeList">
              <el-table-column label="最大生命" prop="maxHp"></el-table-column>
              <el-table-column label="攻击" prop="atk"></el-table-column>
              <el-table-column label="防御" prop="def"></el-table-column>
              <el-table-column label="法抗" prop="magres"></el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="employeeList">
              <el-table-column label="部署费用" prop="maxHp"></el-table-column>
              <el-table-column label="攻击" prop="atk"></el-table-column>
              <el-table-column label="防御" prop="def"></el-table-column>
              <el-table-column label="法抗" prop="magres"></el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <!-- 分页 -->
      </el-card>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      props: {
        label: 'name',
        children: 'zones'
      },
      count: 1,
      employeeList: [],
      total: 0
    }
  },
  // 创建时调用
  created () {
    this.getEmployeeList()
  },
  methods: {
    // 获取干员列表
    getEmployeeList () {
      const employeeList = require('../static/employee_table_sim.json')
      this.employeeList = employeeList.char_285_medic2
    },
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
.el-aside {
  background-color: #fff;
  margin: 10px;
}
.el-main {
  background-color: #eaedf1;
}
// 输入栏style
.search-input {
  margin: 5px 0px;
}
// 卡片style
.text {
  font-size: 14px;
}
.item {
  padding: 18px 0;
}
// 卡片style
.box-card {
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15) !important;
}
</style>
