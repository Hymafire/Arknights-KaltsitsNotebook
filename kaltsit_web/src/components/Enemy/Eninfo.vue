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
        最大血量：{{ enemy.maxHp[0] }}
      </div>
      <div class="enemy-style">
        攻击：{{ enemy.atk[0] }}
      </div>
      <div class="enemy-style">
        防御：{{ enemy.def[0] }}
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
    </el-card>
  </el-container>
</template>

<script>
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
  updated () {
    this.findEnemy()
  },
  props: {
    enemy_name: String
  },
  methods: {
    getEnemyData () {
      const enemyData = require('@/assets/data/enemydata.json')
      this.enemyData = enemyData
    },
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
.head-title {
  font-weight: bold;
}
.enemy-style {
  padding: 3px
}
</style>
