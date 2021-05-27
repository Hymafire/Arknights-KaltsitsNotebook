<template>
  <div id="em-analysis">
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
          <RankRadar
            :name="employeeName"
            :dataList="rankData"
            :indicatorList="tagList"
            :isActive="isActive('totalRank')"
          />
        </div>
      </el-collapse-transition>
    </div>
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
          />
        </div>
      </el-collapse-transition>
    </div>
  </div>
</template>

<script>
import DamageClass from './EmAnalysis/DamageClass.vue'
import RankRadar from '../Echarts/RankClass/RankRadar.vue'

export default {
  name: 'EmAnalysis',
  data () {
    return {
      pretreatedData: [],
      employeeNum: Number,
      tagList: [],
      activeName: []
    }
  },
  created () {
    this.getPertreated()
    this.countEmployee()
    this.createTagList()
  },
  props: {
    employeeData: Object,
    employeeKey: String,
    emParam: Array
  },
  components: {
    DamageClass,
    RankRadar
  },
  computed: {
    // 数值排名
    rankData: function () {
      const employee = this.employeeData[this.employeeKey].phases
      const emLen = employee.atk.length - 1
      const rankData = [0, 0, 0, 0, 0]
      for (const Em in this.employeeData) {
        const compareEm = this.employeeData[Em].phases
        if (employee.atk[emLen][1] >= compareEm.atk[compareEm.atk.length - 1][1]) {
          rankData[0]++
        }
        if (employee.atkTime <= compareEm.atkTime) {
          rankData[1]++
        }
        if (employee.maxHp[emLen][1] >= compareEm.maxHp[compareEm.maxHp.length - 1][1]) {
          rankData[2]++
        }
        if (employee.def[emLen][1] >= compareEm.def[compareEm.def.length - 1][1]) {
          rankData[3]++
        }
        if (employee.magRes[emLen] >= compareEm.magRes[compareEm.magRes.length - 1]) {
          rankData[4]++
        }
      }
      return rankData
    },
    employeeName: function () {
      return this.$store.state.employeeName
    }
  },
  methods: {
    getPertreated () {
      this.pretreatedData = require('../../assets/data/pretreated.json')
    },
    countEmployee () {
      this.employeeNum = Object.keys(this.employeeData).length
    },
    createTagList () {
      const tagList = []
      tagList.push({ name: '攻击力', max: this.employeeNum })
      tagList.push({ name: '攻击间隔', max: this.employeeNum })
      tagList.push({ name: '最大生命值', max: this.employeeNum })
      tagList.push({ name: '防御力', max: this.employeeNum })
      tagList.push({ name: '法术抗性', max: this.employeeNum })
      this.tagList = tagList
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

<style lang="scss" scoped>

</style>
