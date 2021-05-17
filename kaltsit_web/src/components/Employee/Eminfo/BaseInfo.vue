<template>
  <div>
    <div id="em-img"/>
    <div id="em-desp">{{ employee.description }}</div>
    <div>{{ employee.itemUsage }}</div>
  </div>
</template>

<script>
export default {
  name: 'BaseInfo',
  props: {
    employee: Array
  }
}
</script>

<style lang="scss" scoped>
.card-style {
  margin-bottom: 5px;
  background-color: white;
  border: 1px solid #ebeef5;
  border-radius: 4px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15);
}
</style>
