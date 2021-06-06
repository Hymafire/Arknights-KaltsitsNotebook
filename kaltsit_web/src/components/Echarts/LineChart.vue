<template>
  <div id="echart-clothes">
    <div :id="chartId" class="echarts-box" />
  </div>
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  name: 'LineChart',
  props: {
    chartId: String,
    legendList: Array,
    seriesList: Array,
    echartLabel: Array,
    isChanged: Boolean
  },
  mounted () {
    this.lineChart()
  },
  methods: {
    lineChart () {
      // 初始化DOM
      const myChart = echarts.getInstanceByDom(document.getElementById(this.chartId))
      if (myChart == null) {
        this.line_chart = echarts.init(document.getElementById(this.chartId))
      }
      // 配置内容
      const option = {
        animation: false,
        title: {
          left: 'center',
          text: this.echartLabel[0]
        },
        grid: {
          top: 35,
          // buttom 参数设置有问题（？？？） 替换成 y2
          y2: 30,
          left: 40,
          right: 40
        },
        // x轴
        xAxis: {
          name: this.echartLabel[1],
          minorTick: {
            show: true
          },
          minorSplitLine: {
            show: true
          }
        },
        // y轴
        yAxis: {
          name: this.echartLabel[2],
          minorTick: {
            show: true
          },
          minorSplitLine: {
            show: true
          }
        },
        // 数据
        series: this.seriesList
      }
      if (this.legendList !== []) {
        option.legend = {
          left: '70',
          data: this.legendList
        }
      }
      this.line_chart.setOption(option)
      // 自适应 有Bug
      // window.addEventListener('resize', () => { myChart.resize() })
      window.onresize = myChart.resize
    }
  },
  watch: {
    isChanged: {
      handler () {
        this.lineChart()
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
