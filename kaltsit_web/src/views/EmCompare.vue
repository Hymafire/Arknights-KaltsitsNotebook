<template>
  <div>
    <span>干员对比</span>
  </div>
</template>

<script>
export default {
  name: 'Compare',
  created () {
    this.closeDrawer()
  },
  methods: {
    closeDrawer () {
      this.$store.commit('dal/closeDrawer')
    }
  }
}
</script>
