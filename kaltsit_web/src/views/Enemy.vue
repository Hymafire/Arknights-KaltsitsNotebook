<template>
  <ViewBaseUi :viewMod="'enemy'" id="enemy-view">
    <Eninfo />
  </ViewBaseUi>
</template>

<script>
import ViewBaseUi from '../components/Common/ViewBaseUi.vue'
import Eninfo from '../components/Enemy/Eninfo.vue'

export default {
  components: {
    ViewBaseUi,
    Eninfo
  }
}
</script>

<style lang="scss" scoped>

</style>
