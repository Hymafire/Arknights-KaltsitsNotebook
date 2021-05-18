<template>
  <div>
    <ul>
      <li v-for="(talent, index) in talents" :key="index">
        <div>{{ talent.name }}</div>
        <div>{{ talent.description }}</div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'TalentInfo',
  data () {
    return {
      talents: {
        type: Array,
        default: []
      }
    }
  },
  props: {
    talentTable: Array,
    paramInputed: Object,
    changed: Boolean
  },
  methods: {
    // 获取需要显示的天赋信息
    getTalents () {
      const talents = []
      for (let i = 0; i < this.talentTable.length; i++) {
        let k = -1
        for (let j = 0; j < this.talentTable[i].length; j++) {
          const talent = this.talentTable[i][j]
          if (this.paramInputed.potentialLevel >= talent.requiredPotentialRank &&
              this.paramInputed.elite >= talent.unlockCondition.phase &&
              this.paramInputed.levelValue >= talent.unlockCondition.level) {
            k = j
          }
        }
        if (k >= 0) {
          talents.push(this.talentTable[i][k])
        }
      }
      this.talents = talents
    }
  },
  watch: {
    changed: {
      handler () {
        this.getTalents()
      },
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
