<template>
  <ViewBaseUi :viewMod="'employee'" id="employee-view">
    <Eminfo />
  </ViewBaseUi>
</template>

<script>
import ViewBaseUi from '../components/Common/ViewBaseUi.vue'
import Eminfo from '../components/Employee/Eminfo.vue'

export default {
  components: {
    ViewBaseUi,
    Eminfo
  }
}
</script>

<style lang="scss" scoped>

</style>
