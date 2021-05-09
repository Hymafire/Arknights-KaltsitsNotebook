<template>
  <div class="base-info card-style">
    <!-- 输入 -->
    <div id="param-input">
      <el-row>
        <span>精英阶段</span>
        <ul class="input-position">
          <li v-for="elt in Array(maxLevel.length).keys()" :key="elt" class="btn-position">
            <el-button size="mini" @click="eliteClick(elt)" class="btn-slience"
              :class="{'btn-active': baseInfo.elite == elt}">{{ elt }}</el-button>
          </li>
        </ul>
      </el-row>
      <el-row>
        <span>潜能等级</span>
        <ul class="input-position">
          <li v-for="pot in Array(potential+1).keys()" :key="pot" class="btn-position">
            <el-button size="mini" @click="potClick(pot)" class="btn-slience"
              :class="{'btn-active': baseInfo.potentialLevel == pot}">{{ pot+1 }}</el-button>
          </li>
        </ul>
      </el-row>
      <!-- 等级 -->
      <el-row>
        <span>干员等级</span>
        <el-slider v-model="baseInfo.levelValue" :show-tooltip="false" :min="1" :max="maxLevel[baseInfo.elite]"/>
        <span class="value-number">{{ baseInfo.levelValue }}</span>
      </el-row>
      <!-- 信赖 -->
      <el-row>
        <span>干员信赖</span>
        <el-slider v-model="baseInfo.favorValue" :show-tooltip="false" :min="0" :max="100"/>
        <span class="value-number">{{ baseInfo.favorValue }}</span>
      </el-row>
    </div>
    <div id="param-show">
      <ul>
        <li>
          <span>最大生命</span>
          <span>{{showParam.maxHp}}</span>
        </li>
        <li>
          <span>攻击</span>
          <span>{{showParam.atk}}</span>
        </li>
        <li>
          <span>防御</span>
          <span>{{showParam.def}}</span>
        </li>
        <li>
          <span>法抗</span>
          <span>{{showParam.magRes}}</span>
        </li>
        <li>
          <span>部署费用</span>
          <span>{{showParam.cost}}</span>
        </li>
        <li>
          <span>阻挡数</span>
          <span>{{showParam.block}}</span>
        </li>
        <li>
          <span>攻击间隔</span>
          <span>{{showParam.atkTime}}</span>
        </li>
        <li>
          <span>在部署时间</span>
          <span>{{showParam.respawnTime}}</span>
        </li>
      </ul>
    </div>
    <div id="range-show">
      射程展示
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseInfo',
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
    maxLevel: Array,
    showParam: Array
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
.base-info {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  >div {
    text-align: left;
    min-width: 360px;
    height: 160px;
    margin-left: 10px;
  }
}
// 输入信息样式
#param-input {
  .el-row {
    display: flex;
    height: 40px;
    line-height: 40px;
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
    font-size: 15px;
    font-weight: 500;
    padding: 5px 12px;
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
    width: 65%;
    margin: 0px 10px;
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
// 展示信息样式
#param-show {
}
// 卡片
.card-style {
  margin-bottom: 5px;
  background-color: white;
  border: 1px solid rgb(230, 230, 230);
  border-radius: 3px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15);
}
</style>
