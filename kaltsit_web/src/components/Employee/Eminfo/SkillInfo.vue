<template>
  <div>
    <ul>
      <li v-for="(skill, index) in showSkills" :key="index" class="mask-fa">
        <div :class="{'mask-layer': !skillsFlag[index]}" class="mask-text">
          <span :class="{'text-display': skillsFlag[index]}"> ==== 未解锁 ==== </span>
        </div>
        <div class="skill-box">
          <div id="title-box">
            <div>
              <img id="img-box" :src="imgUrls[index]" alt="Worry!" />
            </div>
            <div>{{ showSkills[index].name }}</div>
          </div>
          <div id="description-box">
            <div>
              <span>{{ showSkills[index].initSp }} | </span>
              <span>{{ showSkills[index].spCost }} | </span>
              <span>{{ showSkills[index].duration }}</span>
            </div>
            <div v-html="showSkills[index].description"></div>
          </div>
          <div id="level-box">
            <el-button @click="increaseN(index)" size="mini" class="level-btn">+</el-button>
            <div class="level-value">Lv. {{ skillsLevel[index] }}</div>
            <el-button @click="decreaseN(index)" size="mini" class="level-btn">-</el-button>
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
      // 目标干员的数据
      emSkills: Array,
      // 技能的等级
      skillsLevel: Array,
      // 技能是否解锁
      skillsFlag: Array,
      // 技能等级信息改变
      levelChanged: false,
      // 技能的图片信息
      imgUrls: Array,
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
      const imgUrls = []
      for (const i in this.skillsName) {
        for (const j in this.skillData) {
          if (this.skillsName[i] === j) {
            emSkills.push(this.skillData[j])
            skillsLevel.push(7)
            imgUrls.push(require('@/assets/images/skillsimgs/skill_icon_' + j + '.png'))
            break
          }
        }
      }
      this.emSkills = emSkills
      this.skillsLevel = skillsLevel
      this.imgUrls = imgUrls
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
// 遮罩层
.mask-text {
  display: flex;
  align-items: center;
  span {
    margin: 0px auto;
    font-size: 20px;
    color: #fff;
    font-weight: 700;
    letter-spacing: 2px;
  }
  .text-display {
    display: none;
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
  background-color: rgba(0, 0, 0, .3);
}
.skill-box {
  display: flex;
  justify-content: space-around;
  border-bottom: 1px solid #ebebeb;
  #title-box {
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
  #description-box {
    width: 70vw;
    padding: 5px;
  }
  #level-box {
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
