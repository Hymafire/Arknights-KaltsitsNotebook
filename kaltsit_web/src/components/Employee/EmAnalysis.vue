<template>
  <div id="em-analysis">
    <!-- 1.totalRank -->
    <CollapseItem :compontentName="'总排名'">
      <TotalRank />
    </CollapseItem>
    <!-- 2.damageClass -->
    <CollapseItem
      :compontentName="'攻击类'"
      v-if="!($store.state.em.emData.profession === 'MEDIC' || $store.state.em.emPretData === 'NoAtk')"
    >
      <DamageClass />
    </CollapseItem>
    <!-- 3.surviveClass -->
    <CollapseItem :compontentName="'生存类'">
      <SurvivalClass />
    </CollapseItem>
    <!-- 5.skillClass -->
    <CollapseItem :compontentName="'技能分析'">
      <SkillClass />
    </CollapseItem>
  </div>
</template>

<script>
import CollapseItem from '../Common/CollapseItem.vue'
import TotalRank from '../Employee/EmAnalysis/TotalRank.vue'
import DamageClass from './EmAnalysis/DamageClass.vue'
import SkillClass from './EmAnalysis/SkillClass.vue'
import SurvivalClass from './EmAnalysis/SurvivalClass.vue'

export default {
  components: {
    CollapseItem,
    TotalRank,
    DamageClass,
    SkillClass,
    SurvivalClass
  }
}
</script>

<style>

</style>
