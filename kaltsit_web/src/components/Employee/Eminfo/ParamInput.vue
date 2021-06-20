<template>
  <div id="param-input">
    <div class="input-container">
      <el-row>
        <span>精英阶段</span>
        <ul class="input-position">
          <li
            v-for="elt in Array(maxLevel.length).keys()"
            :key="elt"
            class="btn-position"
          >
            <el-button
              size="mini"
              @click="eliteClick(elt)"
              class="btn-slience"
              :class="{'btn-active': baseInfo.elite == elt}"
            >
              {{ elt }}
            </el-button>
          </li>
        </ul>
      </el-row>
      <el-row>
        <span>潜能等级</span>
        <ul class="input-position">
          <li
            v-for="pot in Array(potential+1).keys()"
            :key="pot"
            class="btn-position"
          >
            <el-button
              size="mini"
              @click="potClick(pot)"
              class="btn-slience"
              :class="{'btn-active': baseInfo.potentialLevel == pot}"
            >
              {{ pot+1 }}
            </el-button>
          </li>
        </ul>
      </el-row>
      <!-- 等级 -->
      <el-row>
        <span>干员等级</span>
        <el-slider
          v-model="baseInfo.levelValue"
          :show-tooltip="false"
          :min="1"
          :max="maxLevel[baseInfo.elite]"
        />
        <span class="value-number">{{ baseInfo.levelValue }}</span>
      </el-row>
      <!-- 信赖 -->
      <el-row>
        <span>干员信赖</span>
        <el-slider
          v-model="baseInfo.favorValue"
          :show-tooltip="false"
          :min="0"
          :max="100"
        />
        <span class="value-number">{{ baseInfo.favorValue }}</span>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ParamInput',
  data () {
    return {
      baseInfo: {
        elite: 0,
        potentialLevel: 0,
        levelValue: 1,
        favorValue: 100
      }
    }
  },
  computed: {
    emKey () {
      return this.$store.state.em.emKey
    },
    potential () {
      return this.$store.state.em.emData.maxPotential
    },
    maxLevel () {
      return this.$store.state.em.emData.phases.maxLevel
    }
  },
  methods: {
    submitInfo () {
      this.$store.commit('em/updateEmInputParam', this.baseInfo)
    },
    eliteClick (elt) {
      this.baseInfo.elite = elt
    },
    potClick (pot) {
      this.baseInfo.potentialLevel = pot
    },
    initInputParam () {
      this.baseInfo.elite = Math.min(this.baseInfo.elite, this.maxLevel.length - 1)
      this.baseInfo.potentialLevel = Math.min(this.baseInfo.potentialLevel, this.potential)
    }
  },
  watch: {
    baseInfo: {
      handler () {
        this.submitInfo()
      },
      deep: true,
      immediate: true
    },
    emKey: {
      handler () {
        this.initInputParam()
        this.submitInfo()
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.input-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  min-height: 160px;
}
#param-input {
  min-width: 300px;
  // width: 40%;
  flex: 1;
  // max-width: 420px;
  height: 100%;
  .el-row {
    display: flex;
    width: 96%;
    height: 40px;
    align-items: center;
  }
  span {
    font-weight: 700;
  }
  .value-number {
    font-weight: normal;
    text-align: left;
    width: 30px;
  }
  .input-position {
    display: inline-block;
    margin-left: 15px;
  }
  // 按钮
  .btn-position {
    display: inline-flex;
    margin-right: 5px;
  }
  button {
    text-align: center;
    font-size: 15px;
    font-weight: 500;
    padding: 5px 12px;
  }
  @media only screen and (max-width:333px) {
    button {
      padding: 5px 10px;
    }
  }
  @media only screen and (min-width:768px) and (max-width:800px) {
    button {
      padding: 5px 11px;
    }
  }
  .btn-slience {
    color: #67c23a;
    background-color: #f0f9eb;
    border-color: #c2e7b0;
  }
  .btn-active {
    color: #fff;
    background-color: #67c23a;
    border-color: #67c23a;
  }
  // 滑动条
  .el-slider {
    width: calc(100% - 120px);
    margin-left: 15px;
    margin-right: 10px;
    align-items: center;
  }
  /deep/.el-slider__runway {
    margin: 17px 0;
  }
  /deep/.el-slider__button {
    width: 10px;
    height: 10px;
    border-color: #67c23a;
  }
  /deep/.el-slider__bar {
    background-color: #67c23a;
  }
}
@media only screen and (max-width:767px) {
  #param-input {
    width: 100%;
  }
}
</style>
