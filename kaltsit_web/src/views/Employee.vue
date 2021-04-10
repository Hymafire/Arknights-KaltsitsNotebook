<template>
  <el-container class="home-container">
    <!--  左  -->
    <el-aside width="200px" class="home-aside" >
      <el-input prefix-icon="el-icon-user" />
      <el-tree :props="props" :load="loadNode" lazy show-checkbox> </el-tree>
    </el-aside>
    <!--  主体  -->
    <el-main>Main</el-main>
  </el-container>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      props: {
        label: 'name',
        children: 'zones'
      },
      count: 1
    }
  },
  methods: {
    handleCheckChange (data, checked, indeterminate) {
      console.log(data, checked, indeterminate)
    },
    handleNodeClick (data) {
      console.log(data)
    },
    loadNode (node, resolve) {
      if (node.level === 0) {
        return resolve([{ name: '★★★★★★' }, { name: '★★★★★' }, { name: '★★★★' }, { name: '★★★' }, { name: '★★' }, { name: '★' }])
      }
      if (node.level > 3) return resolve([])

      var hasChild
      if (node.level === 1) {
        return resolve([{ name: '近卫' }, { name: '医疗' }])
      }
      /*
      if (node.data.name === 'region1') {
        hasChild = true
      } else if (node.data.name === 'region2') {
        hasChild = false
      } else {
        hasChild = Math.random() > 0.5
      }
*/
      setTimeout(() => {
        var data
        if (hasChild) {
          data = [
            {
              name: 'zone' + this.count++
            },
            {
              name: 'zone' + this.count++
            }
          ]
        } else {
          data = []
        }

        resolve(data)
      }, 500)
    }
  }
}
</script>

<style lang="scss" scoped>
.home-container {
  height: 100%;
}
.home-aside {
}
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  color: #fff;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}
.el-aside {
  background-color: #333744;
}
.el-main {
  background-color: #eaedf1;
}
</style>
