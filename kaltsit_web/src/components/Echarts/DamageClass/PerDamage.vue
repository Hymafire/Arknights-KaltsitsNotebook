<template>
  <div
    id="pre-damage"
    class="echarts-box"
  />
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  name: 'PerDamage',
  props: {
    atk: Number,
    atkTime: Number,
    isActive: {
      type: Boolean,
      default: false
    }
  },
  mounted () {
    this.preDamageChart()
  },
  methods: {
    preDamageChart () {
      // 数据
      const data = []
      for (let def = 0; def <= 800; def++) {
        const damage = Math.max(this.atk - def, this.atk * 0.05)
        const pre_dam = damage / this.atkTime
        data.push([def, pre_dam])
      }
      // 初始化DOM
      const myChart = echarts.getInstanceByDom(document.getElementById('pre-damage'))
      if (myChart == null) {
        this.pre_dam_chart = echarts.init(document.getElementById('pre-damage'))
      }
      // 配置内容
      const option = {
        // 是否开启动画化
        animation: false,
        // 标题
        title: {
          left: 'center',
          text: '秒伤害量-防御'
        },
        // 四周间距
        grid: {
          top: 50,
          // buttom 参数设置有问题（？？？） 替换成 y2
          y2: 30,
          left: 30,
          right: 50
        },
        // x轴
        xAxis: {
          name: '防御',
          minorTick: {
            show: true
          },
          minorSplitLine: {
            show: true
          }
        },
        // y轴
        yAxis: {
          name: '秒伤害量',
          minorTick: {
            show: true
          },
          // 辅助线
          minorSplitLine: {
            show: true
          }
        },
        series: [
          {
            // 图表类型
            type: 'line',
            showSymbol: false,
            clip: true,
            data: data
          }
        ]
      }
      this.pre_dam_chart.setOption(option)
      // 自适应
      window.addEventListener('resize', () => { myChart.resize() })
    }
  },
  watch: {
    atk: {
      handler () {
        if (this.isActive) {
          this.preDamageChart()
        }
      }
    },
    atkTime: {
      handler () {
        if (this.isActive) {
          this.preDamageChart()
        }
      }
    },
    isActive: {
      handler () {
        this.preDamageChart()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
// 图表容器
@media only screen and (max-width:599px) {
  .echarts-box {
    width: 100vw;
    height: 75vw;
    margin: 0 auto;
  }
}
@media only screen and (min-width:600px) {
  .echarts-box {
    width: 600px;
    height: 450px;
    margin: 0 auto;
  }
}
</style>
