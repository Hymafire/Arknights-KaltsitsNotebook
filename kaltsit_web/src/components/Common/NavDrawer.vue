<template>
  <div>
    <el-drawer
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose"
      size="40%"
    >
      <div id="drawer-nav">
        <router-link to="/home" replace>
          首页
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
      </div>
    </el-drawer>
  </div>
</template>

<script>
export default {
  name: 'NavDrawer',
  data () {
    return {
      drawer: false,
      direction: 'ttb'
    }
  },
  computed: {
    isDrawerOpen () {
      return this.$store.state.dal.isDrawerOpen
    }
  },
  methods: {
    handleClose () {
      this.$store.commit('dal/closeDrawer')
    }
  },
  watch: {
    isDrawerOpen: {
      handler () {
        this.drawer = this.$store.state.dal.isDrawerOpen
      }
    }
  }
}
</script>

<style lang="scss" scoped>
a {
  display: block;
  text-decoration: none;
}
/deep/.el-drawer__header {
  margin-bottom: 0px;
  padding: 10px;
}
#drawer-nav {
  height: 100%;
  >a {
    display: block;
    box-sizing: border-box;
    height: 42px;
    line-height: 42px;
    padding-left: 30px;
    font-size: 16px;
    color: #303133;
  }
  >a:hover {
    background-color: #f9f9f9;
  }
}
</style>
