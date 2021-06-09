<template>
  <div class="w">
    <!-- headImg -->
    <BaseInfo />
    <!-- 主信息区 -->
    <div class="info-main">
      <!-- 参数信息 -->
      <div id="param-info">
        <ParamInput />
        <ParamShow />
        <RangeShow />
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
  align-items: center;
  flex-wrap: wrap;
}
</style>
