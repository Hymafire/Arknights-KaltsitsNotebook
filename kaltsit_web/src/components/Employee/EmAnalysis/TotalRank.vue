<template>
  <RankRadar
    :key="this.$store.state.em.emKey"
    :dataList="rankData"
    :indicatorList="tagList"
  />
</template>

<script>
import RankRadar from '../../Echarts/RankRadar.vue'

export default {
  data () {
    return {
      tagList: []
    }
  },
  created () {
    this.createTagList()
  },
  components: {
    RankRadar
  },
  computed: {
    rankData: function () {
      const employee = this.$store.state.em.emData.phases
      const emFavor = this.$store.state.em.emData.favor
      const emLen = employee.atk.length - 1
      const rankData = [0, 0, 0, 0, 0]
      for (const em in this.$store.state.em.employeeTable) {
        const compareEm = this.$store.state.em.employeeTable[em].phases
        const compareEmF = this.$store.state.em.employeeTable[em].favor
        const compareEmLen = compareEm.atk.length - 1
        if (employee.atk[emLen][1] + emFavor.atk >= compareEm.atk[compareEmLen][1] + compareEmF.atk) {
          rankData[0]++
        }
        if (employee.atkTime <= compareEm.atkTime) {
          rankData[1]++
        }
        if (employee.maxHp[emLen][1] + emFavor.maxHp >= compareEm.maxHp[compareEmLen][1] + compareEmF.maxHp) {
          rankData[2]++
        }
        if (employee.def[emLen][1] + emFavor.def >= compareEm.def[compareEmLen][1] + compareEmF.def) {
          rankData[3]++
        }
        if (employee.magRes[emLen] >= compareEm.magRes[compareEmLen]) {
          rankData[4]++
        }
      }
      return rankData
    }
  },
  methods: {
    createTagList () {
      const tagList = []
      const employeeNum = this.$store.state.em.emPretreatedData.atk.totalAvg.emNum
      tagList.push({ name: '攻击力', max: employeeNum })
      tagList.push({ name: '攻击间隔', max: employeeNum })
      tagList.push({ name: '最大生命值', max: employeeNum })
      tagList.push({ name: '防御力', max: employeeNum })
      tagList.push({ name: '法术抗性', max: employeeNum })
      this.tagList = tagList
    }
  }
}
</script>

<style>

</style>
