<template>
  <div>
    <div v-for="(skill, i) in skillsTable" :key="skill">
      <CollapseItem
        :compontentName="skillData(skill, i).name"
        :layer="3"
      >
        <SkillAnalysis
          :skillId="skill"
          :emParam="emParam"
          :skillData="skillData(skill, i)"
        />
      </CollapseItem>
    </div>
  </div>
</template>

<script>
import CollapseItem from '../../Common/CollapseItem.vue'
import SkillAnalysis from './SkillClass/SkillAnalysis.vue'

export default {
  props: {
    emParam: Object,
    skillsLevel: Array,
    skillsFlag: Array
  },
  components: {
    SkillAnalysis,
    CollapseItem
  },
  computed: {
    skillsTable () {
      return this.$store.state.employeeData[this.$store.state.employeeKey].skills
    }
  },
  methods: {
    skillData (skillId, skillLevel) {
      const skillsData = require('../../../assets/data/skill_table.json')
      return skillsData[skillId].levels[skillLevel]
    }
  }
}
</script>

<style>

</style>
