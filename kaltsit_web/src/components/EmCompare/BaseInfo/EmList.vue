<template>
  <div class="list-container">
    <div v-for="(em, index) in this.$store.state.emc.emNameList" :key="index" class="employee-container">
      <div>
        <div class="icon-box" :style="{'background-image': 'url(' + iconUrls[index] + ')'}">
          <div class="em-name" @click="subEmployee(index)">{{ em }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    iconUrls () {
      const iconUrls = []
      const emList = this.$store.state.emc.emKeyList
      console.log(emList)
      for (let i = 0; i < emList.length; i++) {
        this.$set(iconUrls, i, require('@/assets/images/emicons/' + emList[i] + '.png'))
      }
      return iconUrls
    }
  },
  methods: {
    subEmployee (index) {
      this.$store.commit('emc/subEmployee', index)
    }
  }
}
</script>

<style lang="scss" scoped>
.list-container {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
}
.employee-container {
  display: center;
  // flex: 0.5
}
.icon-box {
  width: 90px;
  height: 90px;
  background-size: 90px 90px;
  display: flex;
  align-items: flex-end;
}
.em-name {
  padding-left: 3px;
  padding-bottom: 1px;
  color: azure;
  font-weight: 700;
}
</style>
