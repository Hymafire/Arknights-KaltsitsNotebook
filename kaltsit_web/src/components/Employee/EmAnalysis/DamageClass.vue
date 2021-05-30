<template>
  <div id="damage-class">
    <div id="damageRank">
      <div class="class-collapse-title">
        <span>- 伤害类排名</span>
        <button
          @click="changeActive('damageRank')"
          :class="{'el-icon-arrow-right': !isActive('damageRank'), 'el-icon-arrow-down': isActive('damageRank')}"
        />
      </div>
      <el-collapse-transition>
        <div v-if="isActive('damageRank')">
          DamageClass
        </div>
      </el-collapse-transition>
    </div>
    <div id="damageBar">
      <div class="class-collapse-title">
        <span>- 伤害类对比</span>
        <button
          @click="changeActive('damageBar')"
          :class="{'el-icon-arrow-right': !isActive('damageBar'), 'el-icon-arrow-down': isActive('damageBar')}"
        />
      </div>
      <el-collapse-transition>
        <div v-if="isActive('damageBar')">
          <DamageBar
            :key="this.$store.state.employeeKey"
            :atk="emParam.atk"
            :atkTime="emParam.atkTime"
          />
        </div>
      </el-collapse-transition>
    </div>
    <div id="perDamage">
      <div class="class-collapse-title">
        <span>- 秒伤害量</span>
        <button
          @click="changeActive('perDamage')"
          :class="{'el-icon-arrow-right': !isActive('perDamage'), 'el-icon-arrow-down': isActive('perDamage')}"
        />
      </div>
      <el-collapse-transition>
        <div v-if="isActive('perDamage')">
          <PerDamage
            :atk="emParam.atk"
            :atkTime="emParam.atkTime"
            :baseAtkTime="emParam.baseAtkTime"
            :atkMod="atkMod"
            :damMod="damMod"
          />
        </div>
      </el-collapse-transition>
    </div>
    <div id="totalDamage">
      <div class="class-collapse-title">
        <span>- 总伤害量</span>
        <button
          @click="changeActive('totalDamage')"
          :class="{'el-icon-arrow-right': !isActive('totalDamage'), 'el-icon-arrow-down': isActive('totalDamage')}"
        />
      </div>
      <el-collapse-transition>
        <div v-if="isActive('totalDamage')">
          <DamageTotal
            :avgDef="pretreated.enAvgDef"
            :atk="emParam.atk"
            :atkTime="emParam.atkTime"
            :isActive="true"
          />
        </div>
      </el-collapse-transition>
    </div>
  </div>
</template>

<script>
import DamageTotal from '../../Echarts/DamageClass/DamageTotal.vue'
import { damModJudge, atkModJudge } from '../../utils/damageCalc.js'
import PerDamage from '../EmAnalysis/DamageClass/PerDamage.vue'
import DamageBar from '../EmAnalysis/DamageClass/DamageBar.vue'
// import PerDamage from '../../Echarts/DamageClass/PerDamage.vue'
// import RankRadar from '../../Echarts/RankClass/RankRadar.vue'

export default {
  name: 'DamageClass',
  data () {
    return {
      activeName: []
    }
  },
  props: {
    emParam: Array
  },
  components: {
    DamageTotal,
    PerDamage,
    DamageBar
    // RankRadar
  },
  computed: {
    changed: function () {
      return this.$store.state.isEmParamsUpdate
    },
    damMod: function () {
      return damModJudge(this.$store.state.employeeData[this.$store.state.employeeKey].description)
    },
    atkMod: function () {
      return atkModJudge(this.$store.state.employeeData[this.$store.state.employeeKey].description)
    }
  },
  methods: {
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
  },
  watch: {
    changed: {
      handler () {
        this.$forceUpdate()
      },
      immediate: true
    }
  }
}
</script>

<style lang="scss" scroped>

</style>
