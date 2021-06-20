<template>
  <div id="range-show">
    <div class="range-chart-container">
      <div v-for="row in rowRange" :key="row" class="range-row">
        <div v-for="col in colRange" :key="col" class="range-box-style" :class="getColorClass(col, row)" :style="blockSize" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RangeShow',
  data () {
    return {
      rangeTable: Object,
      colRange: Array,
      rowRange: Array
    }
  },
  computed: {
    rangeId () {
      return this.$store.state.em.emData.phases.range[this.$store.state.em.emInputParam.elite]
    },
    blockSize () {
      const maxDiff = Math.max(this.colRange.length, this.rowRange.length)
      const styleObj = {
        // width: 设定宽度，用于处理部分浏览器兼容问题
        width: Math.min(70 / maxDiff, 24) + '%',
        padding: Math.min(35 / maxDiff, 12) + '%',
        margin: 6 / (maxDiff + 1) + '%'
      }
      return styleObj
    }
  },
  created () {
    this.getRangeTable()
    this.getRangeData()
  },
  methods: {
    getRangeTable () {
      this.rangeTable = require('../../../assets/data/range_table.json')
    },
    getRangeData () {
      const colrange = [0, 0]
      const rowrange = [0, 0]
      const gridsList = this.rangeTable[this.rangeId].grids
      for (const pos in gridsList) {
        colrange[0] = Math.min(gridsList[pos].col, colrange[0])
        colrange[1] = Math.max(gridsList[pos].col, colrange[1])
        rowrange[0] = Math.min(gridsList[pos].row, rowrange[0])
        rowrange[1] = Math.max(gridsList[pos].row, rowrange[1])
      }
      this.colRange = this.RangeList(colrange[0], colrange[1])
      this.rowRange = this.RangeList(rowrange[0], rowrange[1])
    },
    RangeList (min, max) {
      const List = []
      for (let i = min; i <= max; i++) {
        List.push(i)
      }
      return List
    },
    getColorClass (col, row) {
      if (col === 0 && row === 0) {
        return 'base-position'
      } else if (this.isInList(col, row)) {
        return 'atk-range'
      } else {
        return 'blank-range'
      }
    },
    isInList (col, row) {
      const gridsList = this.rangeTable[this.rangeId].grids
      for (const pos in gridsList) {
        if (col === gridsList[pos].col && row === gridsList[pos].row) {
          return true
        }
      }
      return false
    }
  },
  watch: {
    rangeId: {
      handler () {
        this.getRangeData()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
#range-show {
  min-width: 140px;
  max-width: 200px;
  width: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
}
.range-chart-container {
  width: 100%;
  height: 100%;
  padding-left: 2px;
  padding-right: 5px;
  box-sizing: border-box;
}
.range-row {
  display: flex;
  justify-content: center;
  flex-wrap: nowrap;
  width: 100%;
}
.range-box-style {
  // display: inline-block;
  box-sizing: border-box;
  // -webkit-box-sizing: border-box;
}
.base-position {
  border: 3px solid darkgrey;
  background-color: gray;
}
.atk-range {
  border: 3px solid #ddd;
  background-color: #fdfdfd;
}
.blank-range {
  border: 3px solid transparent;
  background-color: transparent;
}
</style>
