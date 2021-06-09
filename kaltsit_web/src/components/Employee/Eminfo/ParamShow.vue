<template>
  <div id="param-show">
    <ul>
      <li>
        <strong>最大生命</strong>
        <span>{{ showParam.maxHp }}</span>
      </li>
      <li>
        <strong>攻击</strong>
        <span>{{ showParam.atk }}</span>
      </li>
      <li>
        <strong>防御</strong>
        <span>{{ showParam.def }}</span>
      </li>
      <li>
        <strong>法抗</strong>
        <span>{{ showParam.magRes }}</span>
      </li>
      <li>
        <strong>部署费用</strong>
        <span>{{ showParam.cost }}</span>
      </li>
      <li>
        <strong>阻挡数</strong>
        <span>{{ showParam.blockCnt }}</span>
      </li>
      <li>
        <strong>攻击间隔</strong>
        <span>{{ showParam.atkTime }}s</span>
      </li>
      <li>
        <strong>在部署时间</strong>
        <span>{{ showParam.respawnTime }}s</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ParamShow',
  computed: {
    showParam () {
      return this.$store.state.em.emParam
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
