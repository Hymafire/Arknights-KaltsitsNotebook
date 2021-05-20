<template>
  <div id="base-info" class="title-sticky bc-color">
    <div id="em-img" :style="{backgroundImage:'url(' + imgUrl + ')'}" class="bc-img">
      <div class="bc-title">{{ employee.name }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseInfo',
  props: {
    employee: Object,
    employeeKey: String
  },
  computed: {
    imgUrl: function () {
      return require('../../../assets/images/emimgs/' + this.employeeKey + '.png')
    }
  }
}
</script>

<style lang="scss" scoped>
#base-info {
  width: 100%;
  height: 450px;
  display: flex;
}
#em-img {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: start;
  align-items: flex-end;
}
.bc-color {
  background-color: #ddd;
}
.bc-img {
  background-repeat: no-repeat;
  background-size: 512px 512px;
  background-position: center;
}
.title-sticky {
  position: sticky;
  top: -412px;
  z-index: 1002;
}
.bc-title {
  padding-left: 35px;
  padding-bottom: 2px;
  font-size: 1.75rem;
  font-style: italic;
  color: #fff;
  font-weight: 700;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.2);
}
</style>
