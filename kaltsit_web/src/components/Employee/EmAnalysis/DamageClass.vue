<template>
  <div id="damage-class">
    <!-- damageClass -->
    <CollapseItem
      :compontentName="'伤害类排名'"
      :isChild="true"
    >
      {{ 'DamageClass' }}
    </CollapseItem>
    <!-- damageClass-end -->
    <!-- damageBar -->
    <CollapseItem
      :compontentName="'伤害类对比'"
      :isChild="true"
    >
      <DamageBar
        :key="this.$store.state.employeeKey"
        :atk="emParam.atk"
        :atkTime="emParam.atkTime"
      />
    </CollapseItem>
    <!-- damageBar-end -->
    <!-- perdamage -->
    <CollapseItem
      :compontentName="'秒伤害量'"
      :isChild="true"
    >
      <PerDamage
        :atk="emParam.atk"
        :atkTime="emParam.atkTime"
        :baseAtkTime="emParam.baseAtkTime"
        :atkMod="atkMod"
        :damMod="damMod"
      />
    </CollapseItem>
    <!-- perDamage-end -->
  </div>
</template>

<script>
import CollapseItem from '../../Common/CollapseItem.vue'
import { damModJudge, atkModJudge } from '../../utils/damageCalc.js'
import PerDamage from '../EmAnalysis/DamageClass/PerDamage.vue'
import DamageBar from '../EmAnalysis/DamageClass/DamageBar.vue'
// import RankRadar from '../../Echarts/RankClass/RankRadar.vue'

export default {
  name: 'DamageClass',
  props: {
    emParam: Object
  },
  components: {
    CollapseItem,
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

<style>

</style>
