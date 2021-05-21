<template>
  <el-container>
    <el-header height="42px">
      <div class="head-name">
        {{ enemy.name }}
      </div>
    </el-header>
    <el-main class="info-main">
      <BaseInfo :enemy="enemy" :enemyKey="enemy.Key"/>
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
      enemyData: []
    }
  },
  created () {
    this.getEnemyData()
  },
  components: {
    BaseInfo,
    PerDamage
  },
  computed: {
    enemy: function () {
      for (const en in this.enemyData) {
        if (this.enemyData[en].name === this.$store.state.enemyName) {
          return this.enemyData[en]
        }
      }
      return []
    }
  },
  methods: {
    // 获取数据
    getEnemyData () {
      this.enemyData = require('@/assets/data/enemydata.json')
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
