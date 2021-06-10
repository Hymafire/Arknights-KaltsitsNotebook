<template>
  <div id="damage-class">
    <!-- damageBar -->
    <CollapseItem
      :compontentName="'伤害类对比'"
      :layer="2"
    >
      <DamageBar
        :key="this.$store.state.em.emKey"
      />
    </CollapseItem>
    <!-- damageBar-end -->
    <!-- perdamage -->
    <CollapseItem
      :compontentName="'秒伤害量'"
      :layer="2"
    >
      <PerDamage />
    </CollapseItem>
    <!-- perDamage-end -->
  </div>
</template>

<script>
import CollapseItem from '../../Common/CollapseItem.vue'
import PerDamage from '../EmAnalysis/DamageClass/PerDamage.vue'
import DamageBar from '../EmAnalysis/DamageClass/DamageBar.vue'
// import RankRadar from '../../Echarts/RankClass/RankRadar.vue'

export default {
  name: 'DamageClass',
  components: {
    CollapseItem,
    PerDamage,
    DamageBar
    // RankRadar
  },
  computed: {
    isEmUpdate () {
      return this.$store.state.isEmUpdate
    }
  },
  watch: {
    isEmUpdate: {
      handler () {
        this.$forceUpdate()
      }
    }
  }
}
</script>

<style>

</style>
