<template>
  <div id="range-show">
    <div class="range-box-style" />
  </div>
</template>

<script>
export default {
  name: 'RangeShow'
}
</script>

<style lang="scss" scoped>
#range-show {
  width: 20%;
  display: flex;
  justify-content: center;
}
.range-box-style {
  display: inline-block;
  box-sizing: border-box;
  height: 1.5vw;
  width: 1.5vw;
  padding: 1.5vw;
  margin: 0.5vw;
  border: 3px solid #ddd;
  background-color: #fdfdfd;
}
</style>
