<template>
  <el-container>
    <el-header height="42px">
      <div class="head-name">
        {{ enemy.name }}
      </div>
    </el-header>
    <el-main class="info-main">
      <BaseInfo :enemy-params="enemy" />
      <PerDamage
        :atk="enemy.atk[0]"
        :atk-time="enemy.atkTime"
        :is-active="true"
      />
    </el-main>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
import BaseInfo from './Eninfo/BaseInfo.vue'
import PerDamage from '../Echarts/DamageClass/PerDamage.vue'

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
  props: {
    enemy_name: {
      type: String,
      default: '源石虫'
    }
  },
  components: {
    BaseInfo,
    PerDamage
  },
  methods: {
    // 获取数据
    getEnemyData () {
      this.enemyData = require('@/assets/data/enemydata.json')
    },
    // 查询敌人 （入口）
    findEnemy () {
      for (const en in this.enemyData) {
        if (this.enemyData[en].name === this.enemy_name) {
          this.enemy = this.enemyData[en]
          break
        }
      }
    }
  },
  watch: {
    enemy_name: {
      handler: function () {
        this.findEnemy()
      },
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>
// 页头
.head-name {
  height: 100%;
  font-size: 28px;
  font-style: italic;
  font-weight: bold;
  padding-left: 20px;
  border-bottom: 2px solid #dcdfe6;
}
.info-main {
  padding: 0px 10px;
}
</style>
