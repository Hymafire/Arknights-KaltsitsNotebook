<template>
  <div>Test</div>
</template>

<script>
import { emDataPretreate } from '../components/utils/pretreatedCalc.js'

export default {
  created () {
    this.testUtils()
  },
  methods: {
    testUtils () {
      const employeeData = require('@/assets/data/employeedata.json')
      console.log(emDataPretreate(employeeData))
    }
  }
}
</script>

<style>

</style>
