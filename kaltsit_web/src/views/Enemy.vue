<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="220px" class="home-aside" >
      <el-input prefix-icon="el-icon-user" placeholder="输入敌方名称" class="search-input">
        <el-button slot="append" icon="el-icon-search"></el-button>
      </el-input>
      <el-tree :props="props" :load="loadNode" lazy></el-tree>
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>{{ enemyList.Value[0].enemyData.name.m_value }}</span>
        </div>
        <div class="enemy-style">
          描述：{{ enemyList.Value[0].enemyData.description.m_value }}
        </div>
        <div class="enemy-style">
          最大血量：{{ enemyList.Value[0].enemyData.attributes.maxHp.m_value }}
        </div>
        <div class="enemy-style">
          攻击：{{ enemyList.Value[0].enemyData.attributes.atk.m_value }}
        </div>
        <div class="enemy-style">
          防御：{{ enemyList.Value[0].enemyData.attributes.def.m_value }}
        </div>
        <div class="enemy-style">
          法抗：{{ enemyList.Value[0].enemyData.attributes.magicResistance.m_value }}
        </div>
        <div class="enemy-style">
          移速：{{ enemyList.Value[0].enemyData.attributes.moveSpeed.m_value }}
        </div>
        <div class="enemy-style">
          攻击间隔：{{ enemyList.Value[0].enemyData.attributes.baseAttackTime.m_value }}s
        </div>
        <div class="enemy-style">
          生命回复：{{ enemyList.Value[0].enemyData.attributes.hpRecoveryPerSec.m_value }}/s
        </div>
        <div class="enemy-style">
          重量：{{ enemyList.Value[0].enemyData.attributes.massLevel.m_value }}
        </div>
        <div class="enemy-style">
          射程：{{ enemyList.Value[0].enemyData.rangeRadius.m_value }}
        </div>
      </el-card>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      props: {
        label: 'name',
        children: 'zones',
        idLeaf: 'leaf'
      },
      enemyList: [],
      total: 0
    }
  },
  created () {
    this.getEnemyList()
  },
  methods: {
    getEnemyList () {
      const enemyList = require('../static/enemy_table.json')
      this.enemyList = enemyList[0]
      this.total = enemyList.length
    },
    loadNode (node, resolve) {
      if (node.level === 0) {
        return resolve([{ name: '敌方列表' }])
      }
      if (node.level > 1) return resolve([])

      setTimeout(() => {
        const data = [{
          name: 'leaf',
          leaf: true
        }, {
          name: 'zone'
        }]

        resolve(data)
      }, 500)
    }
  }
}
</script>

<style lang="scss" scoped>
.home-container {
  height: 100%;
}
.el-aside {
  background-color: #fff;
  margin: 10px;
}
.el-main {
  background-color: #eaedf1;
}
.search-input {
  margin: 5px 0px;
}
.enemy-style {
  padding: 3px;
}
</style>
