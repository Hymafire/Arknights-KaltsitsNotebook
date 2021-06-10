<template>
  <div id="param-show">
    <ul>
      <li>
        <strong>最大生命</strong>
        <span>{{ showParam.maxHp }}<i v-if="upParam.maxHp != 0"> (+{{ upParam.maxHp }})</i></span>
      </li>
      <li>
        <strong>攻击</strong>
        <span>{{ showParam.atk }}<i v-if="upParam.atk != 0"> (+{{ upParam.atk }})</i></span>
      </li>
      <li>
        <strong>防御</strong>
        <span>{{ showParam.def }}<i v-if="upParam.def != 0"> (+{{ upParam.def }})</i></span>
      </li>
      <li>
        <strong>法抗</strong>
        <span>{{ showParam.magRes }}<i v-if="upParam.magRes != 0"> (+{{ upParam.magRes }})</i></span>
      </li>
      <li>
        <strong>部署费用</strong>
        <span>{{ showParam.cost }}<i v-if="upParam.cost != 0"> ({{ upParam.cost }})</i></span>
      </li>
      <li>
        <strong>阻挡数</strong>
        <span>{{ showParam.blockCnt }}<i v-if="upParam.blockCnt != 0"> (+{{ upParam.blockCnt }})</i></span>
      </li>
      <li>
        <strong>攻击间隔</strong>
        <span>{{ showParam.atkTime }}<i v-if="upParam.atkTime != 0"> ({{ upParam.atkTime }})</i> s</span>
      </li>
      <li>
        <strong>在部署时间</strong>
        <span>{{ showParam.respawnTime }}<i v-if="upParam.respawnTime != 0"> ({{ upParam.respawnTime }})</i> s</span>
      </li>
    </ul>
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
      // const upParam = emParamUpCalc(this.$store.state.em.emData, this.$store.state.em.emInputParam)
      return emParamUpCalc(this.$store.state.em.emData, this.$store.state.em.emInputParam)
    }
  }
}
</script>

<style lang="scss" scoped>
#param-show {
  min-width: 370px;
  display: flex;
  flex: 1;
  ul {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }
  li {
    box-sizing: border-box;
    height: 50px;
    width: 48%;
    max-width: 220px;
    padding: 2px 2px;
  }
  strong {
    display: inline-block;
    height: 30px;
    width: 84px;
    line-height: 30px;
    text-align: center;
    margin: 0px 10px;
    padding: 10px 0px;
  }
  span {
    margin-left: 10px;
  }
  i {
    font-style: normal;
    color: #f49800;
  }
}
//
.hidden-style {
  height: 0px;
  width: 0px;
  font-size: 0px;
  color: transparent;
}
@media only screen and (max-width:450px){
  #param-show {
    width: 100%;
  }
}
</style>
