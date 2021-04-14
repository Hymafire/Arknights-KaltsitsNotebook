<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="220px" class="home-aside">
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
          <el-row :gutter="10" type="flex">
            <el-col :span="6">
              <span class="head-name">{{ employee.name }}</span>
            </el-col>
            <el-col :span="18" class="head-description">
              <span class="head-title">特性：</span>
              <span>{{ employee.description }}</span>
            </el-col>
          </el-row>
        </div>
        <!-- 第一排数据 -->
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="em_param">
              <el-table-column label="属性："></el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="[em_param]">
              <el-table-column label="最大生命" prop="maxHp"></el-table-column>
              <el-table-column label="攻击" prop="atk"></el-table-column>
              <el-table-column label="防御" prop="def"></el-table-column>
              <el-table-column label="法抗" prop="magicResistance"></el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <!-- 第二排数据 -->
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="[em_param]">
              <el-table-column label="部署费用" prop="cost"></el-table-column>
              <el-table-column label="阻挡数" prop="blockCnt"></el-table-column>
              <el-table-column label="攻击间隔" prop="baseAttackTime"></el-table-column>
              <el-table-column label="再部署时间" prop="respawnTime"></el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <!-- 第三排数据 -->
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="[employee]">
              <el-table-column label="天赋" prop="talents"></el-table-column>
            </el-table>
          </el-col>
        </el-row>
        <!-- 分页 -->
      </el-card>
    </el-main>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
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
      em_param: [],
      total: 0,
      props: {
        name: 'name',
        label: 'name'
      },
      searchname: '斯卡蒂',
      elite: '0',
      level: '40',
      favor: '100'
    }
  },
  // 创建时调用
  created () {
    this.getEmployeeTable()
    this.getEmployeeList()
    this.haveEmployeeList()
  },
  mounted () {
    this.findEmployee()
  },
  methods: {
    // 获取干员列表
    getEmployeeTable () {
      const employeeTable = require('../assets/data/employee_table.json')
      this.employeeTable = employeeTable
      this.total = employeeTable.length
    },
    // 干员名单
    getEmployeeList () {
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
      }
    },
    haveEmployeeList () {
      this.employeeList =
      [
        {
          name: '★★★★★★',
          children: this.employeeList6
        },
        {
          name: '★★★★★',
          children: this.employeeList5
        },
        {
          name: '★★★★',
          children: this.employeeList4
        },
        {
          name: '★★★',
          children: this.employeeList3
        },
        {
          name: '★★',
          children: this.employeeList2
        },
        {
          name: '★',
          children: this.employeeList1
        }
      ]
    },
    findEmployee () {
      for (var en in this.employeeTable) {
        if (this.employeeTable[en].name === this.searchname) {
          this.employee = this.employeeTable[en]
          break
        }
      }
    },
    /* ========================================== 分界线 ========================================= */
    // 用于计算干员的基础属性
    getEmployeeParam () {
      this.employeeBaseParamClac()
      this.employeeFavorClac()
      // 潜能
      // 天赋
    },
    // 用于计算干员的等级数据
    employeeBaseParamClac () {
      const min_data = this.employee.phases[this.elite].attributesKeyFrames[0].data
      const max_data = this.employee.phases[this.elite].attributesKeyFrames[1].data
      const diff = this.employee.phases[this.elite].maxLevel - 1
      this.em_param = min_data
      // 具体参数计算
      this.em_param.maxHp += Math.round((this.level - 1) * (max_data.maxHp - min_data.maxHp) / diff)
      this.em_param.atk += Math.round((this.level - 1) * (max_data.atk - min_data.atk) / diff)
      this.em_param.def += Math.round((this.level - 1) * (max_data.def - min_data.def) / diff)
    },
    // 用于计算信赖的加成
    employeeFavorClac () {
      const min_favor = Math.min(this.favor, 100)
      const favor_data = this.employee.favorKeyFrames[1].data
      this.em_param.maxHp += Math.round(favor_data.maxHp * min_favor / 100)
      this.em_param.atk += Math.round(favor_data.atk * min_favor / 100)
      this.em_param.def += Math.round(favor_data.def * min_favor / 100)
      console.log(this.em_param)
    },
    // 点击事件
    handleNodeClick (data) {
      this.searchname = data.name
      this.findEmployee()
      this.getEmployeeParam()
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
