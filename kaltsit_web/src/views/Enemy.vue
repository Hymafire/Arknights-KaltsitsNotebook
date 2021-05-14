<template>
  <el-container>
    <!-- 列表和查询区 -->
    <el-aside width="249px" :class="{'aside-collapse': $store.state.isListCollapse}">
      <SearchList
        :list-data="enemyList"
        @objChanged="changeName"
      />
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <Eninfo :enemy_name="enemy_name" />
    </el-main>
  </el-container>
</template>

<script>
import SearchList from '../components/Common/SearchList.vue'
import Eninfo from '../components/Enemy/Eninfo.vue'

export default {
  data () {
    return {
      enemy_name: '源石虫',
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
    changeName (name) {
      this.enemy_name = name
    },
    getEnemyList () {
      this.enemyList = require('@/assets/data/enemylist.json')
    },
    closeDrawer () {
      this.$store.commit('closeDrawer')
    },
    initCollapse () {
      this.$store.commit('initCollapse')
    }
  }
}
</script>

<style lang="scss" scoped>
.el-container {
  height: 100%;
}
.el-aside {
  background-color: #fff;
  padding: 1px;
}
.el-main {
  background-color: #fff;
  padding: 1px;
}
.aside-collapse {
  display: none !important;
}
</style>
