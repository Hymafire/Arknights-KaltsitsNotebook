<template>
  <div id="bar-style">
    <!-- Atk -->
    <div id="atk">
      <BarChart
        :chartId="'atk-bar-chart'"
        :title="'攻击力'"
        :seriesList="seriesList"
        :dataList="atkDataList"
        :isChanged="$store.state.em.isEmUpdate"
      />
    </div>
    <div id="atkTime">
      <BarChart
        :chartId="'atktime-bar-chart'"
        :title="'攻击速度'"
        :seriesList="seriesList"
        :dataList="atkTimeDataList"
        :isChanged="$store.state.em.isEmUpdate"
      />
    </div>
    <BarChart
      :chartId="'perdam-bar-chart'"
      :title="'秒输出量'"
      :seriesList="seriesList"
      :dataList="perDamDataList"
      :isChanged="$store.state.em.isEmUpdate"
    />
  </div>
</template>

<script>
import BarChart from '../../../Echarts/BarChart.vue'

export default {
  data () {
    return {
      seriesList: [
        { type: 'bar' },
        { type: 'bar' },
        { type: 'bar' }
      ]
    }
  },
  components: {
    BarChart
  },
  computed: {
    atkDataList () {
      const emData = this.$store.state.em.emData
      const emParam = this.$store.state.em.emParam
      const max = emData.phases.atk[emData.phases.atk.length - 1][1] + emData.favor.atk
      const min = emData.phases.atk[0][0]
      return this.formatData('atk', emParam.atk, max, min)
    },
    atkTimeDataList () {
      const emParam = this.$store.state.em.emParam
      return this.formatData('atkTime', emParam.atkTime, emParam.atkTime, emParam.atkTime)
    },
    perDamDataList () {
      const emData = this.$store.state.em.emData
      const emParam = this.$store.state.em.emParam
      const max = (emData.phases.atk[emData.phases.atk.length - 1][1] + emData.favor.atk) / emParam.atkTime
      const min = emData.phases.atk[0][0] / emParam.atkTime
      const perDam = emParam.atk / emParam.atkTime
      return this.formatData('perDam', perDam.toFixed(2), max.toFixed(2), min.toFixed(2))
    }
  },
  methods: {
    formatData (param, emValue, emMax, emMin) {
      const emData = this.$store.state.em.emData
      const emPretreatedData = this.$store.state.em.emPretreatedData
      const option = {
        dimensious: ['class', 'avg', 'max', 'min'],
        source: [
          {
            class: emData.name,
            avg: emValue,
            max: emMax,
            min: emMin
          },
          {
            class: emData.profession,
            min: emPretreatedData[param].profession[emData.profession].minValue,
            avg: emPretreatedData[param].profession[emData.profession].avgValue,
            max: emPretreatedData[param].profession[emData.profession].maxValue
          },
          {
            class: emData.position,
            min: emPretreatedData[param].position[emData.position].minValue,
            avg: emPretreatedData[param].position[emData.position].avgValue,
            max: emPretreatedData[param].position[emData.position].maxValue
          },
          {
            class: emData.rarity + 1 + '星',
            min: emPretreatedData[param].rarity[emData.rarity].minValue,
            avg: emPretreatedData[param].rarity[emData.rarity].avgValue,
            max: emPretreatedData[param].rarity[emData.rarity].maxValue
          },
          {
            class: '总体',
            min: emPretreatedData[param].totalAvg.minValue,
            avg: emPretreatedData[param].totalAvg.avgValue,
            max: emPretreatedData[param].totalAvg.maxValue
          }
        ]
      }
      return option
    }
  }
}
</script>

<style lang="scss" scoped>
#bar-style {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
</style>
