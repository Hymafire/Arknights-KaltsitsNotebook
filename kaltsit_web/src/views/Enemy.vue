<template>
  <el-container>
    <!-- 列表和查询区 -->
    <el-aside class="aside-width" :class="{'aside-collapse': $store.state.isListCollapse}">
      <SearchList :list-data="enemyList" @objChanged="changeName" />
    </el-aside>
    <!--  属性输出区  -->
    <el-main :class="{'is-aside-collapse': $store.state.isListCollapse}">
      <div class="collapse-btn-box" :class="{'btn-box-collapsed': $store.state.isListCollapse}">
        <el-button
          class="collapse-btn"
          @click="changeCollapse"
          :class="[{'el-icon-d-arrow-left': !$store.state.isListCollapse},
          {'el-icon-d-arrow-right': $store.state.isListCollapse}]"
        />
      </div>
      <Eninfo/>
    </el-main>
  </el-container>
</template>

<script>
import SearchList from '../components/Common/SearchList.vue'
import Eninfo from '../components/Enemy/Eninfo.vue'

export default {
  data () {
    return {
      enemyList: []
    }
  },
  created () {
    this.getEnemyList()
    this.closeDrawer()
    this.initCollapse()
  },
  components: {
    SearchList,
    Eninfo
  },
  methods: {
    getEnemyList () {
      this.enemyList = require('@/assets/data/enemylist.json')
    },
    changeName (name) {
      this.$store.commit('changeEnemyName', name)
    },
    closeDrawer () {
      this.$store.commit('closeDrawer')
    },
    initCollapse () {
      this.$store.commit('initCollapse')
    },
    changeCollapse () {
      this.$store.commit('changeCollapse')
    }
  }
}
</script>

<style lang="scss" scoped>
.el-container {
  height: 100%;
  position: relative;
}
.el-aside {
  position: absolute;
  z-index: 1003;
  height: 100%;
  background-color: rgba(255, 255, 255, .98);
  box-sizing: border-box;
  padding: 1px;
  border-right: 1px solid #dcdfe6;
}
.aside-width {
  width: 249px !important;
}
.el-main {
  position: absolute;
  height: 100%;
  left: 249px;
  width: calc(100% - 249px);
  background-color: #fff;
  box-sizing: border-box;
  padding: 1px;
}
.aside-collapse {
  display: none !important;
  // transform: translate(-249px, 0);
}
.is-aside-collapse {
  left: 0px !important;
  width: 100%;
}
@media only screen and (max-width:1080px) {
  .el-main {
    left: 0px;
    width: 100%;
  }
}
.collapse-btn-box {
  width: 30px;
  height: 30px;
  position: fixed;
  text-align: right;
  box-sizing: border-box;
  left: 249px;
  top: 52px;
  z-index: 1003;
}
@media only screen and (max-width:767px) {
  .collapse-btn-box {
    top: 46px;
  }
  .aside-width {
    width: 199px !important;
  }
  .collapse-btn-box {
    left: 199px;
  }
}
.btn-box-collapsed {
  left: 1px;
}
.collapse-btn {
  height: 30px;
  width: 30px;
  border: 0px solid transparent;
  padding: 0px;
  background-color: rgba(255, 255, 255, .8);
}
</style>
