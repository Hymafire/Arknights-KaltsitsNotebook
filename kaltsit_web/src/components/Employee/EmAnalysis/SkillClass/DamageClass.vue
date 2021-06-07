<template>
  <div>
    <!-- damageClass -->
    <CollapseItem
      :compontentName="'伤害类排名'"
      :isChild="true"
    >
      {{ 'DamageClass' }}
    </CollapseItem>
    <!-- damageClass-end -->
    <!-- perDamage-Line-Chart -->
    <CollapseItem
      :compontentName="'秒伤折线图'"
      :isChild="true"
    >
      <PerDamage
        :skillParam="skillParam"
        :skillId="skillId"
        :emParam="emParam"
      />
    </CollapseItem>
  </div>
</template>

<script>
import CollapseItem from '../../../Common/CollapseItem.vue'
import perDamage from './DamageClass/PerDamage.vue'
import { emDataPretreate } from '../../../utils/skillParamCalc.js'

export default {
  props: {
    emParam: Object,
    skillData: Object,
    skillId: String
  },
  components: {
    CollapseItem,
    perDamage
  },
  computed: {
    skillParam () {
      return emDataPretreate(this.emParam, this.skillData, 'dam')
    }
  }
}
</script>

<style>

</style>
