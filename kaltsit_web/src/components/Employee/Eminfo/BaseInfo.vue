<template>
  <div id="base-info" :style="{backgroundImage:'url(' + imgUrl + ')'}" class="bc-img title-sticky">
    <div class="bc-title">{{ employee.name }}</div>
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
  justify-content: start;
  align-items: flex-end;
}
#em-img {
  display: inline-block;
  height: 250px;
  height: 250px;
}
.bc-img {
  background-repeat: no-repeat;
  background-size: 512px 512px;
  background-position: center;
}
.title-sticky {
  position: sticky;
  top: -410px;
  z-index: 1002;
}
.bc-title {
  padding-left: 35px;
  padding-bottom: 2px;
  font-size: 1.75rem;
  font-style: italic;
  color: #fff;
  font-weight: 700;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.15);
}
.card-style {
  margin-bottom: 5px;
  background-color: white;
  border: 1px solid #ebeef5;
  border-radius: 4px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15);
}
</style>
