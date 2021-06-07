<template>
  <LineChart
    :chartId="'skill-perdamage-chart-' + skillId"
    :legendList="legendList"
    :seriesList="seriesList"
    :echartLabel="echartLabel"
    :isChanged="$store.state.isEmParamsUpdate"
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
    skillParam: Object,
    emParam: Object
  },
  components: {
    LineChart
  },
  computed: {
    seriesList () {
      const dataList = []
      const dataList1 = perDamage(this.emParam.atk, this.emParam.atkTime, this.baseAtkTime, this.damMod, this.atkMod)
      dataList.push(dataList1)
      const dataList2 = perDamage(this.skillParam.atk, this.skillParam.atkTime, this.baseAtkTime, this.damMod, this.atkMod)
      dataList.push(dataList2)
      return lineSeriesFormat(dataList, this.legendList)
    },
    echartLabel () {
      let xAxis = '防御'
      if (this.damMod === 'Mag') {
        xAxis = '法抗'
      }
      return labelFormat(xAxis, '秒伤害量')
    }
  }
}
</script>

<style>

</style>
