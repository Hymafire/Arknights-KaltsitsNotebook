<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="220px" class="home-aside" >
      <el-input prefix-icon="el-icon-user" placeholder="输入干员名称" v-model="filterText" class="search-input">
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
      <el-tree :data="employeeList" :props="props" accordion @node-click="handleNodeClick" highlight-current> </el-tree>
    </el-aside>
    <!--  主体  -->
    <el-main>
      <!-- 卡片区 -->
      <el-card class="box-card">
        <!-- 页头 -->
        <div slot="header" class="clearfix">
          <el-row :gutter="20" type="flex">
            <el-col :span="4">
              <span class="head-name">{{ employeeList.name }}</span>
            </el-col>
            <el-col :span="20" class="head-description">
              <span class="head-title">特性：</span>
              <span>{{ employeeList.description }}</span>
            </el-col>
          </el-row>
        </div>
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="employeeList">
              <el-table-column label="属性"></el-table-column>
            </el-table>
          </el-col>
        </el-row>
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
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="employeeList">
              <el-table-column label="天赋" prop="char_149_scave"></el-table-column>
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
      employeeTable: [],
      employeeList: [],
      employeeList1: [],
      employeeList2: [],
      employeeList3: [],
      employeeList4: [],
      employeeList5: [],
      employeeList6: [],
      employee: [],
      total: 0
    }
  },
  // 创建时调用
  created () {
    this.getEmployeeTable()
    this.getEmployeeList()
  },
  mounted () {
    this.findemployee()
  },
  methods: {
    // 获取干员列表
    getemployeeTable () {
      const employeeTable = require('../assets/data/employee_table.json')
      this.employeeTable = employeeTable
      this.total = employeeTable.length
      // console.log(employeeTable)
    },
    // 干员名单
    getemployeeList () {
      var cnt = [0, 0, 0, 0, 0, 0]
      for (var en in this.employeeTable) {
        if (this.employeeTable[en].profession !== 'TRAP' && this.employeeTable[en].profession !== 'TOKEN') {
          if (this.employeeTable[en].rarity === 0) {
            this.employeeList1[cnt[0]] = { name: this.employeeTable[en].name }
            cnt[0]++
          } else if (this.employeeTable[en].rarity === 1) {
            this.employeeList2[cnt[1]] = { name: this.employeeTable[en].name }
            cnt[1]++
          } else if (this.employeeTable[en].rarity === 2) {
            this.employeeList3[cnt[2]] = { name: this.employeeTable[en].name }
            cnt[2]++
          } else if (this.employeeTable[en].rarity === 3) {
            this.employeeList4[cnt[3]] = { name: this.employeeTable[en].name }
            cnt[3]++
          } else if (this.employeeTable[en].rarity === 4) {
            this.employeeList5[cnt[4]] = { name: this.employeeTable[en].name }
            cnt[4]++
          } else if (this.employeeTable[en].rarity === 5) {
            this.employeeList6[cnt[5]] = { name: this.employeeTable[en].name }
            cnt[5]++
          }
        }
        // this.employeeList[cnt] = { name: this.employeeTable[en].profession }
        // cnt++
      }
      // console.log(this.employeeList)
    },
    haveEmployeeList () {

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
// 页头
.head-name {
  font-size: 30px;
  font-style: italic;
  font-weight: bold;
  padding: 0 0 0 20px;
}
.head-description {
  padding: 10px 0px 0px 0px;
}
.head-title {
  font-weight: bold;
}
</style>
