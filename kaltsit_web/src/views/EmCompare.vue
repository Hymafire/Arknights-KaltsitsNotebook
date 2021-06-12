<template>
  <ViewBaseUi id="emCom-view" :viewMod="'emcompare'">
    <EmcInfo />
  </ViewBaseUi>
</template>

<script>
import ViewBaseUi from '../components/Common/ViewBaseUi.vue'
import EmcInfo from '../components/EmCompare/EmcInfo.vue'

export default {
  components: {
    ViewBaseUi,
    EmcInfo
  }
}
</script>
