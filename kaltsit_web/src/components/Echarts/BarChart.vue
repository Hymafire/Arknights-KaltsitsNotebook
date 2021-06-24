<template>
  <div id="echart-clothes">
    <div :id="chartId" class="echarts-box" />
  </div>
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  name: 'BarChart',
  props: {
    chartId: String,
    title: String,
    seriesList: Array,
    dataList: Object
  },
  mounted () {
    this.initBarChart()
  },
  computed: {
    barChartOption () {
      const option = {
        title: {
          text: this.title
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {},
        grid: {
          left: '3%',
          right: '4%',
          top: '8%',
          bottom: '3%',
          containLabel: true
        },
        dataset: this.dataList,
        xAxis: { type: 'category' },
        yAxis: {},
        series: this.seriesList
      }
      return option
    }
  },
  methods: {
    initBarChart () {
      this.barChart = echarts.init(document.getElementById(this.chartId))
      this.barChart.setOption(this.barChartOption)
      window.addEventListener('resize', () => { this.barChart.resize() })
    }
  },
  watch: {
    barChartOption: {
      handler () {
        this.barChart.setOption(this.barChartOption)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
#echart-clothes {
  width: 100%;
  overflow: hidden;
}
</style>
