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
      <router-link to="/compare" replace>
        干员对比
      </router-link>
      <router-link to="/enemy" replace>
        敌人分析
      </router-link>
      <!--
      <router-link to="/createm" replace>简历编辑</router-link>
      <router-link to="/createn" replace>敌人登记</router-link>
      -->
    </div>
    <!-- 大-end -->
    <!-- 小 -->
    <div id="tool-bar" class="hidden-sm-and-up">
      <div class="tool-mag">&gt;</div>
      <div class="tool-title">{{$route.name}}</div>
      <button class="tool-btn" @click="openDrawer">|||</button>
    </div>
    <!-- 小-end -->
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css'

export default {
  name: 'NavBar',
  methods: {
    openDrawer () {
      this.$store.commit('openDrawer')
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
    height: 52px;
    line-height: 52px;
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
    height: 52px;
    width: 52px;
    line-height: 52px;
    font-size: 26px;
    font-weight: 100;
    text-align: center;
  }
  .tool-title {
    display: inline-block;
    box-sizing: border-box;
    height: 52px;
    line-height: 52px;
    font-size: 22px;
    font-weight: 400;
    color: #303133;
    margin-right: auto;
  }
  .tool-btn {
    height: 52px;
    width: 52px;
    border: 0px solid transparent;
    background-color: transparent;
  }
  button:hover {
    background-color: rgba(0, 0, 0, .1)
  }
}
</style>
