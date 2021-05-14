<template>
  <div
    id="rank-radar"
    class="echarts-box"
  />
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  name: 'RankRadar',
  props: {
    name: String
    // rankTable: Array
  },
  mounted () {
    this.rankRadarChart()
  },
  methods: {
    rankRadarChart () {
      const data = [100, 100, 100, 100, 100]
      //
      const myChart = echarts.getInstanceByDom(document.getElementById('rank-radar'))
      if (myChart == null) {
        this.rank_radar = echarts.init(document.getElementById('rank-radar'))
      }
      //
      const option = {
        title: {
          text: '能力评分图'
        },
        radar: {
          name: {
          },
          indicator: [
            { name: '最大生命力', max: 200 },
            { name: '攻击力', max: 200 },
            { name: '防御力', max: 200 },
            { name: '法抗', max: 200 },
            { name: '攻击速度', max: 200 }
            // { name: '攻击范围', max: 5 },
          ]
        },
        series: [
          {
            name: 'rank_radar',
            type: 'radar',
            data: data
          }
        ]
      }
      this.rank_radar.setOption(option)
      window.addEventListener('resize', () => { myChart.resize() })
    }
  },
  watch: {
    name: {
      handler () {
        this.rankRadarChart()
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
