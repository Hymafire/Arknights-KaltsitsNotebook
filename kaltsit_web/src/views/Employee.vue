<template>
  <el-container>
    <!-- 干员列表和查询区 -->
    <el-aside width="249px" :class="{'aside-collapse': $store.state.isListCollapse}">
      <SearchList
        :list-data="employeeList"
        @objChanged="changeName"
      />
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <Eminfo :employee_name="employee_name" />
    </el-main>
  </el-container>
</template>

<script>
import SearchList from '../components/Common/SearchList.vue'
import Eminfo from '../components/Employee/Eminfo.vue'

export default {
  data () {
    return {
      employee_name: '斯卡蒂',
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
    changeName (name) {
      this.employee_name = name
    },
    getEmployeeList () {
      this.employeeList = require('@/assets/data/employeelist.json')
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
  padding: 1px;
  background-color: #fff;
}
.el-main {
  background-color: #fff;
  padding: 1px;
}
.aside-collapse {
  display: none !important;
}
</style>
