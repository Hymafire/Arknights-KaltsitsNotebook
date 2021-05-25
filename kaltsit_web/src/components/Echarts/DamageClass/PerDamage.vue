<template>
  <div
    id="per-damage"
    class="echarts-box"
  />
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'
import damageCalc from '../../utils/damageCalc.js'

export default {
  name: 'PerDamage',
  props: {
    atk: Number,
    atkTime: Number,
    damMod: {
      type: String,
      default: 'Phy'
    },
    atkMod: {
      type: String,
      default: '0'
    },
    isActive: {
      type: Boolean,
      default: false
    }
  },
  mounted () {
    this.perDamageChart()
  },
  methods: {
    perDamageChart () {
      // 数据
      const data = damageCalc.perDamage(this.atk, this.atkTime, this.damMod, this.atkMod)
      // 初始化DOM
      const myChart = echarts.getInstanceByDom(document.getElementById('per-damage'))
      if (myChart == null) {
        this.per_dam_chart = echarts.init(document.getElementById('per-damage'))
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
          top: 10,
          // buttom 参数设置有问题（？？？） 替换成 y2
          y2: 30,
          left: 30,
          right: 40
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
      this.per_dam_chart.setOption(option)
      // 自适应
      if (this.isActive) {
        window.addEventListener('resize', () => { myChart.resize() })
      }
    }
  },
  watch: {
    atk: {
      handler () {
        if (this.isActive) {
          this.perDamageChart()
        }
      }
    },
    atkTime: {
      handler () {
        if (this.isActive) {
          this.perDamageChart()
        }
      }
    },
    isActive: {
      handler () {
        this.perDamageChart()
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
