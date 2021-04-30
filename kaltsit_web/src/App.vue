<template>
  <div id="App">
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
#id {
  height: 100%
}
</style>
