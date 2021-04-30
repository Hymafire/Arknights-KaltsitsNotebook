<template>
  <el-container class="info-container">
    <el-header class="info-header">
      <el-card>
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
      </el-card>
    </el-header>
    <el-main class="info-main">
      <el-card class="box-card">
        <div>
          <span>最大血量：</span> {{ enemy.maxHp[0] }}
        </div>
        <div>
          <span>攻击：</span> {{ enemy.atk[0] }}
        </div>
        <div>
          <span>防御：</span> {{ enemy.def[0] }}
        </div>
        <div>
          <span>法抗：</span> {{ enemy.magRes[0] }}
        </div>
        <div>
          <span>移速：</span> {{ enemy.moveSpd }}
        </div>
        <div>
          <span>攻击间隔：</span> {{ enemy.atkTime }}s
        </div>
        <div>
          <span>生命回复：</span> {{ enemy.hpRec }}/s
        </div>
        <div>
          <span>重量：</span> {{ enemy.massLevel }}
        </div>
        <div>
          <span>射程：</span> {{ enemy.rangeRadius }}
        </div>
      </el-card>

      <!-- 秒伤表 -->

      <el-card class="card-box">
        <div
          id="pre-damage"
          class="echarts-box"
        />
      </el-card>
    </el-main>
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
.info-header {
  padding: 0px;
}
// 属性盒子
.box-card {
  height: 100%;
  width: 100%;
  // 各属性间距
  div {
    padding: 3px;
    // 属性标题
    span {
      font-weight: 700;
      background-color: rgba(172, 255, 47, 0.6);
    }
  }
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
// 图表容器
.echarts-box {
  width: 600px;
  height: 400px;
}
</style>
