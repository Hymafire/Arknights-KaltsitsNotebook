<template>
  <div class="collapse-box">
    <div :class="{'class-collapse-title': isChild, 'collapse-title': !isChild}">
      <span>{{ compontentName }}</span>
      <button
        @click="isActive = !isActive"
        :class="{'el-icon-arrow-right': !isActive, 'el-icon-arrow-down': isActive}"
      />
    </div>
    <el-collapse-transition>
      <div v-if="isActive">
        <slot></slot>
      </div>
    </el-collapse-transition>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isActive: false
    }
  },
  props: {
    isChild: {
      type: Boolean,
      default: false
    },
    compontentName: String
  }
}
</script>

<style>

</style>
