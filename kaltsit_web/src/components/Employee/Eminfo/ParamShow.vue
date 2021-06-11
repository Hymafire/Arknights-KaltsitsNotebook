<template>
  <div id="param-show">
    <div>
      <strong>最大生命</strong>
      <span>{{ showParam.maxHp }}<i v-if="upParam.maxHp != 0"> (+{{ upParam.maxHp }})</i></span>
    </div>
    <div>
      <strong>攻击</strong>
      <span>{{ showParam.atk }}<i v-if="upParam.atk != 0"> (+{{ upParam.atk }})</i></span>
    </div>
    <div>
      <strong>防御</strong>
      <span>{{ showParam.def }}<i v-if="upParam.def != 0"> (+{{ upParam.def }})</i></span>
    </div>
    <div>
      <strong>法抗</strong>
      <span>{{ showParam.magRes }}<i v-if="upParam.magRes != 0"> (+{{ upParam.magRes }})</i></span>
    </div>
    <div>
      <strong>部署费用</strong>
      <span>{{ showParam.cost }}<i v-if="upParam.cost != 0"> ({{ upParam.cost }})</i></span>
    </div>
    <div>
      <strong>阻挡数</strong>
      <span>{{ showParam.blockCnt }}<i v-if="upParam.blockCnt != 0"> (+{{ upParam.blockCnt }})</i></span>
    </div>
    <div>
      <strong>攻击间隔</strong>
      <span>{{ showParam.atkTime }}<i v-if="upParam.atkTime != 0"> ({{ upParam.atkTime }})</i> s</span>
    </div>
    <div>
      <strong>在部署时间</strong>
      <span>{{ showParam.respawnTime }}<i v-if="upParam.respawnTime != 0"> ({{ upParam.respawnTime }})</i> s</span>
    </div>
  </div>
</template>

<script>
import { emParamUpCalc } from '../../utils/baseCalc.js'

export default {
  name: 'ParamShow',
  computed: {
    showParam () {
      return this.$store.state.em.emParam
    },
    upParam () {
      return emParamUpCalc(this.$store.state.em.emData, this.$store.state.em.emInputParam)
    }
  }
}
</script>

<style lang="scss" scoped>
#param-show {
  width: 48%;
  max-width: 220px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  flex: 1;
  min-width: auto;
  > div {
    box-sizing: border-box;
    flex-wrap: nowrap;
    height: 50px;
    width: 48%;
    max-width: 220px;
    padding: 2px 2px;
  }
  strong {
    display: inline-block;
    box-sizing: border-box;
    text-align: center;
    margin: 0px 10px;
    // padding: 10px 0px;
  }
  span {
    margin-left: 10px;
    display: inline-block;
    text-align: left;
  }
  i {
    font-style: normal;
    color: #f49800;
  }
}
@media only screen and (max-width:450px){
  #param-show {
    width: 100%;
  }
}
</style>
