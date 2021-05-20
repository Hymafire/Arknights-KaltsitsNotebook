<template>
  <el-container>
    <!-- 头部 -->
    <el-header height="42px">
      <div class="head-name">
        {{ employee.name }}
      </div>
    </el-header>
    <!-- 头部-end -->
    <!-- 信息区 -->
    <el-main class="info-main">
      <div class="w">
        <!-- 基础信息 -->
        <BaseInfo :employee="employee" :employeeKey="employee.Key"/>
        <!-- 参数信息 -->
        <div id="param-info">
          <ParamInput
            :maxLevel="employee.phases.maxLevel"
            :potential="employee.maxPotential"
            @submitInfo="updateInfo"
          />
          <!-- changed_flag 用于表示 em_param 已经修改，需要更新 -->
          <ParamShow :showParam="em_param" :changed="changed_flag" />
          <RangeShow />
        </div>
        <!-- 天赋信息 -->
        <div>
          <TalentInfo
            :talentTable="employee.talents"
            :paramInputed="infoForm"
            :changed="changed_flag"
          />
          <!-- 技能信息 -->
          <SkillInfo
            :employeeName="employee_name"
            :skillsName="employee.skills"
            :elite="infoForm.elite"
          />
        </div>
        <!-- 分析区 -->
        <el-collapse v-model="activeName" class="collapse-title">
          <el-collapse-item title="秒伤害量" name="1">
            <PerDamage
              :atk="em_param.atk"
              :atkTime="em_param.atkTime"
              :isActive="isActive('1')"
            />
          </el-collapse-item>
          <el-collapse-item title="总伤害量" name="2">
            <DamageTotal
              :avgDef="pretreated.enAvgDef"
              :atk="em_param.atk"
              :atkTime="em_param.atkTime"
              :isActive="isActive('2')"
            />
          </el-collapse-item>
          <el-collapse-item title="能力评分表" name="3">
            <RankRadar :name="employee_name" :isActive="isActive('3')"/>
          </el-collapse-item>
        </el-collapse>
        <!-- 分析区-end -->
      </div>
    </el-main>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
import BaseInfo from './Eminfo/BaseInfo.vue'
import ParamInput from './Eminfo/ParamInput.vue'
import ParamShow from './Eminfo/ParamShow.vue'
import RangeShow from './Eminfo/RangeShow.vue'
import TalentInfo from './Eminfo/TalentInfo.vue'
import SkillInfo from './Eminfo/SkillInfo.vue'
import RankRadar from '../Echarts/RankClass/RankRadar.vue'
import PerDamage from '../Echarts/DamageClass/PerDamage.vue'
import DamageTotal from '../Echarts/DamageClass/DamageTotal.vue'
import baseCalc from '../utils/baseCalc.js'

export default {
  data () {
    return {
      employeeData: [],
      pretreated: [],
      employee: [],
      em_param: [],
      infoForm: [],
      changed_flag: false,
      activeName: []
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
    TalentInfo,
    SkillInfo,
    PerDamage,
    DamageTotal,
    RankRadar
  },
  methods: {
    // 获取干员列表
    getEmployeeData () {
      this.employeeData = require('@/assets/data/employeedata.json')
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
      this.letsCalc()
    },
    // 更新输入的信息
    updateInfo (info) {
      this.infoForm = info
    },
    // 计算函数入口
    letsCalc () {
      baseCalc.baseParamCalc(this.em_param, this.employee.phases, this.infoForm)
      baseCalc.favorCalc(this.em_param, this.employee.favor, this.infoForm.favorValue)
      baseCalc.potentialCalc(this.em_param, this.employee.potential, this.infoForm.potentialLevel)
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
      this.$store.commit('changeCollapse')
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
        this.letsCalc()
        this.$forceUpdate()
      },
      deep: true
    }
  }
}
</script>

<style lang="scss" scoped>
// 标题
.head-name {
  height: 100%;
  font-size: 28px;
  font-style: italic;
  font-weight: bold;
  padding-left: 20px;
  border-bottom: 2px solid #dcdfe6;
}
// 信息展示区
.el-main {
  padding: 10px;
  padding-top: 7px !important;
}
.w {
  max-width: 1080px;
  margin: 0 auto;
}
//
#param-info {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}
// 图形区
// 抽屉标题
.collapse-title {
  height: 30px;
}
//
/deep/.el-collapse-item__header {
  height: 39px;
  font-size: 16px;
  font-weight: 700;
  padding-left: 20px;
  letter-spacing: 2px;
}
//
/deep/.el-collapse-item__content {
  padding: 0px;
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
