<template>
  <div id="param-show">
    <ul class="show-container">
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
      return emParamUpCalc(this.$store.state.em.emData, this.$store.state.em.emInputParam)
    }
  }
}
</script>

<style lang="scss" scoped>
#param-show {
  display: flex;
  height: 200px;
  flex: 1.2;
}
.show-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
li {
  display: flex;
  flex-wrap: wrap;
  width: 49%;
}
strong {
  display: inline-block;
  box-sizing: border-box;
  text-align: center;
  width: 100%;
  min-width: 80px;
}
span {
  display: inline-block;
  text-align: center;
  width: 100%;
}
i {
  font-style: normal;
  color: #f49800;
}
@media only screen and (max-width: 767px) {
  strong {
    margin-bottom: 2px;
  }
}
@media only screen and (min-width: 769px) {
  strong {
    width: 40%;
  }
  span {
    margin-left: 10px;
    width: 40%;
    min-width: 100px;
    text-align: left;
  }
  li {
    justify-content: space-around;
  }
}
@media only screen and (max-width: 360px) {
  span {
    font-size: 14px;
  }
}
</style>
