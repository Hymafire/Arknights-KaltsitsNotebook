<template>
  <el-card>
    <div
      id="damage-total"
      class="echarts-box"
    />
  </el-card>
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  name: 'DamageTotal',
  props: {
    avgDef: Array,
    atk: Number,
    atkTime: Number,
    isActive: {
      type: Boolean,
      default: false
    }
  },
  mounted () {
    this.damageTotalChart()
  },
  methods: {
    damageTotalChart () {
      const data = [[], [], [], []]
      const def_list = this.avgDef
      for (let time = 0; time <= 30; time++) {
        for (let i = 0; i < 4; i++) {
          const damage = Math.max(this.atk - def_list[i], this.atk * 0.05)
          const pre_dam = damage / this.atkTime
          const total_dam = pre_dam * time
          data[i].push([time, total_dam])
        }
      }
      // 初始化DOM
      const myChart = echarts.getInstanceByDom(document.getElementById('damage-total'))
      if (myChart == null) {
        this.pre_dam_time_chart = echarts.init(document.getElementById('damage-total'))
      }
      // 配置内容
      const option = {
        animation: false,
        title: {
          left: '20%',
          text: '伤害量-时间'
        },
        legend: {
          left: '40%',
          data: ['Avg', 'NORMAL', 'ELITE', 'BOSS']
        },
        grid: {
          top: 40,
          left: 50,
          right: 40,
          buttom: 50
        },
        xAxis: {
          name: '时间',
          minorTick: {
            show: true
          },
          minorSplitLine: {
            show: true
          }
        },
        yAxis: {
          name: '伤害量',
          minorTick: {
            show: true
          },
          minorSplitLine: {
            show: true
          }
        },
        series: [
          {
            name: 'Avg',
            type: 'line',
            showSymbol: false,
            clip: true,
            data: data[0]
          },
          {
            name: 'NORMAL',
            type: 'line',
            showSymbol: false,
            clip: true,
            data: data[1]
          },
          {
            name: 'ELITE',
            type: 'line',
            showSymbol: false,
            clip: true,
            data: data[2]
          },
          {
            name: 'BOSS',
            type: 'line',
            showSymbol: false,
            clip: true,
            data: data[3]
          }
        ]
      }
      this.pre_dam_time_chart.setOption(option)
    }
  },
  watch: {
    atk: {
      handler () {
        if (this.isActive) {
          this.damageTotalChart()
        }
      },
      immediate: true
    },
    atkTime: {
      handler () {
        if (this.isActive) {
          this.damageTotalChart()
        }
      },
      immediate: true
    },
    isActive: {
      handler () {
        this.damageTotalChart()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.echarts-box {
  width: 600px;
  height: 400px;
  margin: 0 auto;
}
</style>
