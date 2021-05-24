<template>
  <div id="em-echarts">
    <el-collapse v-model="activeName" class="collapse-title">
      <el-collapse-item title="能力排名" name="totalClass">
        <RankRadar
          :name="employeeName"
          :dataList="rankData"
          :indicatorList="tagList"
          :isActive="isActive('totalClass')"
        />
      </el-collapse-item>
      <el-collapse-item title="伤害类" name="damageClass">
        <DamageClass
          :employeeName="employeeName"
          :emParam="emParam"
          :pretreated="pretreatedData"
          :isClassActive="isActive('damageClass')"
        />
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
import DamageClass from './EmAnalysis/DamageClass.vue'
import RankRadar from '../Echarts/RankClass/RankRadar.vue'

export default {
  name: 'EmAnalysis',
  data () {
    return {
      pretreatedData: [],
      employeeNum: Number,
      tagList: [],
      activeName: []
    }
  },
  created () {
    this.getPertreated()
    this.countEmployee()
    this.createTagList()
  },
  props: {
    employeeName: String,
    employeeData: Object,
    employeeKey: String,
    emParam: Array
  },
  components: {
    DamageClass,
    RankRadar
  },
  computed: {
    // 数值排名
    rankData: function () {
      const employee = this.employeeData[this.employeeKey].phases
      const emLen = employee.atk.length - 1
      const rankData = [0, 0, 0, 0, 0]
      for (const Em in this.employeeData) {
        const compareEm = this.employeeData[Em].phases
        if (employee.atk[emLen][1] >= compareEm.atk[compareEm.atk.length - 1][1]) {
          rankData[0]++
        }
        if (employee.atkTime <= compareEm.atkTime) {
          rankData[1]++
        }
        if (employee.maxHp[emLen][1] >= compareEm.maxHp[compareEm.maxHp.length - 1][1]) {
          rankData[2]++
        }
        if (employee.def[emLen][1] >= compareEm.def[compareEm.def.length - 1][1]) {
          rankData[3]++
        }
        if (employee.magRes[emLen] >= compareEm.magRes[compareEm.magRes.length - 1]) {
          rankData[4]++
        }
      }
      return rankData
    },
    emParamTmp: function () {
      return this.emParam
    }
  },
  methods: {
    getPertreated () {
      this.pretreatedData = require('../../assets/data/pretreated.json')
    },
    countEmployee () {
      this.employeeNum = Object.keys(this.employeeData).length
    },
    createTagList () {
      const tagList = []
      tagList.push({ name: '攻击力', max: this.employeeNum })
      tagList.push({ name: '攻击间隔', max: this.employeeNum })
      tagList.push({ name: '最大生命值', max: this.employeeNum })
      tagList.push({ name: '防御力', max: this.employeeNum })
      tagList.push({ name: '法术抗性', max: this.employeeNum })
      this.tagList = tagList
    },
    // 判断折叠面板是否处于激活状态
    isActive (name) {
      for (let i = 0; i < this.activeName.length; i++) {
        if (name === this.activeName[i]) {
          return true
        }
      }
      return false
    }
  }
}
</script>

<style lang="scss" scoped>
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
</style>
