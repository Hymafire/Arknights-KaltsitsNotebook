<template>
  <el-container>
    <!-- 头部 -->
    <el-header>
      <el-row :gutter="10" type="flex">
        <el-col :span="6">
          <span class="head-name">{{ employee.name }}</span>
        </el-col>
        <el-col :span="18" class="head-description">
          <span class="head-title">描述：</span>
          <span>{{ employee.description }}</span>
        </el-col>
      </el-row>
    </el-header>
    <hr>
    <!-- 信息区 -->
    <el-main>
      <BaseInfo
        :maxLevel="employee.phases.maxLevel"
        :potential="employee.maxPotential"
        :showParam="em_param"
        @submitInfo="updateInfo"
      />
      <div class="base-info card-style">
        <ParamInput
          :maxLevel="employee.phases.maxLevel"
          :potential="employee.maxPotential"
          @submitInfo="updateInfo"
        />
        <!-- changed_flag 用于表示 em_param 已经修改，需要更新 -->
        <ParamShow :showParam="em_param" :changed="changed_flag" />
        <RangeShow />
      </div>
      <!-- 分析区 -->
      <PerDamage :atk="em_param.atk" :atkTime="em_param.atkTime"/>
      <DamageTotal :avgDef="pretreated.enAvgDef" :atk="em_param.atk" :atkTime="em_param.atkTime"/>
      <div id="rank-radar" class="echarts-box" />
    </el-main>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'
import PerDamage from '../Echarts/DamageClass/PerDamage.vue'
import DamageTotal from '../Echarts/DamageClass/DamageTotal.vue'
import BaseInfo from './Eminfo/BaseInfo.vue'
import ParamInput from './Eminfo/ParamInput.vue'
import ParamShow from './Eminfo/ParamShow.vue'
import RangeShow from './Eminfo/RangeShow.vue'

export default {
  data () {
    return {
      employeeData: [],
      skillData: [],
      pretreated: [],
      employee: [],
      employeeSkill: [],
      em_param: [],
      infoForm: [],
      changed_flag: false
    }
  },
  // 创建时调用
  created () {
    this.getEmployeeData()
    this.findEmployee()
  },
  props: {
    employee_name: String
  },
  components: {
    BaseInfo,
    ParamInput,
    ParamShow,
    RangeShow,
    PerDamage,
    DamageTotal
  },
  methods: {
    // 获取干员列表
    getEmployeeData () {
      this.employeeData = require('@/assets/data/employeedata.json')
      this.skillData = require('@/assets/data/skill_table.json')
      this.pretreated = require('@/assets/data/pretreated.json')
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
      this.changed_flag = !this.changed_flag
    },
    updateInfo (info) {
      this.infoForm = info
    },
    /* ========================================== 分界线 ========================================= */
    // 用于计算干员的等级数据
    employeeBaseParamClac () {
      const Lv = this.infoForm.levelValue - 1
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
      this.em_param.baseAtkTime = 100.0
      this.em_param.respawnTime = this.employee.phases.respawnTime
    },
    // 用于计算信赖的加成
    // 有bug
    employeeFavorClac () {
      const min_favor = this.infoForm.favorValue
      // 存储基础数据
      this.em_param.maxHp += Math.round(this.employee.favor.maxHp * min_favor / 100)
      this.em_param.atk += Math.round(this.employee.favor.atk * min_favor / 100)
      this.em_param.def += Math.round(this.employee.favor.def * min_favor / 100)
    },
    // 用于计算潜能的加成
    employeeTalentClac () {
    },
    getInfo () {
    },
    // 绘图区 ===============================================================
    // 能力排名
    rankRadar () {
      const data = []
      for (var em in this.employeeData) {
        const em_data = this.employeeData[em]
        console.log(em_data)
      }
      this.rank_radar = echarts.init(document.getElementById('rank_radar'))
      const option = {
        title: {
          text: '能力评分图'
        },
        radar: {
          name: {
          },
          indicator: [
            { name: '最大生命力', max: 200 },
            { name: '攻击力', max: 200 },
            { name: '防御力', max: 200 },
            { name: '法抗', max: 200 },
            { name: '攻击速度', max: 200 }
            // { name: '攻击范围', max: 5 },
          ]
        },
        series: [
          {
            name: 'rank_radar',
            type: 'radar',
            data: data
          }
        ]
      }
      this.rank_radar.setOption(option)
    }
  },
  watch: {
    employee_name: {
      handler () {
        this.findEmployee()
      },
      immediate: true
    },
    infoForm: {
      handler () {
        this.employeeBaseParamClac()
        this.employeeFavorClac()
        this.changed_flag = !this.changed_flag
        // 更新数据
        this.$forceUpdate()
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>
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
// 敌方名称
.head-title {
  font-weight: bold;
}
// 属性标题
.param-title {
  font-weight: bold;
}
// 图表容器
.echarts-box {
  width: 600px;
  height: 400px;
}
//
.base-info {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  >div {
    text-align: left;
    min-width: 360px;
    height: 160px;
    margin-left: 10px;
  }
}
// 卡片
.card-style {
  margin-bottom: 5px;
  background-color: white;
  border: 1px solid #ebeef5;
  border-radius: 4px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15);
}
</style>
