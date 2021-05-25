<template>
  <div id="em-analysis">
    <el-collapse v-model="activeName" class="collapse-title">
      <el-collapse-item title="能力排名" name="totalRank">
        <RankRadar
          :name="employeeName"
          :dataList="rankData"
          :indicatorList="tagList"
          :isActive="isActive('totalRank')"
        />
      </el-collapse-item>
      <el-collapse-item title="秒伤害量" name="perDamage">
        <PerDamage
          :atk="emParam.atk"
          :atkTime="emParam.atkTime"
          :isActive="isActive('perDamage')"
        />
      </el-collapse-item>
      <el-collapse-item title="总伤害量" name="totalDamage">
        <DamageTotal
          :avgDef="pretreatedData.enAvgDef"
          :atk="emParam.atk"
          :atkTime="emParam.atkTime"
          :isActive="isActive('totalDamage')"
        />
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
// import DamageClass from './EmAnalysis/DamageClass.vue'
import RankRadar from '../Echarts/RankClass/RankRadar.vue'
import PerDamage from '../Echarts/DamageClass/PerDamage.vue'
import DamageTotal from '../Echarts/DamageClass/DamageTotal.vue'

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
    emParam: Array,
    isChanged: Boolean
  },
  components: {
    // DamageClass,
    RankRadar,
    PerDamage,
    DamageTotal
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
  },
  watch: {
    isChanged: {
      handler () {
        this.$forceUpdate()
      },
      immediate: true
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
