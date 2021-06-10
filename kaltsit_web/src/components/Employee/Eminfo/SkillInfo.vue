<template>
  <div>
    <ul>
      <li v-for="(skill, index) in showSkills" :key="index" class="mask-fa">
        <div
          :id="maskId(index)"
          :class="{'mask-layer-hidden': skillsFlag[index]}"
          class="mask-text mask-layer">
          <span :class="{'text-hidden': skillsFlag[index]}">
            ==== 未解锁 ====
          </span>
        </div>
        <div class="skill-box">
          <div class="title-box">
            <div>
              <img class="img-box" :src="imgUrls[index]" alt="Worry!" />
            </div>
            <div>{{ showSkills[index].name }}</div>
          </div>
          <div class="description-box">
            <div>
              <span>{{ showSkills[index].initSp }} | </span>
              <span>{{ showSkills[index].spCost }} | </span>
              <span>{{ showSkills[index].duration }}</span>
            </div>
            <div v-html="showSkills[index].description"></div>
          </div>
          <div class="level-box">
            <el-button @click="increaseN(index)" size="mini" class="level-btn" :disabled="skillsMaxLevelLimit(index)">+</el-button>
            <div class="level-value">Lv. {{ skillsLevel[index] + 1 }}</div>
            <el-button @click="decreaseN(index)" size="mini" class="level-btn" :disabled="skillsLevel[index] <= 0">-</el-button>
          </div>
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
      showSkills: Array,
      // 重新处理后的数据
      skillsTranslated: Array,
      skillsLevel: Array,
      skillsFlag: Array
    }
  },
  computed: {
    skillsName () {
      return this.$store.state.em.emData.skills
    },
    elite () {
      return this.$store.state.em.emInputParam.elite
    },
    imgUrls () {
      const imgUrls = []
      const skillsData = this.$store.state.em.emSkillsData
      for (const skillId in skillsData) {
        const skillData = skillsData[skillId]
        if (skillData.iconId === null) {
          imgUrls.push(require('@/assets/images/skillsimgs/skill_icon_' + skillData.skillId + '.png'))
        } else {
          imgUrls.push(require('@/assets/images/skillsimgs/skill_icon_' + skillData.iconId + '.png'))
        }
      }
      return imgUrls
    }
  },
  created () {
    this.initSkillsLevel()
    this.translateSkills()
    this.getShowSkills()
  },
  mounted () {
    this.isDisplayNone()
  },
  methods: {
    // 获取需要显示的技能信息
    getShowSkills () {
      const showSkills = []
      const skillsFlag = []
      for (const skill in this.skillsTranslated) {
        showSkills.push(this.skillsTranslated[skill][this.skillsLevel[skill]])
        if (this.elite >= skill) {
          skillsFlag.push(true)
        } else {
          skillsFlag.push(false)
        }
      }
      this.showSkills = showSkills
      this.skillsFlag = skillsFlag
    },
    // 翻译技能信息,并重新保存
    translateSkills () {
      const emSkills = this.$store.state.em.emSkillsData
      const skillsTranslated = []
      for (const i in emSkills) {
        const skill = []
        for (const j in emSkills[i].levels) {
          const skillLv = []
          skillLv.name = emSkills[i].levels[j].name
          skillLv.duration = emSkills[i].levels[j].duration
          const str = descTranslate(emSkills[i].levels[j].description, emSkills[i].levels[j].blackboard)
          skillLv.description = str
          skillLv.initSp = emSkills[i].levels[j].spData.initSp
          skillLv.spCost = emSkills[i].levels[j].spData.spCost
          skill.push(skillLv)
        }
        skillsTranslated.push(skill)
      }
      this.skillsTranslated = skillsTranslated
    },
    initSkillsLevel () {
      const skillsLevel = []
      for (const i in this.skillsName) {
        if (this.elite === 0) {
          this.$set(skillsLevel, i, 3)
        } else {
          this.$set(skillsLevel, i, 6)
        }
      }
      this.skillsLevel = skillsLevel
    },
    initSkillsLevel2 () {
      const maxLevel = [3, 6, 9]
      for (const i in this.skillsName) {
        this.skillsLevel[i] = Math.min(this.skillsLevel[i], maxLevel[this.elite])
      }
    },
    skillsMaxLevelLimit (i) {
      const maxLevel = [3, 6, 9]
      if (this.skillsLevel[i] >= maxLevel[this.elite]) {
        return true
      }
    },
    increaseN (n) {
      this.$set(this.skillsLevel, n, this.skillsLevel[n] + 1)
    },
    decreaseN (n) {
      this.$set(this.skillsLevel, n, this.skillsLevel[n] - 1)
    },
    maskId (index) {
      return 'mask-layer' + index
    },
    isDisplayNone () {
      for (const index in this.skillsFlag) {
        if (this.skillsFlag[index]) {
          setTimeout(function () {
            const obj = document.getElementById('mask-layer' + index)
            obj.style.zIndex = '-1'
          }, 800)
        } else {
          const obj = document.getElementById('mask-layer' + index)
          obj.style.zIndex = '1'
        }
      }
    }
  },
  watch: {
    skillsName: {
      handler () {
        this.initSkillsLevel()
        this.translateSkills()
        this.getShowSkills()
        this.isDisplayNone()
      }
    },
    elite: {
      handler () {
        this.initSkillsLevel2()
        this.getShowSkills()
        this.isDisplayNone()
      }
    },
    skillsLevel: {
      handler () {
        this.getShowSkills()
        this.$store.commit('em/updateSkillsLevel', this.skillsLevel)
        this.$store.commit('em/updateSkillsFlag', this.skillsFlag)
        this.$store.commit('em/changeIsEmUpdate')
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>
// 遮罩层
.mask-text {
  display: flex;
  align-items: center;
  span {
    margin: 0px auto;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 2px;
    transition: all .8s;
    color: #fff;
  }
  .text-hidden {
    // display: none;
    transition: all .8s;
    color: rgba(255, 255, 255, 0);
  }
}
.mask-fa {
  position: relative;
}
.mask-layer {
  position: absolute;
  float: left;
  z-index: 1;
  width: 100%;
  height: 100%;
  transition: all .8s;
  background-color: rgba(0, 0, 0, .4);
}
.mask-layer-hidden {
  transition: all .8s;
  background-color: rgba(0, 0, 0, 0);
}
.mask-layer-display {
  display: none;
}
.skill-box {
  display: flex;
  justify-content: space-around;
  border-bottom: 1px solid #ebebeb;
  .title-box {
    width: 10vw;
    max-width: 110px;
    min-width: 70px;
    img {
      text-align: center;
      height: 64px;
      width: 64px;
    }
    div {
      text-align: center;
    }
  }
  .description-box {
    width: 70vw;
    padding: 5px;
  }
  .level-box {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 5vw;
    min-width: 32px;
    .level-btn {
      width: 32px;
      text-align: center;
      padding: 5px 5px;
      margin: 0px auto;
    }
    .level-value {
      text-align: center;
    }
  }
}
</style>
