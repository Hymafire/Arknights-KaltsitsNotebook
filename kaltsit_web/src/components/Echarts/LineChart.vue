<template>
  <div id="line-chart" class="echarts-box" />
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  name: 'LineChart',
  props: {
    legendList: [],
    seriesList: Array,
    echartLabel: Array,
    isChanged: Boolean,
    isActive: {
      type: Boolean,
      default: false
    }
  },
  mounted () {
    this.lineChart()
  },
  computed: {
    employeeName: function () {
      return this.$store.state.employeeName
    }
  },
  methods: {
    lineChart () {
      // 初始化DOM
      const myChart = echarts.getInstanceByDom(document.getElementById('line-chart'))
      if (myChart == null) {
        this.line_chart = echarts.init(document.getElementById('line-chart'))
      }
      // 配置内容
      const option = {
        animation: false,
        title: {
          left: 'center',
          text: this.echartLabel[0]
        },
        // 曲线标题
        legend: {
          left: '70%',
          data: this.legendList
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
      this.line_chart.setOption(option)
      // 自适应 有Bug
      if (this.isActive) {
        window.addEventListener('resize', () => { myChart.resize() })
      }
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

<style>

</style>
