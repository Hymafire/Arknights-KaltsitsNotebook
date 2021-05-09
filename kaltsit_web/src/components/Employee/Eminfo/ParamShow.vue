<template>
  <div id="param-show">
    <ul>
      <li>
        <span>最大生命</span>
        <span>{{showParam.maxHp}}</span>
      </li>
      <li>
        <span>攻击</span>
        <span>{{showParam.atk}}</span>
      </li>
      <li>
        <span>防御</span>
        <span>{{showParam.def}}</span>
      </li>
      <li>
        <span>法抗</span>
        <span>{{showParam.magRes}}</span>
      </li>
      <li>
        <span>部署费用</span>
        <span>{{showParam.cost}}</span>
      </li>
      <li>
        <span>阻挡数</span>
        <span>{{showParam.block}}</span>
      </li>
      <li>
        <span>攻击间隔</span>
        <span>{{showParam.atkTime}}</span>
      </li>
      <li>
        <span>在部署时间</span>
        <span>{{showParam.respawnTime}}</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ParamShow',
  props: {
    showParam: Array,
    showHp: Number
  },
  watch: {
    showParam: {
      handler () {
        console.log(this.showParam)
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style>

</style>
