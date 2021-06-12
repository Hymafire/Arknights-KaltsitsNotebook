<template>
  <div id="bar-style">
    <!-- Atk -->
    <div id="atk">
      <BarChart
        :chartId="'atk-bar-chart'"
        :title="'攻击力'"
        :seriesList="seriesList"
        :dataList="atkDataList"
        :isChanged="$store.state.em.isEmUpdated"
      />
    </div>
    <div id="atkTime">
      <BarChart
        :chartId="'atktime-bar-chart'"
        :title="'攻击速度'"
        :seriesList="seriesList"
        :dataList="atkTimeDataList"
        :isChanged="$store.state.em.isEmUpdated"
      />
    </div>
    <BarChart
      :chartId="'perdam-bar-chart'"
      :title="'秒输出量'"
      :seriesList="seriesList"
      :dataList="perDamDataList"
      :isChanged="$store.state.em.isEmUpdated"
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
      return this.formatData('perDam', perDam, max, min)
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
            avg: (emValue).toFixed(2),
            max: (emMax).toFixed(2),
            min: (emMin).toFixed(2)
          },
          {
            class: this.$store.state.loc.profList[emData.profession],
            min: (emPretreatedData[param].profession[emData.profession].minValue).toFixed(2),
            avg: (emPretreatedData[param].profession[emData.profession].avgValue).toFixed(2),
            max: (emPretreatedData[param].profession[emData.profession].maxValue).toFixed(2)
          },
          {
            class: this.$store.state.loc.posList[emData.position],
            min: (emPretreatedData[param].position[emData.position].minValue).toFixed(2),
            avg: (emPretreatedData[param].position[emData.position].avgValue).toFixed(2),
            max: (emPretreatedData[param].position[emData.position].maxValue).toFixed(2)
          },
          {
            class: emData.rarity + 1 + '星',
            min: (emPretreatedData[param].rarity[emData.rarity].minValue).toFixed(2),
            avg: (emPretreatedData[param].rarity[emData.rarity].avgValue).toFixed(2),
            max: (emPretreatedData[param].rarity[emData.rarity].maxValue).toFixed(2)
          },
          {
            class: '总体',
            min: (emPretreatedData[param].totalAvg.minValue).toFixed(2),
            avg: (emPretreatedData[param].totalAvg.avgValue).toFixed(2),
            max: (emPretreatedData[param].totalAvg.maxValue).toFixed(2)
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
