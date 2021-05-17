<template>
  <div id="param-input">
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
  props: {
    potential: Number,
    maxLevel: Array
  },
  methods: {
    submitInfo () {
      this.$emit('submitInfo', this.baseInfo)
    },
    eliteClick (elt) {
      this.baseInfo.elite = elt
    },
    potClick (pot) {
      this.baseInfo.potentialLevel = pot
    }
  },
  watch: {
    baseInfo: {
      handler () {
        this.submitInfo()
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>
#param-input {
  .el-row {
    display: flex;
    height: 50px;
    line-height: 50px;
    padding-left: 10px;
  }
  span {
    font-weight: 700;
  }
  .value-number {
    font-weight: normal;
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
  @media only screen and (max-width:321px) {
    button {
      padding: 5px 10px;
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
    width: 60%;
    margin-left: 15px;
    margin-right: 10px;
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
</style>
