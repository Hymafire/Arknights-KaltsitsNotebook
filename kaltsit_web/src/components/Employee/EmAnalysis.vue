<template>
  <div id="em-analysis">
    <!-- 1.totalRank -->
    <CollapseItem :compontentName="'总排名'">
      <TotalRank />
    </CollapseItem>
    <!-- totalRank-end -->
    <!-- 2.damageClass -->
    <CollapseItem :compontentName="'攻击类'">
      <DamageClass :emParam="emParam" />
    </CollapseItem>
    <!-- damageClass-end -->
    <!-- 5.skillClass -->
    <CollapseItem :compontentName="'技能分析'">
      <SkillClass
        :emParam="emParam"
        :skillsLevel="skillsLevel"
        :skillsFlag="skillsFlag"
      />
    </CollapseItem>
    <!-- skillClass-end -->
  </div>
</template>

<script>
import CollapseItem from '../Common/CollapseItem.vue'
import TotalRank from '../Employee/EmAnalysis/TotalRank.vue'
import DamageClass from './EmAnalysis/DamageClass.vue'
import SkillClass from './EmAnalysis/SkillClass.vue'

export default {
  name: 'EmAnalysis',
  props: {
    emParam: Object,
    skillsLevel: Array,
    skillsFlag: Array
  },
  components: {
    CollapseItem,
    TotalRank,
    DamageClass,
    SkillClass
  }
}
</script>

<style>

</style>
