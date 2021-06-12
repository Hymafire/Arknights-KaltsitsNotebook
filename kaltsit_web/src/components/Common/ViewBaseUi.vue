<template>
  <el-container>
    <!-- 列表和查询区 -->
    <el-aside class="aside-width" :class="{'aside-collapse': $store.state.dal.isListCollapse}">
      <SearchList :list-data="List" @objChanged="changeName" />
    </el-aside>
    <!--  属性输出区  -->
    <el-main :class="{'is-aside-collapse': $store.state.dal.isListCollapse}">
      <div class="collapse-btn-box" :class="{'btn-box-collapsed': $store.state.dal.isListCollapse}">
        <el-button
          class="collapse-btn"
          @click="changeCollapse"
          :class="[{'el-icon-s-fold': !$store.state.dal.isListCollapse},
          {'el-icon-s-unfold': $store.state.dal.isListCollapse}]"
        />
      </div>
      <slot></slot>
    </el-main>
  </el-container>
</template>

<script>
import SearchList from './SearchList.vue'

export default {
  data () {
    return {
      List: [],
      initName: {
        employee: '斯卡蒂',
        enemy: '源石虫'
      },
      commitInstruct: {
        employee: 'em/changeEmployeeName',
        enemy: 'en/changeEnemyName'
      },
      disCommitList: {
        employee: ['★', '★★', '★★★', '★★★★', '★★★★★', '★★★★★★', '先锋', '狙击', '医疗', '术师', '近卫', '重装', '辅助', '特种'],
        enemy: ['普通', '精英', '领袖']
      }
    }
  },
  props: {
    viewMod: String
  },
  created () {
    this.getList()
    this.closeDrawer()
    this.initCollapse()
    this.changeName(this.initName[this.viewMod])
  },
  components: {
    SearchList
  },
  methods: {
    getList () {
      if (this.viewMod === 'enemy') {
        this.List = require('@/assets/data/enemylist.json')
      } else {
        this.List = require('@/assets/data/employeelist.json')
      }
    },
    changeName (name) {
      const disCommitList = this.disCommitList[this.viewMod]
      const isIn = disCommitList.indexOf(name)
      if (isIn === -1) {
        this.$store.commit(this.commitInstruct[this.viewMod], name)
      }
    },
    closeDrawer () {
      this.$store.commit('dal/closeDrawer')
    },
    initCollapse () {
      this.$store.commit('dal/initCollapse')
    },
    changeCollapse () {
      this.$store.commit('dal/changeCollapse')
    }
  }
}
</script>

<style lang="scss" scoped>
.el-button {
  font-size: 20px;
  color: rgba(64, 64, 64, .7)
}
.el-container {
  height: 100%;
  position: relative;
}
.el-aside {
  position: absolute;
  z-index: 1004;
  height: 100%;
  background-color: rgba(255, 255, 255, .98);
  box-sizing: border-box;
  padding: 1px;
  border-right: 1px solid #dcdfe6;
  // 动画
  transition: all 0.4s;
  -webkit-transform: translate(0, 0px);
  transform: translate(0, 0px);
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
  // 动画
  transition: all 0.4s;
  -webkit-transform: translate(-249px, 0px);
  transform: translate(-249px, 0px);
}
.is-aside-collapse {
  left: 0px !important;
  width: 100%;
}
.collapse-btn-box {
  width: 30px;
  height: 30px;
  position: fixed;
  text-align: right;
  box-sizing: border-box;
  // left: 249px;
  // 动画
  transition: all 0.4s;
  -webkit-transform: translate(0, 0);
  transform: translate(0, 0);
  top: 52px;
  z-index: 1004;
}
@media only screen and (max-width:1080px) {
  .el-main {
    left: 0px;
    width: 100%;
  }
  .collapse-btn-box {
    transition: all 0.4s;
    -webkit-transform: translate(248px, 0px);
    transform: translate(248px, 0px);
  }
}
@media only screen and (max-width:767px) {
  .collapse-btn-box {
    top: 46px;
  }
  .aside-width {
    width: 199px !important;
  }
  .collapse-btn-box {
    // left: 199px;
    -webkit-transform: translate(198px, 0px);
    transform: translate(198px, 0px);
  }
  .el-aside {
    -webkit-transform: translate(0, 0px);
    transform: translate(0, 0px);
  }
  .aside-collapse {
    -webkit-transform: translate(-199px, 0px);
    transform: translate(-199px, 0px);
  }
}
.btn-box-collapsed {
  // left: 1px;
  transition: all 0.4s;
  -webkit-transform: translate(0, 0);
  transform: translate(0, 0);
}
.collapse-btn {
  height: 30px;
  width: 30px;
  border: 0px solid transparent;
  padding: 0px;
  background-color: rgba(255, 255, 255, .8);
}
</style>
