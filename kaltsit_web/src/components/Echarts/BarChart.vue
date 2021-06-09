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
    // legendList: Array,
    chartId: String,
    title: String,
    seriesList: Array,
    dataList: Object,
    isChanged: Boolean
  },
  mounted () {
    this.barChart()
  },
  methods: {
    barChart () {
      // 初始化DOM
      const myChart = echarts.getInstanceByDom(document.getElementById(this.chartId))
      if (myChart == null) {
        this.bar_chart = echarts.init(document.getElementById(this.chartId))
      }
      // 配置内容
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
      this.bar_chart.setOption(option)
      // 自适应 有Bug
      window.addEventListener('resize', () => { myChart.resize() })
      // window.onresize = myChart.resize
    }
  },
  watch: {
    isChanged: {
      handler () {
        this.barChart()
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
