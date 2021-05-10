<template>
  <el-container>
    <!-- 头部 -->
    <el-header>
      <div class="head-name">
        <el-button @click="changeCollapse">|||</el-button>
        {{ employee.name }}
      </div>
    </el-header>
    <!-- 信息区 -->
    <el-main>
      <div class="w">
        <!-- 基础信息 -->
        <BaseInfo />
        <!-- 参数信息 -->
        <div class="base-info card-style">
          <ParamInput
            :max-level="employee.phases.maxLevel"
            :potential="employee.maxPotential"
            @submitInfo="updateInfo"
          />
          <!-- changed_flag 用于表示 em_param 已经修改，需要更新 -->
          <ParamShow
            :show-param="em_param"
            :changed="changed_flag"
          />
          <RangeShow />
        </div>
        <!-- 分析区 -->
        <el-collapse
          v-model="activeName"
          class="aaa"
        >
          <el-collapse-item
            title="秒伤害量"
            name="1"
          >
            <PerDamage
              :atk="em_param.atk"
              :atk-time="em_param.atkTime"
              :is-active="isActive('1')"
            />
          </el-collapse-item>
          <el-collapse-item
            title="总伤害量"
            name="2"
          >
            <DamageTotal
              :avg-def="pretreated.enAvgDef"
              :atk="em_param.atk"
              :atk-time="em_param.atkTime"
              :is-active="isActive('2')"
            />
          </el-collapse-item>
          <el-collapse-item
            title="能力评分表"
            name="3"
          >
            <RankRadar :name="employee_name" />
          </el-collapse-item>
        </el-collapse>
      </div>
    </el-main>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
import PerDamage from '../Echarts/DamageClass/PerDamage.vue'
import DamageTotal from '../Echarts/DamageClass/DamageTotal.vue'
import BaseInfo from './Eminfo/BaseInfo.vue'
import ParamInput from './Eminfo/ParamInput.vue'
import ParamShow from './Eminfo/ParamShow.vue'
import RangeShow from './Eminfo/RangeShow.vue'
import RankRadar from '../Echarts/RankClass/RankRadar.vue'
import baseClac from '../utils/baseClac.js'

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
      changed_flag: false,
      activeName: [],
      isCollapse: false
    }
  },
  // 创建时调用
  created () {
    this.getEmployeeData()
  },
  mounted () {
    this.findEmployee()
  },
  props: {
    employee_name: {
      type: String,
      default: '斯卡蒂'
    }
  },
  components: {
    BaseInfo,
    ParamInput,
    ParamShow,
    RangeShow,
    PerDamage,
    DamageTotal,
    RankRadar
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
      for (const em in this.employeeData) {
        if (this.employeeData[em].name === this.employee_name) {
          this.employee = this.employeeData[em]
          break
        }
      }
      this.letsClac()
    },
    // 更新输入的信息
    updateInfo (info) {
      this.infoForm = info
    },
    // 计算函数入口
    letsClac () {
      baseClac.baseParamClac(this.em_param, this.employee.phases, this.infoForm)
      baseClac.favorClac(this.em_param, this.employee.favor, this.infoForm.favorValue)
      baseClac.potentialClac(this.em_param, this.employee.potential, this.infoForm.potentialLevel)
      this.changed_flag = !this.changed_flag
    },
    // 判断折叠面板是否处于激活状态
    isActive (name) {
      for (let i = 0; i < this.activeName.length; i++) {
        if (name === this.activeName[i]) {
          return true
        }
      }
      return false
    },
    changeCollapse () {
      this.isCollapse = !this.isCollapse
      this.$emit('listCollapse', this.isCollapse)
    }
  },
  watch: {
    employee_name: {
      handler () {
        this.findEmployee()
      }
    },
    infoForm: {
      handler () {
        this.letsClac()
        this.$forceUpdate()
      },
      deep: true
    }
  }
}
</script>

<style lang="scss" scoped>
// 标题
.el-header {
  height: 50px !important;
  line-height: 50px;
  z-index: 100;
}
.list-btn {
  font-size: 25px;
  font-weight: bold;
  padding: 0px 5px;
}
.head-name {
  font-size: 30px;
  font-style: italic;
  font-weight: bold;
  padding-left: 50px;
  border-bottom: 2px solid #dcdfe6;
}
// 信息展示区
.el-main {
  padding-top: 7px !important;
}
.w {
  max-width: 1200px;
  margin: 0 auto;
}
/deep/.el-collapse-item__header {
  height: 32px;
  line-height: 32px;
  font-size: 15px;
  font-weight: 700;
  padding-left: 20px;
}
//
.base-info {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  >div {
    text-align: center;
    min-width: 360px;
    max-width: 400px;
    height: 200px;
    margin-left: 10px;
  }
}
.aaa {
  height: 30px;
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
