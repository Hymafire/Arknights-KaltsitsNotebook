<template>
  <el-container class="info-container">
    <el-card>
      <!-- 头部 -->
      <div slot="header" class="clearfix">
        <el-row :gutter="10" type="flex">
          <el-col :span="6">
            <span class="head-name">{{ employee.name }}</span>
          </el-col>
          <el-col :span="18" class="head-description">
            <span class="head-title">描述：</span>
            <span>{{ employee.description }}</span>
          </el-col>
        </el-row>
      </div>
      <!-- 信息输入区 -->
      <div>
        <el-row :gutter="10" type="flex">
          <el-col>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.elite" />
          </el-col>
          <el-col>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.level" />
          </el-col>
          <el-col>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.favor" />
          </el-col>
          <el-col>
            <el-input prefix-icon="el-icon-user" v-model="infoForm.potential" />
          </el-col>
          <el-col :span="2">
            <el-button type="primary" @click="getInfo">确认</el-button>
          </el-col>
        </el-row>
      </div>
      <hr>
      <!-- 基础信息区 -->
      <div>
        <el-row :gutter="20" type="flex">
          <el-col :span="24">
            <el-table :data="[em_param]">
              <el-table-column label="最大生命" prop="maxHp" />
              <el-table-column label="攻击" prop="atk" />
              <el-table-column label="防御" prop="def" />
              <el-table-column label="法抗" prop="magRes" />
            </el-table>
          </el-col>
        </el-row>
        <el-row :gutter="20" type="flex">
          <el-col :span="24">
            <el-table :data="[em_param]">
              <el-table-column label="部署费用" prop="cost" />
              <el-table-column label="阻挡数" prop="blockCnt" />
              <el-table-column label="攻击间隔" prop="atkTime" />
              <el-table-column label="再部署时间" prop="respawnTime" />
            </el-table>
          </el-col>
        </el-row>
        <el-row :gutter="20" type="flex">
          <el-col :span="24">
            <el-table :data="[em_talents]">
              <el-table-column label="天赋" prop="name" />
            </el-table>
          </el-col>
        </el-row>
      </div>
      <hr>
      <!-- 分析区 -->
      <div>
      </div>
    </el-card>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
export default {
  data () {
    return {
      employeeData: [],
      employee: [],
      em_param: [],
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
        potential: [
          { required: true, message: '潜能', trigger: 'blur' }
        ]
      }
    }
  },
  // 创建时调用
  created () {
    this.getEmployeeData()
    this.findEmployee()
  },
  mounted () {
  },
  props: {
    employee_name: String
  },
  methods: {
    // 获取干员列表
    getEmployeeData () {
      const employeeData = require('@/assets/data/employeedata.json')
      this.employeeData = employeeData
    },
    // 查找干员
    findEmployee () {
      for (var em in this.employeeData) {
        if (this.employeeData[em].name === this.employee_name) {
          this.employee = this.employeeData[em]
          break
        }
      }
      this.employeeBaseParamClac()
      this.employeeFavorClac()
    },
    /* ========================================== 分界线 ========================================= */
    // 用于计算干员的等级数据
    employeeBaseParamClac () {
      const Lv = this.infoForm.level - 1
      const elt = this.infoForm.elite
      const diff = this.employee.phases.maxLevel[elt] - 1
      // 具体参数计算及赋值
      this.em_param.maxHp = this.employee.phases.maxHp[elt][0] + Math.round(Lv * (this.employee.phases.maxHp[elt][1] - this.employee.phases.maxHp[elt][0]) / diff)
      this.em_param.atk = this.employee.phases.atk[elt][0] + Math.round(Lv * (this.employee.phases.atk[elt][1] - this.employee.phases.atk[elt][0]) / diff)
      this.em_param.def = this.employee.phases.def[elt][0] + Math.round(Lv * (this.employee.phases.def[elt][1] - this.employee.phases.def[elt][0]) / diff)
      this.em_param.magRes = this.employee.phases.magRes[elt]
      this.em_param.cost = this.employee.phases.cost[elt]
      this.em_param.blockCnt = this.employee.phases.blockCnt[elt]
      this.em_param.range = this.employee.phases.range[elt]
      this.em_param.atkTime = this.employee.phases.atkTime
      this.em_param.respawnTime = this.employee.phases.respawnTime
    },
    // 用于计算信赖的加成
    // 有bug
    employeeFavorClac () {
      const min_favor = Math.min(this.infoForm.favor, 100)
      // 存储基础数据
      this.em_param.maxHp += Math.round(this.employee.favor.maxHp * min_favor / 100)
      this.em_param.atk += Math.round(this.employee.favor.atk * min_favor / 100)
      this.em_param.def += Math.round(this.employee.favor.def * min_favor / 100)
      console.log(this.em_param)
    },
    // 用于计算潜能的加成
    employeeTalentClac () {
    },
    getInfo () {
    }
  },
  watch: {
    employee_name: {
      handler: function () {
        this.findEmployee()
      },
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>
.info-container {
  height: 100%;
  padding: 0px;
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
.el-card {
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15) !important;
  width: 100%;
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
