<template>
  <div>
    <!-- damageClass -->
    <CollapseItem
      :compontentName="'伤害类排名'"
      :layer="5"
    >
      {{ 'DamageClass' }}
    </CollapseItem>
    <!-- damageClass-end -->
    <!-- perDamage-Line-Chart -->
    <CollapseItem
      :compontentName="'秒伤折线图'"
      :layer="5"
    >
      <PerDamage
        :skillParam="skillParam"
        :skillId="skillData.skillId"
        :emParam="emParam"
        :damMod="damMod"
        :atkMod="atkMod"
      />
    </CollapseItem>
  </div>
</template>

<script>
import CollapseItem from '../../../Common/CollapseItem.vue'
import PerDamage from './DamageClass/PerDamage.vue'
import { getSkillParam } from '../../../utils/skillParamCalc.js'

export default {
  props: {
    skillData: Object
  },
  components: {
    CollapseItem,
    PerDamage
  },
  computed: {
    skillParam () {
      const emParam = this.$store.state.em.emParam
      return getSkillParam(emParam, this.skillData, 'dam')
    }
  }
}
</script>

<style>

</style>
