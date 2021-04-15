<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="220px" class="home-aside">
      <el-input prefix-icon="el-icon-user" placeholder="输入干员名称" v-model="searchname" class="search-input">
        <el-button slot="append" icon="el-icon-search" @click="findEmployee"/>
      </el-input>
      <el-tree :data="employeeList" :props="props" accordion @node-click="handleNodeClick" highlight-current />
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
          <el-col :span="2" :offset="7" />
          <el-col :span="13">
            <el-table :data="[employee]">
              <el-table-column label="属性列表：" prop="itemUsage" />
            </el-table>
          </el-col>
        </el-row>
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="[em_param]">
              <el-table-column label="最大生命" prop="maxHp" />
              <el-table-column label="攻击" prop="atk" />
              <el-table-column label="防御" prop="def" />
              <el-table-column label="法抗" prop="magicResistance" />
            </el-table>
          </el-col>
        </el-row>
        <!-- 第二排数据 -->
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="[em_param]">
              <el-table-column label="部署费用" prop="cost" />
              <el-table-column label="阻挡数" prop="blockCnt" />
              <el-table-column label="攻击间隔" prop="baseAttackTime" />
              <el-table-column label="再部署时间" prop="respawnTime" />
            </el-table>
          </el-col>
        </el-row>
        <!-- 第三排数据 -->
        <el-row :gutter="20" type="flex">
          <el-col :span="16" :offset="7">
            <el-table :data="[em_talent]">
              <el-table-column label="天赋" prop="talents" />
            </el-table>
          </el-col>
        </el-row>
        <!-- 数据输入栏 -->
        <el-form
          ref="loginFormRef"
          :model="infoForm"
          :rules="infoRules"
          label-width="0px"
          class="info_form"
        >
          <el-form-item prop="elite">
            <span>精英化等级：</span>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.elite" @keyup.enter.native="getEmployeeParam"/>
          </el-form-item>
          <el-form-item prop="level">
            <span>干员等级：</span>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.level" @keyup.enter.native="getEmployeeParam"/>
          </el-form-item>
          <el-form-item prop="favor">
            <span>信赖度：</span>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.favor" @keyup.enter.native="getEmployeeParam"/>
          </el-form-item>
          <el-form-item prop="potential">
            <span>潜能：</span>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.potential" @keyup.enter.native="getEmployeeParam"/>
          </el-form-item>
        </el-form>
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
      employee: [],
      em_param: [],
      em_talent: [],
      props: {
        name: 'name',
        label: 'name'
      },
      searchname: '斯卡蒂',
      infoForm: {
        elite: '0',
        level: '1',
        favor: '0',
        potential: '0'
      },
      infoRules: {
        elit: [
          { required: true, message: '精英化等级', trigger: 'blur' }
        ],
        level: [
          { required: true, message: '干员等级', trigger: 'blur' }
        ],
        favor: [
          { required: true, message: '信赖度', trigger: 'blur' }
        ],
        potation: [
          { required: true, message: '潜能', trigger: 'blur' }
        ]
      }
    }
  },
  // 创建时调用
  created () {
    this.getEmployeeTable()
    this.getEmployeeList()
  },
  mounted () {
    this.findEmployee()
  },
  methods: {
    // 获取干员列表
    getEmployeeTable () {
      const employeeTable = require('../assets/data/employee_table.json')
      this.employeeTable = employeeTable
    },
    // 干员名单
    getEmployeeList () {
      var cnt = [0, 0, 0, 0, 0, 0]
      var employeeChiList = [[], [], [], [], [], []]
      var rarity = 0
      // 遍历获得子列表
      for (var en in this.employeeTable) {
        if (this.employeeTable[en].profession !== 'TRAP' && this.employeeTable[en].profession !== 'TOKEN') {
          rarity = this.employeeTable[en].rarity
          employeeChiList[rarity][cnt[rarity]] = { name: this.employeeTable[en].name }
          cnt[rarity]++
        }
      }
      // 生成列表
      this.employeeList =
      [
        {
          name: '★★★★★★',
          children: employeeChiList[5]
        },
        {
          name: '★★★★★',
          children: employeeChiList[4]
        },
        {
          name: '★★★★',
          children: employeeChiList[3]
        },
        {
          name: '★★★',
          children: employeeChiList[2]
        },
        {
          name: '★★',
          children: employeeChiList[1]
        },
        {
          name: '★',
          children: employeeChiList[0]
        }
      ]
    },
    // 查找干员
    findEmployee () {
      for (var en in this.employeeTable) {
        if (this.employeeTable[en].name === this.searchname) {
          this.employee = this.employeeTable[en]
          break
        }
      }
      this.getEmployeeParam()
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
      const min_data = this.employee.phases[this.infoForm.elite].attributesKeyFrames[0].data
      const max_data = this.employee.phases[this.infoForm.elite].attributesKeyFrames[1].data
      const diff = this.employee.phases[this.infoForm.elite].maxLevel - 1
      this.em_param = min_data
      // 具体参数计算
      this.em_param.maxHp += Math.round((this.infoForm.level - 1) * (max_data.maxHp - min_data.maxHp) / diff)
      this.em_param.atk += Math.round((this.infoForm.level - 1) * (max_data.atk - min_data.atk) / diff)
      this.em_param.def += Math.round((this.infoForm.level - 1) * (max_data.def - min_data.def) / diff)
    },
    // 用于计算信赖的加成
    // 有bug
    employeeFavorClac () {
      const min_favor = Math.min(this.infoForm.favor, 100)
      const favor_data = this.employee.favorKeyFrames[1].data
      // 存储基础数据
      this.em_param.maxHp += Math.round(favor_data.maxHp * min_favor / 100)
      this.em_param.atk += Math.round(favor_data.atk * min_favor / 100)
      this.em_param.def += Math.round(favor_data.def * min_favor / 100)
    },
    // 用于计算潜能的加成
    employeeTalentClac () {
    },
    // 点击事件
    handleNodeClick (data) {
      this.searchname = data.name
      this.findEmployee()
    },
    resetLoginForm () {
      this.$refs.infoRef.resetFields()
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
// 输入框
.info_form {
  position: absolute;
  top: 171px;
  width: 22%;
  padding: 20px;
  box-sizing: border-box;
}
</style>
