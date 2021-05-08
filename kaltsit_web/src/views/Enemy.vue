<template>
  <el-container>
    <!-- 敌方列表和查询区 -->
    <el-aside width="250px">
      <Enlist :enemy_name="enemy_name" @enemyChanged="changeName" />
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <Eninfo :enemy_name="enemy_name" />
    </el-main>
  </el-container>
</template>

<script>
import Enlist from '../components/Enemy/Enlist.vue'
import Eninfo from '../components/Enemy/Eninfo.vue'

export default {
  data () {
    return {
      enemy_name: '源石虫'
    }
  },
  components: {
    Enlist,
    Eninfo
  },
  methods: {
    changeName (name) {
      this.enemy_name = name
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
</style>
