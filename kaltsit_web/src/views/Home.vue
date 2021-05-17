<template>
  <div class="linear">
    <div class="welcome-title">
      <div>凯尔希的笔记本</div>
      <div>Kal'tsit's Notebook</div>
    </div>
    <div>
      <div class="version">
        v0.8.0
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  created () {
    this.closeDrawer()
  },
  methods: {
    closeDrawer () {
      this.$store.commit('closeDrawer')
    }
  }
}
</script>

<style lang="scss" scoped>
// 欢迎词
.welcome-title {
  margin: 0px;
  font-size: 40px;
  overflow: hidden;
  position: absolute;
  text-align: center;
  top: 37%;
  width: 100%;
}
// 版本号
.version {
  position: absolute;
  text-align: right;
  bottom: 2px;
  right: 10px;
  width: 100%;
}
</style>
