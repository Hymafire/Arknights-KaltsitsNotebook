<template>
  <el-container class="searchlist-color">
    <!-- 搜索栏 -->
    <el-header class="search-header" height="50px">
      <el-input
        prefix-icon="el-icon-user"
        placeholder="输入查询名称"
        v-model="objName"
        class="search-input"
        maxlength="20"
      >
        <el-button
          slot="append"
          icon="el-icon-search"
          @click="searchName"
          class="search-btn"
        />
      </el-input>
    </el-header>
    <!-- 搜索栏-end -->
    <!-- 列表栏 -->
    <el-main class="list-main searchlist-color">
      <el-tree
        class="searchlist-color"
        :data="listData"
        :props="proplist"
        @node-click="handleNodeClick"
        highlight-current
        accordion
      />
    </el-main>
    <!-- 列表栏-end -->
  </el-container>
</template>

<script>
export default {
  name: 'SearchList',
  data () {
    return {
      proplist: {
        label: 'name',
        children: 'children'
      },
      objName: ''
    }
  },
  props: {
    listData: Array
  },
  methods: {
    handleNodeClick (data) {
      this.$emit('objChanged', data.name)
    },
    searchName () {
      this.$emit('objChanged', this.objName)
    }
  }
}
</script>

<style lang="scss" scoped>
.searchlist-color {
  background-color: transparent;
}
.search-input {
  margin-top: 10px;
}
.search-header {
  padding: 5px;
  padding-top: 0px;
}
.list-main {
  height: 100%;
  padding: 5px;
}
.search-btn {
  padding: 0px;
  margin: 0 auto;
}
/deep/.el-input-group__append {
  padding: 0px 15px;
}
</style>
