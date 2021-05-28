<template>
  <div id="em-analysis">
    <!-- totalRank -->
    <div id="totalRank" class="collapse-box">
      <div class="collapse-title">
        <span>总排名</span>
        <button
          @click="changeActive('totalRank')"
          :class="{'el-icon-arrow-right': !isActive('totalRank'), 'el-icon-arrow-down': isActive('totalRank')}"
        />
      </div>
      <el-collapse-transition>
        <div v-if="isActive('totalRank')">
          <TotalRank
            :employeeData="employeeData"
            :employeeKey="employeeKey"
          />
        </div>
      </el-collapse-transition>
    </div>
    <!-- totalRank-end -->
    <!-- damageClass -->
    <div id="damageClass" class="collapse-box">
      <div class="collapse-title">
        <span>攻击类</span>
        <button
          @click="changeActive('damageClass')"
          :class="{'el-icon-arrow-right': !isActive('damageClass'), 'el-icon-arrow-down': isActive('damageClass')}"
        />
      </div>
      <el-collapse-transition>
        <div v-if="isActive('damageClass')">
          <DamageClass
            :emParam="emParam"
            :pretreated="pretreatedData"
            :description="employeeData[employeeKey].description"
          />
        </div>
      </el-collapse-transition>
    </div>
    <!-- damageClass-end -->
  </div>
</template>

<script>
import DamageClass from './EmAnalysis/DamageClass.vue'
import TotalRank from '../Employee/EmAnalysis/TotalRank.vue'

export default {
  name: 'EmAnalysis',
  data () {
    return {
      pretreatedData: [],
      activeName: []
    }
  },
  created () {
    this.getPertreated()
  },
  props: {
    employeeData: Object,
    employeeKey: String,
    emParam: Array
  },
  components: {
    DamageClass,
    TotalRank
  },
  methods: {
    getPertreated () {
      this.pretreatedData = require('../../assets/data/pretreated.json')
    },
    // 判断折叠面板是否处于激活状态
    isActive (name) {
      for (let i = 0; i < this.activeName.length; i++) {
        if (name === this.activeName[i]) {
          return true
        }
      }
      return false
    },
    changeActive (name) {
      const index = this.activeName.indexOf(name)
      if (index === -1) {
        this.activeName.push(name)
      } else {
        this.activeName.splice(index, 1)
      }
    }
  }
}
</script>

<style>

</style>
