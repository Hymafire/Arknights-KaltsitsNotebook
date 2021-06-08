<template>
  <div>
    <CollapseItem
      :compontentName="' -总评价'"
      :isChild="true"
    >
    </CollapseItem>
    <CollapseItem
      v-if="skillType.dam"
      :compontentName="' -攻击类'"
      :isChild="true"
    >
      <DamageClass
        :emParam="emParam"
        :skillId="skillId"
        :skillData="skillData"
      />
    </CollapseItem>
    <CollapseItem
      v-if="skillType.sur"
      :compontentName="' -生存类'"
      :isChild="true"
    >
    </CollapseItem>
    <CollapseItem
      v-if="skillType.sup"
      :compontentName="' -辅助类'"
      :isChild="true"
    >
    </CollapseItem>
  </div>
</template>

<script>
import CollapseItem from '../../../Common/CollapseItem.vue'
import DamageClass from './DamageClass.vue'

export default {
  data () {
    return {
      // 一个技能可以同时拥有多个类型
      skillType: {
        dam: false,
        sur: false,
        sup: false
      }
    }
  },
  props: {
    skillId: String,
    emParam: Object,
    skillData: Object
  },
  components: {
    CollapseItem,
    DamageClass
  },
  created () {
    this.getSkillType()
  },
  methods: {
    // 获取技能类型:
    getSkillType () {
      for (let i = 0; i < this.skillData.blackboard.length; i++) {
        const keyTag = this.skillData.blackboard[i].key
        if (keyTag.indexOf('atk') !== -1) {
          this.skillType.dam = true
        } else if (keyTag.indexOf('attack') !== -1) {
          this.skillType.dam = true
        } else if (keyTag.indexOf('time') !== -1) {
          this.skillType.dam = true
        } else if (keyTag.indexOf('cost') !== -1) {
          this.skillType.sup = true
        } else if (keyTag.indexOf('def') !== -1) {
          this.skillType.sur = true
        }
      }
      console.log(this.skillType)
    }
  }
}
</script>

<style>

</style>
