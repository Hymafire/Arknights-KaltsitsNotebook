<template>
  <div>
    <CollapseItem
      :compontentName="'总评价'"
      :layer="4"
    >
    </CollapseItem>
    <CollapseItem
      v-if="skillType.dam"
      :compontentName="'攻击类'"
      :layer="4"
    >
      <DamageClass
        :skillData="skillData"
      />
    </CollapseItem>
    <CollapseItem
      v-if="skillType.sur"
      :compontentName="'生存类'"
      :layer="4"
    >
    </CollapseItem>
    <CollapseItem
      v-if="skillType.sup"
      :compontentName="'辅助类'"
      :layer="4"
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
    skillNo: Number
  },
  components: {
    CollapseItem,
    DamageClass
  },
  created () {
    this.getSkillType()
  },
  computed: {
    skillData () {
      return this.$store.state.em.emSkillsData[this.skillId].levels[this.$store.state.em.emSkillsLevel[this.skillNo]]
    }
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
    }
  }
}
</script>

<style>

</style>
