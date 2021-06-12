<template>
  <div class="w">
    <!-- headImg -->
    <BaseInfo />
    <!-- 主信息区 -->
    <div class="info-main">
      <!-- 参数信息 -->
      <div id="param-info">
        <ParamInput />
        <div class="param-show-container">
          <ParamShow />
          <RangeShow />
        </div>
      </div>
      <div>
        <!-- 天赋信息 -->
        <TalentInfo />
        <!-- 技能信息 -->
        <SkillInfo />
      </div>
      <!-- 分析区 -->
      <EmAnalysis />
    </div>
  </div>
</template>

<script>
/* eslint-disable camelcase */
import BaseInfo from './Eminfo/BaseInfo.vue'
import ParamInput from './Eminfo/ParamInput.vue'
import ParamShow from './Eminfo/ParamShow.vue'
import RangeShow from './Eminfo/RangeShow.vue'
import TalentInfo from './Eminfo/TalentInfo.vue'
import SkillInfo from './Eminfo/SkillInfo.vue'
import EmAnalysis from './EmAnalysis.vue'

export default {
  components: {
    BaseInfo,
    ParamInput,
    ParamShow,
    RangeShow,
    TalentInfo,
    SkillInfo,
    EmAnalysis
  }
}
</script>

<style lang="scss" scoped>
// 信息展示区
.w {
  max-width: 1080px;
  margin: 0 auto;
}
.info-main {
  padding: 3px;
  padding-top: 0px;
}
//
#param-info {
  display: flex;
  // justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  height: 200px;
}
.param-show-container {
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  // justify-content: space-around;
  // width: 60%;
  flex: 1.5;
}
@media only screen and (max-width: 767px) {
  #param-info {
    height: auto;
  }
  .param-show-container {
    width: 100%;
  }
}
</style>
