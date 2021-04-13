<template>
  <el-container class="home-container">
    <!--  敌方列表和查询区 -->
    <el-aside width="220px" class="home-aside" >
      <div>
        <el-input prefix-icon="el-icon-user" placeholder="输入敌方名称" class="search-input">
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </div>
      <div>
        <!-- <el-tree :props="props" :load="loadNode" lazy></el-tree> -->
        <el-tree :data="enemyList" :props="props" @node-click="handleNodeClick" highlight-current></el-tree>
      </div>
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <el-row :gutter="10" type="flex">
            <el-col :span="6">
              <span class="head-name">{{ enemy.enemyData.name.m_value }}</span>
            </el-col>
            <el-col :span="18" class="head-description">
              <span class="head-title">描述：</span>
              <span>{{ enemy.enemyData.description.m_value }}</span>
            </el-col>
          </el-row>
        </div>
        <div class="enemy-style">
          最大血量：{{ enemy.enemyData.attributes.maxHp.m_value }}
        </div>
        <div class="enemy-style">
          攻击：{{ enemy.enemyData.attributes.atk.m_value }}
        </div>
        <div class="enemy-style">
          防御：{{ enemy.enemyData.attributes.def.m_value }}
        </div>
        <div class="enemy-style">
          法抗：{{ enemy.enemyData.attributes.magicResistance.m_value }}
        </div>
        <div class="enemy-style">
          移速：{{ enemy.enemyData.attributes.moveSpeed.m_value }}
        </div>
        <div class="enemy-style">
          攻击间隔：{{ enemy.enemyData.attributes.baseAttackTime.m_value }}s
        </div>
        <div class="enemy-style">
          生命回复：{{ enemy.enemyData.attributes.hpRecoveryPerSec.m_value }}/s
        </div>
        <div class="enemy-style">
          重量：{{ enemy.enemyData.attributes.massLevel.m_value }}
        </div>
        <div class="enemy-style">
          射程：{{ enemy.enemyData.rangeRadius.m_value }}
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
      enemyTable: [],
      enemyList: [],
      enemy: [],
      total: 0,
      searchName: '源石虫'
    }
  },
  created () {
    this.getEnemyTable()
    this.getEnemyList()
  },
  mounted () {
    this.findEnemy()
  },
  methods: {
    // 获取敌方数据
    getEnemyTable () {
      const enemyTable = require('../assets/data/enemy_table.json')
      this.enemyTable = enemyTable
      this.total = enemyTable.length
    },
    // 获取敌方名单
    getEnemyList () {
      for (var i = 0; i < this.total; i++) {
        this.enemyList[i] = { name: this.enemyTable[i].Value[0].enemyData.name.m_value }
      }
      console.log(this.enemyList)
    },
    // 获取目标敌人数据
    findEnemy () {
      for (var i = 0; i < this.total; i++) {
        if (this.enemyTable[i].Value[0].enemyData.name.m_value === this.searchName) {
          this.enemy = this.enemyTable[i].Value[0]
          break
        }
      }
    },
    //
    loadNode (node, resolve) {
      if (node.level === 0) {
        return resolve(this.enemyList)
      }

      if (node.level === 1) {
        return ([])
      }

      setTimeout(() => {
        const data = []
        resolve(data)
      }, 500)
    }
  }
}
</script>

<style lang="scss" scoped>
.home-container {
  height: 92%;
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
</style>
