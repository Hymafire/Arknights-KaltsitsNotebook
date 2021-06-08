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
      legendList: ['常态', '技能'],
      seriesList: []
    }
  },
  props: {
    skillId: String,
    skillParam: Object,
    emParam: Object,
    damMod: String,
    atkMod: Number
  },
  components: {
    LineChart
  },
  computed: {
    isChanged () {
      return this.$store.state.isEmParamsUpdate
    },
    echartLabel () {
      let xAxis = '防御'
      if (this.damMod === 'Mag') {
        xAxis = '法抗'
      }
      return labelFormat(xAxis, '秒伤害量')
    }
  },
  methods: {
    getSeriesList () {
      const dataList = []
      const dataList1 = perDamage(this.emParam.atk, this.emParam.atkTime, this.emParam.baseAtkTime, this.damMod, this.atkMod)
      dataList.push(dataList1)
      const dataList2 = perDamage(this.skillParam.atk, this.skillParam.atkTime, this.skillParam.baseAtkTime, this.damMod, this.atkMod)
      dataList.push(dataList2)
      this.seriesList = lineSeriesFormat(dataList, this.legendList)
    }
  },
  watch: {
    isChanged: {
      handler () {
        this.getSeriesList()
      }
    }
  }
}
</script>

<style>

</style>
