<template>
  <LineChart
    :chartId="'skill-perdamage-chart-' + skillId"
    :legendList="legendList"
    :seriesList="seriesList"
    :echartLabel="echartLabel"
    :isChanged="$store.state.em.isEmUpdated"
    :key="skillId"
  />
</template>

<script>
import LineChart from '../../../../Echarts/LineChart.vue'
import { perDamage } from '../../../../utils/damageCalc.js'
import { labelFormat, lineSeriesFormat } from '../../../../utils/echartsFormat.js'

export default {
  data () {
    return {
      legendList: ['常态', '技能']
    }
  },
  props: {
    skillId: String,
    skillParam: Object
  },
  components: {
    LineChart
  },
  computed: {
    echartLabel () {
      let xAxis = '防御'
      const damMod = this.$store.state.em.emPretData.damMod
      if (damMod === 'Mag') {
        xAxis = '法抗'
      }
      return labelFormat(xAxis, '秒伤害量')
    },
    seriesList () {
      const dataList = []
      const emParam = this.$store.state.em.emParam
      const emPretData = this.$store.state.em.emPretData
      console.log()
      const dataList1 = perDamage(emParam, emPretData)
      dataList.push(dataList1)
      const dataList2 = perDamage(this.skillParam, emPretData)
      dataList.push(dataList2)
      return lineSeriesFormat(dataList, this.legendList)
    }
  }
}
</script>

<style>

</style>
