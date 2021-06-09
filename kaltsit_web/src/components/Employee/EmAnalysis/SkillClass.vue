<template>
  <div>
    <div v-for="skill in skillsData" :key="skill.name">
      <CollapseItem
        :compontentName="skill.name"
        :layer="3"
      >
        <SkillAnalysis :skillData="skill" />
      </CollapseItem>
    </div>
  </div>
</template>

<script>
import CollapseItem from '../../Common/CollapseItem.vue'
import SkillAnalysis from './SkillClass/SkillAnalysis.vue'

export default {
  components: {
    SkillAnalysis,
    CollapseItem
  },
  computed: {
    skillsData () {
      const skillsTable = require('../../../assets/data/skill_table.json')
      const skillsKey = this.$store.state.em.emData.skills
      const skillsLevel = this.$store.state.em.emSkillsLevel
      const skillsData = {}
      for (const i in skillsKey) {
        skillsData[skillsKey[i]] = skillsTable[skillsKey[i]].levels[skillsLevel[i]]
        skillsData[skillsKey[i]].skillId = skillsKey[i]
      }
      return skillsData
    }
  }
}
</script>

<style>

</style>
