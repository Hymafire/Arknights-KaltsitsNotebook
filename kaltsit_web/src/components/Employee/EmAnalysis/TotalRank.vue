<template>
  <RankRadar
    :name="employeeName"
    :dataList="rankData"
    :indicatorList="tagList"
  />
</template>

<script>
import RankRadar from '../../Echarts/RankRadar.vue'

export default {
  data () {
    return {
      employeeNum: Number,
      tagList: []
    }
  },
  created () {
    this.countEmployee()
    this.createTagList()
  },
  components: {
    RankRadar
  },
  props: {
    employeeData: Object,
    employeeKey: String
  },
  computed: {
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
    employeeName: function () {
      return this.$store.state.employeeName
    }
  },
  methods: {
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
    }
  }
}
</script>

<style>

</style>
