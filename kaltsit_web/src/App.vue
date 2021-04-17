<template>
  <div
    id="App"
    class="app-div"
  >
    <!-- 路由占位符 -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss" scoped>
// 设置充满全屏
.app-div {
  height: 100%
}
</style>
