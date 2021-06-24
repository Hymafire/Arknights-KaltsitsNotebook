<template>
  <div id="nav-bar">
    <!-- 大 -->
    <div id="tab-bar" class="hidden-xs-only">
      <router-link to="/home" class="home-btn" replace>
        Kal'tsit's Notebook
      </router-link>
      <router-link to="/employee" replace>
        干员分析
      </router-link>
      <router-link to="/compare" replace v-if="$store.state.cp.isDevFuncApply">
        干员对比
      </router-link>
      <router-link to="/enemy" replace>
        敌人分析
      </router-link>
      <router-link to="/createm" replace v-if="$store.state.cp.isDevFuncApply">
        创作干员
      </router-link>
      <router-link to="/createn" replace v-if="$store.state.cp.isDevFuncApply">
        创作敌人
      </router-link>
    </div>
    <!-- 大-end -->
    <!-- 小 -->
    <div id="tool-bar" class="hidden-sm-and-up">
      <div class="el-icon-menu tool-mag" @click="openControlPanel" />
      <div class="tool-title">{{ $route.name }}</div>
      <button class="tool-btn el-icon-s-operation" @click="openDrawer" />
    </div>
    <!-- 小-end -->
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css'

export default {
  name: 'NavBar',
  data () {
    return {
      controlPanelCnt: 0
    }
  },
  methods: {
    openDrawer () {
      this.$store.commit('dal/openDrawer')
    },
    openControlPanel () {
      this.controlPanelCnt = this.controlPanelCnt + 1
      if (this.controlPanelCnt === 1) {
        setTimeout(() => {
          this.controlPanelCnt = 0
        }, 3000)
      } else if (this.controlPanelCnt >= 5) {
        this.controlPanelCnt = 0
        this.$store.commit('cp/openControlPanel')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
a {
  text-decoration: none;
}
#nav-bar {
  display: flex;
  flex-wrap: nowrap;
}
#tab-bar {
  display: flex;
  flex: 1;
  >a {
    display: inline-block;
    box-sizing: border-box;
    height: 48px;
    line-height: 48px;
    padding: 0px 15px;
    font-size: 16px;
    font-weight: 700;
    color: #909399;
  }
  >a:hover {
    color: #303133;
  }
  .home-btn {
    padding: 0px 15px;
    font-size: 32px;
    font-weight: 400;
    color: #303133;
  }
  .router-link-exact-active {
    color: #303133;
    border-bottom: 2px solid #000;
  }
}
#tool-bar {
  display: flex;
  width: 100%;
  .tool-mag {
    height: 42px;
    width: 42px;
    line-height: 42px;
    font-size: 26px;
    font-weight: 100;
    text-align: center;
    color: rgb(80, 80, 80);
  }
  .tool-title {
    display: inline-block;
    box-sizing: border-box;
    height: 42px;
    line-height: 40px;
    font-size: 21px;
    letter-spacing: 2px;
    font-weight: 400;
    color: #303133;
    margin-right: auto;
  }
  .tool-btn {
    height: 42px;
    width: 42px;
    border: 0px solid transparent;
    background-color: transparent;
    font-size: 26px;
    color: rgb(80, 80, 80)
  }
  button:hover {
    background-color: rgba(0, 0, 0, .1)
  }
}
</style>
