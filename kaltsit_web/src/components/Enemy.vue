<template>
  <el-container class="home-container">
    <!-- 敌方列表和查询区 -->
    <el-aside width="250px" class="home-aside">
      <Enlist v-bind:enemy_name="enemy_name" v-on:enemyChanged="changeName($event)" />
    </el-aside>
    <!--  属性输出区  -->
    <el-main>
      <Eninfo :enemy_name="enemy_name" />
    </el-main>
  </el-container>
</template>

<script>
import Enlist from './Enemy/Enlist.vue'
import Eninfo from './Enemy/Eninfo.vue'

export default {
  data () {
    return {
      enemy_name: '源石虫'
    }
  },
  created () {
  },
  mounted () {
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
.home-container {
  height: 100%;
}
.home-aside {
  padding: 0px;
}
.el-aside {
  background-color: #fff;
  width: 100%;
  height: 100%;
  padding: 1px;
}
.el-main {
  background-color: #fff;
  padding: 1px;
}
</style>
