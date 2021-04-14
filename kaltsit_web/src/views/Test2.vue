<template>
  <div id="app">
    <el-aside>
      <el-tree
        :data="employeeList"
        :props="props"
        accordion
        @node-click="handleNodeClick"
        highlight-current>
      </el-tree>
    </el-aside>
    <el-main>
      {{ employee }}
    </el-main>
  </div>
</template>
<script>
export default {
  name: 'App',
  data () {
    return {
      employeeTable: [],
      employeeList: [],
      employeeList1: [],
      employeeList2: [],
      employeeList3: [],
      employeeList4: [],
      employeeList5: [],
      employeeList6: [],
      employee: [],
      total: 0,
      searchname: '红',
      props: {
        name: 'name',
        label: 'name'
      }
    }
  },
  created () {
    this.getemployeeTable()
    this.getemployeeList()
    this.haveemployeeList()
  },
  mounted () {
    this.findemployee()
    // this.handleNodeClick()
  },
  methods: {
    getemployeeTable () {
      const employeeTable = require('../assets/data/employee_table_sim.json')
      this.employeeTable = employeeTable
      this.total = employeeTable.length
      // console.log(employeeTable)
    },
    getemployeeList () {
      var cnt = [0, 0, 0, 0, 0, 0]
      for (var en in this.employeeTable) {
        if (this.employeeTable[en].profession !== 'TRAP' && this.employeeTable[en].profession !== 'TOKEN') {
          if (this.employeeTable[en].rarity === 0) {
            this.employeeList1[cnt[0]] = { name: this.employeeTable[en].name }
            cnt[0]++
          } else if (this.employeeTable[en].rarity === 1) {
            this.employeeList2[cnt[1]] = { name: this.employeeTable[en].name }
            cnt[1]++
          } else if (this.employeeTable[en].rarity === 2) {
            this.employeeList3[cnt[2]] = { name: this.employeeTable[en].name }
            cnt[2]++
          } else if (this.employeeTable[en].rarity === 3) {
            this.employeeList4[cnt[3]] = { name: this.employeeTable[en].name }
            cnt[3]++
          } else if (this.employeeTable[en].rarity === 4) {
            this.employeeList5[cnt[4]] = { name: this.employeeTable[en].name }
            cnt[4]++
          } else if (this.employeeTable[en].rarity === 5) {
            this.employeeList6[cnt[5]] = { name: this.employeeTable[en].name }
            cnt[5]++
          }
        }
        // this.employeeList[cnt] = { name: this.employeeTable[en].profession }
        // cnt++
      }
      // console.log(this.employeeList)
    },
    haveemployeeList () {
      this.employeeList =
      [
        {
          name: '★★★★★★',
          children: this.employeeList6
        },
        {
          name: '★★★★★',
          children: this.employeeList5
        },
        {
          name: '★★★★',
          children: this.employeeList4
        },
        {
          name: '★★★',
          children: this.employeeList3
        },
        {
          name: '★★',
          children: this.employeeList2
        },
        {
          name: '★',
          children: this.employeeList1
        }
      ]
    },
    findemployee () {
      for (var en in this.employeeTable) {
        if (this.employeeTable[en].name === this.searchname) {
          this.employee = this.employeeTable[en]
        }
      }
    },
    handleNodeClick (data) {
      this.searchname = data.name
      console.log(this.searchname)
      this.findemployee()
    }
  }
}
</script>
