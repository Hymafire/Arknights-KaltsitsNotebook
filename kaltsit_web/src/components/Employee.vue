<template>
  <el-container class="home-container">
    <!-- 敌方列表和查询区 -->
    <el-aside width="250px" class="home-aside">
      <Emlist v-bind:employee_name="employee_name" v-on:employeeChanged="changeName($event)" />
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <Eminfo :employee_name="employee_name" />
    </el-main>
  </el-container>
</template>

<script>
import Emlist from './Employee/Emlist.vue'
import Eminfo from './Employee/Eminfo.vue'

export default {
  data () {
    return {
      employee_name: '斯卡蒂'
    }
  },
  created () {
  },
  mounted () {
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
.home-container {
  height: 100%;
}
.home-aside {
  padding: 0px;
}
.el-aside {
  display: block;
  height: 100%;
  background-color: #fff;
  width: 100%;
}
.el-main {
  // height: 100%;
  // position: absolute;
  left: 250px;
  background-color: #e2e2e2;
  padding: 1px;
  // overflow-y: scroll;
}
</style>
