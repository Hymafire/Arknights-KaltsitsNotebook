<template>
  <div id="bar-style">
    <!-- Atk -->
    <div id="atk">
      <BarChart
        :chartId="'atk-bar-chart'"
        :title="'攻击力'"
        :seriesList="seriesList"
        :dataList="atkDataList"
        :isChanged="$store.state.isEmParamsUpdate"
      />
    </div>
    <div id="atkTime">
      <BarChart
        :chartId="'atktime-bar-chart'"
        :title="'攻击速度'"
        :seriesList="seriesList"
        :dataList="atkTimeDataList"
        :isChanged="$store.state.isEmParamsUpdate"
      />
    </div>
    <BarChart
      :chartId="'perdam-bar-chart'"
      :title="'秒输出量'"
      :seriesList="seriesList"
      :dataList="perDamDataList"
      :isChanged="$store.state.isEmParamsUpdate"
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
  props: {
    atk: Number,
    atkTime: Number
  },
  computed: {
    employee () {
      return this.$store.state.employeeData[this.$store.state.employeeKey]
    },
    atkDataList () {
      const max = this.employee.phases.atk[this.employee.phases.atk.length - 1][1] + this.employee.favor.atk
      const min = this.employee.phases.atk[0][0]
      return this.formatData('atk', this.atk, max, min)
    },
    atkTimeDataList () {
      return this.formatData('atkTime', this.atkTime, this.atkTime, this.atkTime)
    },
    perDamDataList () {
      const max = (this.employee.phases.atk[this.employee.phases.atk.length - 1][1] + this.employee.favor.atk) / this.atkTime
      const min = this.employee.phases.atk[0][0] / this.atkTime
      return this.formatData('perDam', this.perDam, max, min)
    },
    perDam () {
      return this.atk / this.atkTime
    }
  },
  methods: {
    formatData (param, emValue, emMax, emMin) {
      const option = {
        dimensious: ['class', 'avg', 'max', 'min'],
        source: [
          {
            class: this.employee.name,
            avg: emValue,
            max: emMax,
            min: emMin
          },
          {
            class: this.employee.profession,
            min: this.$store.state.emPretreatedData[param].profession[this.employee.profession].minValue,
            avg: this.$store.state.emPretreatedData[param].profession[this.employee.profession].avgValue,
            max: this.$store.state.emPretreatedData[param].profession[this.employee.profession].maxValue
          },
          {
            class: this.employee.position,
            min: this.$store.state.emPretreatedData[param].position[this.employee.position].minValue,
            avg: this.$store.state.emPretreatedData[param].position[this.employee.position].avgValue,
            max: this.$store.state.emPretreatedData[param].position[this.employee.position].maxValue
          },
          {
            class: this.employee.rarity + 1 + '星',
            min: this.$store.state.emPretreatedData[param].rarity[this.employee.rarity].minValue,
            avg: this.$store.state.emPretreatedData[param].rarity[this.employee.rarity].avgValue,
            max: this.$store.state.emPretreatedData[param].rarity[this.employee.rarity].maxValue
          },
          {
            class: '总体',
            min: this.$store.state.emPretreatedData[param].totalAvg.minValue,
            avg: this.$store.state.emPretreatedData[param].totalAvg.avgValue,
            max: this.$store.state.emPretreatedData[param].totalAvg.maxValue
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
