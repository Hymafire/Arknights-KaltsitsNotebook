<template>
  <div>
    <div v-for="(skill, index) in skillsName" :key="skill.Id">
      <CollapseItem
        :compontentName="skill.name"
        :layer="3"
      >
        <SkillAnalysis
          :skillId="skill.Id"
          :skillNo="index"
        />
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
    skillsName () {
      const skillsName = []
      let cnt = 0
      const skillsData = this.$store.state.em.emSkillsData
      for (const skill in skillsData) {
        const skillName = {}
        skillName.name = skillsData[skill].levels[this.$store.state.em.emSkillsLevel[cnt]].name
        skillName.Id = skill
        this.$set(skillsName, cnt++, skillName)
      }
      return skillsName
    }
  }
}
</script>

<style>

</style>
