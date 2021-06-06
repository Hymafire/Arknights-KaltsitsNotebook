<template>
  
</template>

<script>
export default {
  data () {
    return {
      activeName: []
    }
  },
  props: {
    skillParam: Array
  },
  components: {
  },
  methods: {
    // 判断折叠面板是否处于激活状态
    isActive (name) {
      for (let i = 0; i < this.activeName.length; i++) {
        if (name === this.activeName[i]) {
          return true
        }
      }
      return false
    },
    changeActive (name) {
      const index = this.activeName.indexOf(name)
      if (index === -1) {
        this.activeName.push(name)
      } else {
        this.activeName.splice(index, 1)
      }
    }
  }
}
</script>

<style>

</style>
