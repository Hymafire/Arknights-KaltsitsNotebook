<template>
  <el-container>
    <el-header>
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
    </el-header>
    <el-main>
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
      for (var en in this.enemyData) {
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
/deep/.el-header {
  height: 32px;
  line-height: 32px;
}
.head-name {
  font-size: 30px;
  font-style: italic;
  font-weight: bold;
  padding: 0 0 0 20px;
}
.head-description {
  padding: 10px 0px 0px 0px;
}
// 敌人名称
.head-title {
  font-weight: bold;
}
</style>
