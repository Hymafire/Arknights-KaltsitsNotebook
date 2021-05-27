<template>
  <el-container>
    <!-- 干员列表和查询区 -->
    <el-aside class="aside-width" :class="{'aside-collapse': $store.state.isListCollapse}">
      <SearchList
        :list-data="employeeList"
        @objChanged="changeName"
      />
    </el-aside>
    <!--  属性输出区  -->
    <el-main :class="{'is-aside-collapse': $store.state.isListCollapse}">
      <div class="collapse-btn-box" :class="{'btn-box-collapsed': $store.state.isListCollapse}">
        <el-button
          class="collapse-btn"
          @click="changeCollapse"
          :class="[{'el-icon-s-fold': !$store.state.isListCollapse},
          {'el-icon-s-unfold': $store.state.isListCollapse}]"
        />
      </div>
      <Eminfo/>
    </el-main>
  </el-container>
</template>

<script>
import SearchList from '../components/Common/SearchList.vue'
import Eminfo from '../components/Employee/Eminfo.vue'

export default {
  data () {
    return {
      employeeList: []
    }
  },
  created () {
    this.getEmployeeList()
    this.closeDrawer()
    this.initCollapse()
  },
  components: {
    SearchList,
    Eminfo
  },
  methods: {
    getEmployeeList () {
      this.employeeList = require('@/assets/data/employeelist.json')
    },
    changeName (name) {
      this.$store.commit('changeEmployeeName', name)
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
  z-index: 1003;
  height: 100%;
  background-color: rgba(255, 255, 255, .98);
  box-sizing: border-box;
  padding: 1px;
  border-right: 1px solid #dcdfe6;
  // 动画
  transition: all 0.4s;
  -webkit-transform: translate(0, -1px);
  transform: translate(0, -1px);
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
  -webkit-transform: translate(-249px, -1px);
  transform: translate(-249px, -1px);
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
  z-index: 1003;
}
@media only screen and (max-width:1080px) {
  .el-main {
    left: 0px;
    width: 100%;
  }
  .collapse-btn-box {
    transition: all 0.4s;
    -webkit-transform: translate(248px, -1px);
    transform: translate(248px, -1px);
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
    -webkit-transform: translate(0, -1px);
    transform: translate(0, -1px);
  }
  .aside-collapse {
    -webkit-transform: translate(-199px, -1px);
    transform: translate(-199px, -1px);
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
