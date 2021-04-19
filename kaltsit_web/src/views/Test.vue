<template>
  <div id="app">
    <div>{{ enemyList }}</div>
  </div>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      enemyTable: [],
      enemyList: [],
      enemy: [],
      total: 0,
      searchName: '源石虫'
    }
  },
  created () {
    // this.getEnemyTable()
    // this.getEnemyList()
    // this.getEnemyList2()
    this.getEnemyList3()
    this.findEnemy()
  },
  methods: {
    getEnemyList3 () {
      const enemyList = require('@/assets/data/enemylist.json')
      this.enemyList = enemyList
    },
    getEnemyTable () {
      const enemyTable = require('../assets/data/enemy_table.json')
      this.enemyTable = enemyTable
      this.total = enemyTable.length
      console.log(enemyTable)
    },
    getEnemyList () {
      for (var i = 0; i < this.total; i++) {
        this.enemyList[i] = this.enemyTable[i].Value[0].enemyData.name.m_value
      }
      console.log(this.enemyList)
    },
    getEnemyList2 () {
      for (var i = 0; i < this.total; i++) {
        this.enemyList[i] = { name: this.enemyTable[i].Value[0].enemyData.name.m_value }
      }
      console.log(this.enemyList)
    },
    findEnemy () {
      for (var i = 0; i < this.total; i++) {
        if (this.enemyTable[i].Value[0].enemyData.name.m_value === this.searchName) {
          this.enemy = this.enemyTable[i].Value[0]
          break
        }
      }
    }
  }
}
</script>
