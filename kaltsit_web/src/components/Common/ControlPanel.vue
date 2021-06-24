<template>
  <el-dialog
    title="控制面板"
    :visible.sync="isControlPanelOpen"
    width="260px"
  >
    <div class="control-item">
      <span>敌人分析</span>
      <el-switch v-model="isEnemyAnalysis" active-text="开" inactive-text="关" />
    </div>
    <div class="control-item">
      <span>手风琴模式</span>
      <el-switch v-model="isCollapseAccordion" active-text="开" inactive-text="关" />
    </div>
    <div class="control-item">
      <span>对比数量限制</span>
      <el-switch v-model="isCompareNumLimit" active-text="开" inactive-text="关" />
    </div>
    <div class="control-item dev-func-class">
      <span style="color: #FB3535">开发功能</span>
      <el-switch
        v-model="isDevFuncApply"
        active-text="开"
        inactive-text="关"
        active-color="#FB3535"
      />
    </div>
  </el-dialog>
</template>

<script>
export default {
  computed: {
    isControlPanelOpen: {
      get () {
        return this.$store.state.cp.isControlPanelOpen
      },
      set () {
        return this.$store.commit('cp/closeControlPanel')
      }
    },
    isEnemyAnalysis: {
      get () {
        return this.$store.state.cp.isEnemyAnalysis
      },
      set (value) {
        this.$store.commit('cp/changeIsEnemyAnalysis', value)
      }
    },
    isCollapseAccordion: {
      get () {
        return this.$store.state.cp.isCollapseAccordion
      },
      set (value) {
        this.$store.commit('cp/changeIsCollapseAccordion', value)
      }
    },
    isDevFuncApply: {
      get () {
        return this.$store.state.cp.isDevFuncApply
      },
      set (value) {
        this.$store.commit('cp/changeIsDevFuncApply', value)
      }
    },
    isCompareNumLimit: {
      get () {
        return this.$store.state.cp.isCompareNumLimit
      },
      set (value) {
        this.$store.commit('cp/changeIsCompareNumLimit', value)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.control-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 26px;
  margin-bottom: 5px;
  padding: 0px 10px;
  span {
    font-size: 16px;
    line-height: 26px;
    width: 100px;
    color: #303133;
  }
}
/deep/.el-dialog__body {
  padding: 10px;
  padding-bottom: 15px;
}
.dev-func-class {
  padding-top: 3px;
  margin-top: 2px;
  border-top: 1px solid #C0C4CC;
  /deep/.el-switch__label.is-active {
    color: #FB3535;
  }
}
</style>
