<template>
  <LineChart
    :chartId="'base-perdamage-chart'"
    :legendList="legendList"
    :seriesList="seriesList"
    :echartLabel="echartLabel"
    :isChanged="$store.state.em.isEmUpdated"
    :key="$store.state.em.emKey"
  />
</template>

<script>
/* 秒伤害量组件 */
import LineChart from '../../../Echarts/LineChart.vue'
import { perDamage } from '../../../utils/damageCalc.js'
import { labelFormat, lineSeriesFormat } from '../../../utils/echartsFormat.js'

export default {
  components: {
    LineChart
  },
  /* 计算返回：伤害列表 */
  computed: {
    seriesList: function () {
      const dataList = []
      const emParam = this.$store.state.em.emParam
      const emPretData = this.$store.state.em.emPretData
      let nameList = ['']
      const dataList1 = perDamage(emParam, emPretData)
      dataList.push(dataList1)
      if (emPretData.atkMod === 4) {
        const pretData = { atkMod: 0, damMod: emPretData.damMod }
        const dataList2 = perDamage(emParam, pretData)
        dataList.push(dataList2)
        nameList = ['远程', '近战']
      }
      return lineSeriesFormat(dataList, nameList)
    },
    echartLabel: function () {
      let xAxis = '防御'
      if (this.$store.state.em.emPretData.damMod === 'Mag') {
        xAxis = '法抗'
      }
      return labelFormat(xAxis, '秒伤害量')
    },
    legendList: function () {
      if (this.$store.state.em.emPretData.atkMod === 4) {
        return ['远程', '近战']
      }
      return []
    }
  }
}
</script>

<style>

</style>
