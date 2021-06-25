<template>
  <el-container>
    <el-header height="42px">
      <div class="head-name">
        {{ $store.state.en.enName }}
      </div>
    </el-header>
    <el-main class="info-main">
      <BaseInfo />
    </el-main>
  </el-container>
</template>

<script>
/* eslint-disable camelcase */
import BaseInfo from './Eninfo/BaseInfo.vue'

export default {
  components: {
    BaseInfo
  }
}
</script>

<style lang="scss" scoped>
// 页头
.head-name {
  height: 100%;
  font-size: 28px;
  font-style: italic;
  font-weight: bold;
  padding-left: 20px;
  border-bottom: 2px solid #dcdfe6;
}
.info-main {
  padding: 3px;
  padding-top: 0px;
}
</style>
