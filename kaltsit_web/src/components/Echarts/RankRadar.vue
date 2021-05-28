<template>
  <div id="rank-radar" class="echarts-box" />
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  name: 'RankRadar',
  props: {
    name: String,
    dataList: Array,
    indicatorList: Array,
    isActive: {
      type: Boolean,
      default: false
    }
  },
  mounted () {
    this.rankRadarChart()
  },
  methods: {
    rankRadarChart () {
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
          indicator: this.indicatorList
        },
        series: [
          {
            name: 'rank_radar',
            type: 'radar',
            data: [
              {
                value: this.dataList,
                label: {
                  show: true,
                  formatter: function (params) {
                    return params.value
                  }
                }
              }
            ]
          }
        ]
      }
      this.rank_radar.setOption(option)
      if (this.isActive) {
        window.addEventListener('resize', () => { myChart.resize() })
      }
    }
  },
  watch: {
    name: {
      handler () {
        this.rankRadarChart()
      },
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
