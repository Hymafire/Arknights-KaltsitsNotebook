<template>
  <div class="w">
    <!-- 基础信息 -->
    <BaseInfo :employee="employee" :employeeKey="employee.Key"/>
    <!-- 主信息区 -->
    <div class="info-main">
      <!-- 参数信息 -->
      <div id="param-info">
        <ParamInput
          :maxLevel="employee.phases.maxLevel"
          :potential="employee.maxPotential"
          @submitInfo="updateInfo"
        />
        <!-- changed_flag 用于表示 em_param 已经修改，需要更新 -->
        <ParamShow :showParam="emParam" />
        <RangeShow />
      </div>
      <!-- 天赋信息 -->
      <div>
        <TalentInfo
          :talentTable="employee.talents"
          :paramInputed="infoForm"
        />
        <!-- 技能信息 -->
        <SkillInfo
          :skillsName="employee.skills"
          :elite="infoForm.elite"
        />
      </div>
      <!-- 分析区 -->
      <EmAnalysis :emParam="emParam" />
      <!-- 分析区-end -->
    </div>
  </div>
</template>

<script>
/* eslint-disable camelcase */
import BaseInfo from './Eminfo/BaseInfo.vue'
import ParamInput from './Eminfo/ParamInput.vue'
import ParamShow from './Eminfo/ParamShow.vue'
import RangeShow from './Eminfo/RangeShow.vue'
import TalentInfo from './Eminfo/TalentInfo.vue'
import SkillInfo from './Eminfo/SkillInfo.vue'
import baseCalc from '../utils/baseCalc.js'
import EmAnalysis from './EmAnalysis.vue'

export default {
  data () {
    return {
      employee: [],
      emParam: [],
      infoForm: []
    }
  },
  mounted () {
    this.findEmployee()
  },
  components: {
    BaseInfo,
    ParamInput,
    ParamShow,
    RangeShow,
    TalentInfo,
    SkillInfo,
    EmAnalysis
  },
  computed: {
    employeeKey () {
      return this.$store.state.employeeKey
    }
  },
  methods: {
    // 查找干员
    findEmployee () {
      this.employee = this.$store.state.employeeData[this.employeeKey]
      this.letsCalc()
    },
    // 更新输入的信息
    updateInfo (info) {
      this.infoForm = info
    },
    // 计算函数入口
    letsCalc () {
      baseCalc.baseParamCalc(this.emParam, this.employee.phases, this.infoForm)
      baseCalc.favorCalc(this.emParam, this.employee.favor, this.infoForm.favorValue)
      baseCalc.potentialCalc(this.emParam, this.employee.potential, this.infoForm.potentialLevel)
      this.changeUpdate()
    },
    changeCollapse () {
      this.$store.commit('changeCollapse')
    },
    changeUpdate () {
      this.$store.commit('changeIsEmParamsUpdate')
    }
  },
  watch: {
    employeeKey: {
      handler () {
        this.findEmployee()
      }
    },
    infoForm: {
      handler () {
        this.letsCalc()
      },
      deep: true
    }
  }
}
</script>

<style lang="scss" scoped>
// 信息展示区
.w {
  max-width: 1080px;
  margin: 0 auto;
}
.info-main {
  padding: 3px;
  padding-top: 0px;
}
//
#param-info {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}
</style>
