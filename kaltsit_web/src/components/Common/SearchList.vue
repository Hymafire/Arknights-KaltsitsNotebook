<template>
  <el-container>
    <!-- 搜索栏 -->
    <el-header class="search-header">
      <el-input
        prefix-icon="el-icon-user"
        placeholder="输入查询名称"
        v-model="objName"
        class="search-input"
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
    <el-main class="list-main">
      <el-tree
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
.base-style {
  padding: 0;
  margin: 0;
}
.search-input {
  margin-top: 10px;
}
.search-header {
  height: 60px;
  padding: 5px;
}
.list-main {
  height: 100%;
  padding: 5px;
}
</style>
