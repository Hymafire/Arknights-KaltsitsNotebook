<template>
  <div class="linear">
    <div class="welcome-title">
      <div>凯尔希的笔记本</div>
      <div>Kal'tsit's Notebook</div>
    </div>
    <div>
      <div class="version"> v0.6.0 </div>
    </div>
  </div>
</template>

<script>
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
/*
// 背景渐变
.linear {
  height: 100%;
  background-image: linear-gradient(white 95%, rgb(95, 173, 22));
}
*/
</style>
