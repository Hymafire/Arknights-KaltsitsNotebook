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
        :skillId="skillId"
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
import { damModJudge, atkModJudge } from '../../../utils/damageCalc.js'

export default {
  data () {
    return {
      skillParam: {}
    }
  },
  props: {
    emParam: Object,
    skillData: Object,
    skillId: String
  },
  components: {
    CollapseItem,
    PerDamage
  },
  computed: {
    isChanged () {
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
    calcSkillParam () {
      this.skillParam = getSkillParam(this.emParam, this.skillData, 'dam')
    }
  },
  watch: {
    isChanged: {
      handler () {
        this.calcSkillParam()
      }
    }
  }
}
</script>

<style>

</style>
