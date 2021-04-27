<template>
  <el-container class="info-container">
    <el-card class="box-card">
      <div
        slot="header"
        class="clearfix"
      >
        <el-row
          :gutter="10"
          type="flex"
        >
          <el-col :span="6">
            <span class="head-name">{{ enemy.name }}</span>
          </el-col>
          <el-col
            :span="18"
            class="head-description"
          >
            <span class="head-title">描述：</span>
            <span>{{ enemy.description }}</span>
          </el-col>
        </el-row>
      </div>
      <div class="enemy-style">
        <span class="param-title">最大血量：</span>
        <span>{{ enemy.maxHp[0] }}</span>
      </div>
      <div class="enemy-style">
        <span class="param-title">攻击：</span>
        <span>{{ enemy.atk[0] }}</span>
      </div>
      <div class="enemy-style">
        <span class="param-title">防御：</span>
        <span>{{ enemy.def[0] }}</span>
      </div>
      <div class="enemy-style">
        法抗：{{ enemy.magRes[0] }}
      </div>
      <div class="enemy-style">
        移速：{{ enemy.moveSpd }}
      </div>
      <div class="enemy-style">
        攻击间隔：{{ enemy.atkTime }}s
      </div>
      <div class="enemy-style">
        生命回复：{{ enemy.hpRec }}/s
      </div>
      <div class="enemy-style">
        重量：{{ enemy.massLevel }}
      </div>
      <div class="enemy-style">
        射程：{{ enemy.rangeRadius }}
      </div>
      <hr>
      <!-- 秒伤表 -->
      <div id="pre-damage" class="echarts-box" />
    </el-card>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
import * as echarts from 'echarts'

export default {
  data () {
    return {
      enemyData: [],
      enemy: []
    }
  },
  created () {
    this.getEnemyData()
    this.findEnemy()
  },
  mounted () {
    this.getCharts()
  },
  props: {
    enemy_name: String
  },
  methods: {
    // 获取数据
    getEnemyData () {
      this.enemyData = require('@/assets/data/enemydata.json')
    },
    // 查询敌人 （入口）
    findEnemy () {
      for (var en in this.enemyData) {
        if (this.enemyData[en].name === this.enemy_name) {
          this.enemy = this.enemyData[en]
          break
        }
      }
    },
    // 绘图函数区 =========================================
    // 总函数
    getCharts () {
      this.preDamageChart()
    },
    // 秒伤-predamage
    preDamageChart () {
      // 数据
      const data = []
      for (let def = 0; def <= 800; def++) {
        const damage = Math.max(this.enemy.atk[0] - def, this.enemy.atk[0] * 0.05)
        const pre_dam = damage / this.enemy.atkTime
        data.push([def, pre_dam])
      }
      // 初始化DOM
      this.pre_dam_chart = echarts.init(document.getElementById('pre-damage'))
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
          top: 40,
          left: 50,
          right: 40,
          buttom: 50
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
    },
    // 单次伤害-hitdamage
    hitDamageChart () {
    }
  },
  watch: {
    enemy_name: {
      handler: function () {
        this.findEnemy()
        this.getCharts()
      },
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>
.info-container {
  height: 100%;
}
.box-card {
  height: 100%;
  width: 100%;
}
// 页头
.head-name {
  font-size: 30px;
  font-style: italic;
  font-weight: bold;
  padding: 0 0 0 15px;
}
.head-description {
  padding: 10px 0px 0px 0px;
}
// 敌人名称
.head-title {
  font-weight: bold;
}
// 属性标题
.param-title {
  font-weight: bold;
}
.enemy-style {
  padding: 3px
}
// 图表容器
.echarts-box {
  width: 600px;
  height: 400px;
}
</style>
