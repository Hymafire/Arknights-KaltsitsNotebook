<template>
  <div>
    <ul>
      <li v-for="(talent, index) in talents" :key="index" class="mask-fa">
        <div :class="{'mask-layer-hidden': !talentsFlag[index]}" class="mask-text mask-layer">
          <span :class="{'text-display': talentsFlag[index]}"> ==== 未解锁 ==== </span>
        </div>
        <div id="talent-info">
          <div id="talent-name">{{ talent.name }}</div>
          <div id="talent-desc" v-html="talent.description" />
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { tagTranslate } from '../../utils/descTranslate.js'

export default {
  name: 'TalentInfo',
  data () {
    return {
      talents: Array,
      talentsFlag: Array
    }
  },
  props: {
    talentTable: Array,
    paramInputed: Object
  },
  computed: {
    changed: function () {
      return this.$store.state.isEmParamsUpdate
    }
  },
  methods: {
    // 获取需要显示的天赋信息
    getTalents () {
      const talents = []
      const talentsFlag = []
      for (let i = 0; i < this.talentTable.length; i++) {
        let k = 0
        let flag = false
        for (let j = 0; j < this.talentTable[i].length; j++) {
          const talent = this.talentTable[i][j]
          if (this.paramInputed.potentialLevel >= talent.requiredPotentialRank &&
              this.paramInputed.elite >= talent.unlockCondition.phase &&
              this.paramInputed.levelValue >= talent.unlockCondition.level) {
            k = j
            flag = true
          }
        }
        talents.push(this.talentTable[i][k])
        talents[i].description = tagTranslate(talents[i].description)
        talentsFlag.push(flag)
      }
      this.talents = talents
      this.talentsFlag = talentsFlag
    }
  },
  watch: {
    changed: {
      handler () {
        this.getTalents()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.mask-text {
  display: flex;
  align-items: center;
  span {
    margin: 0px auto;
    font-size: 20px;
    transition: all 0.8s;
    color: #fff;
    font-weight: 700;
    letter-spacing: 2px;
  }
  .text-display {
    // display: none;
    transition: all 0.8s;
    color: rgba(255, 255, 255, 0)
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
  transition: all 0.8s;
  background-color: rgba(0, 0, 0, 0);
}
.mask-layer-hidden {
  transition: all 0.8s;
  background-color: rgba(0, 0, 0, .4);
}
ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: start;
  border-top: 1px solid #ebebeb;
  border-bottom: 1px solid #ebebeb;
}
@media only screen and (max-width: 599px) {
  ul li {
    width: 100%
  }
}
@media only screen and (min-width: 600px) {
  ul li {
    width: 50%
  }
}
#talent-info {
  padding: 5px 10px;
  #talent-name {
    font-weight: 700;
  }
}
</style>
