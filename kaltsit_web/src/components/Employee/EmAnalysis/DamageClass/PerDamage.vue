<template>
  <LineChart
    :chartId="'base-perdamage-chart'"
    :legendList="legendList"
    :seriesList="seriesList"
    :echartLabel="echartLabel"
    :isChanged="$store.state.isEmParamsUpdate"
    :key="$store.state.employeeName"
  />
</template>

<script>
/* 秒伤害量组件 */
import LineChart from '../../../Echarts/LineChart.vue'
import { perDamage } from '../../../utils/damageCalc.js'
import { labelFormat, lineSeriesFormat } from '../../../utils/echartsFormat.js'

export default {
  /* 参数：攻击力、攻击间隔、攻击速度、攻击描述、伤害类型 */
  props: {
    atk: Number,
    atkTime: Number,
    baseAtkTime: Number,
    atkMod: Number,
    damMod: String
  },
  components: {
    LineChart
  },
  /* 计算返回：伤害列表 */
  computed: {
    seriesList: function () {
      const dataList = []
      let nameList = ['']
      const dataList1 = perDamage(this.atk, this.atkTime, this.baseAtkTime, this.damMod, this.atkMod)
      dataList.push(dataList1)
      if (this.atkMod === 4) {
        const dataList2 = perDamage(this.atk, this.atkTime, this.baseAtkTime, this.damMod, 0)
        dataList.push(dataList2)
        nameList = ['远程', '近战']
      }
      return lineSeriesFormat(dataList, nameList)
    },
    echartLabel: function () {
      let xAxis = '防御'
      if (this.damMod === 'Mag') {
        xAxis = '法抗'
      }
      return labelFormat(xAxis, '秒伤害量')
    },
    legendList: function () {
      if (this.atkMod === 4) {
        return ['远程', '近战']
      }
      return []
    }
  }
}
</script>

<style>

</style>
