<template>
  <el-container>
    <!-- 敌方列表和查询区 -->
    <el-aside width="250px">
      <Emlist :employee_name="employee_name" @employeeChanged="changeName($event)" />
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <Eminfo :employee_name="employee_name" />
    </el-main>
  </el-container>
</template>

<script>
import Emlist from '../components/Employee/Emlist.vue'
import Eminfo from '../components/Employee/Eminfo.vue'

export default {
  data () {
    return {
      employee_name: '斯卡蒂'
    }
  },
  components: {
    Emlist,
    Eminfo
  },
  methods: {
    changeName (name) {
      this.employee_name = name
    }
  }
}
</script>

<style lang="scss" scoped>
.el-aside {
  height: 100%;
  width: 100%;
  padding: 0px;
  background-color: #fff;
}
.el-main {
  left: 250px;
  background-color: #e2e2e2;
  padding: 1px;
}
</style>
