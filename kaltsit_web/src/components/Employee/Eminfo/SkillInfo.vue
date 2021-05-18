<template>
  <div>
    <ul>
      <li v-for="(skill, index) in showSkills" :key="index">
        <div>===============</div>
        <div>
          <div>图片</div>
          <div>{{ showSkills[index].name }}</div>
        </div>
        <div>
          <div>
            <span>{{ showSkills[index].initSp }} | </span>
            <span>{{ showSkills[index].spCost }} | </span>
            <span>{{ showSkills[index].duration }}</span>
          </div>
          <div v-html="showSkills[index].description"></div>
        </div>
        <div>
          技能等级
          <el-button @click="increaseN(index)">+</el-button>
          {{ skillsLevel[index] }}
          <el-button @click="decreaseN(index)">-</el-button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { descTranslate } from '../../utils/descTranslate.js'

export default {
  name: 'SkillInfo',
  data () {
    return {
      // 用于显示的数据
      showSkills: {
        type: Array,
        default: []
      },
      // 重新处理后的数据
      skillsTranslated: {
        type: Array,
        default: []
      },
      // 目标干员的数据
      emSkills: {
        type: Array,
        default: []
      },
      // 技能的等级
      skillsLevel: {
        type: Array,
        default: []
      },
      // 技能等级信息改变
      levelChanged: {
        type: Boolean,
        default: false
      },
      // 所有的技能信息
      skillData: Object
    }
  },
  props: {
    employeeName: String,
    skillsName: Array,
    elite: Number
  },
  created () {
    this.getSkillData()
    this.getSkills()
    this.translateSkills()
    this.getShowSkills()
  },
  methods: {
    // 获取需要显示的技能信息
    getShowSkills () {
      const showSkills = []
      for (let i = 0; i <= this.elite; i++) {
        if (this.skillsLevel[i] !== null) {
          showSkills.push(this.skillsTranslated[i][this.skillsLevel[i]])
          // showSkills.push(this.translateSkills[i][this.skillsLevel[i]])
        }
      }
      this.showSkills = showSkills
    },
    // 翻译技能信息,并重新保存
    translateSkills () {
      const skillsTranslated = []
      for (const i in this.emSkills) {
        const skill = []
        for (const j in this.emSkills[i].levels) {
          const skillLv = []
          skillLv.name = this.emSkills[i].levels[j].name
          skillLv.duration = this.emSkills[i].levels[j].duration
          const str = descTranslate(this.emSkills[i].levels[j].description, this.emSkills[i].levels[j].blackboard)
          skillLv.description = str
          skillLv.initSp = this.emSkills[i].levels[j].spData.initSp
          skillLv.spCost = this.emSkills[i].levels[j].spData.spCost
          skill.push(skillLv)
        }
        skillsTranslated.push(skill)
      }
      this.skillsTranslated = skillsTranslated
    },
    // 获取目标干员的技能信息
    getSkills () {
      const emSkills = []
      const skillsLevel = []
      for (const i in this.skillsName) {
        for (const j in this.skillData) {
          if (this.skillsName[i] === j) {
            emSkills.push(this.skillData[j])
            skillsLevel.push(7)
            break
          }
        }
      }
      descTranslate(emSkills[0].levels[1].description)
      this.emSkills = emSkills
      this.skillsLevel = skillsLevel
    },
    // 获取技能数据
    getSkillData () {
      this.skillData = require('@/assets/data/skill_table.json')
    },
    increaseN (n) {
      this.skillsLevel[n]++
      this.levelChanged = !this.levelChanged
    },
    decreaseN (n) {
      this.skillsLevel[n]--
      this.levelChanged = !this.levelChanged
    }
  },
  watch: {
    employeeName: {
      handler () {
        this.getSkills()
        this.translateSkills()
        this.getShowSkills()
      },
      immediate: true
    },
    elite: {
      handler () {
        this.getShowSkills()
      },
      immediate: true
    },
    levelChanged: {
      handler () {
        this.getShowSkills()
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
