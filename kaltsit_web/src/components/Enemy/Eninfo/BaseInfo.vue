<template>
  <!-- 敌人的基础信息 -->
  <div>
    <img id="en-img" :src="imgUrl" alt="Worry!"/>
    <ul>
      <li>
        <span>最大血量</span> {{ enemyParams.maxHp[0] }}
      </li>
      <li>
        <span>攻击</span> {{ enemyParams.atk[0] }}
      </li>
      <li>
        <span>防御</span> {{ enemyParams.def[0] }}
      </li>
      <li>
        <span>法抗</span> {{ enemyParams.magRes[0] }}
      </li>
      <li>
        <span>移速</span> {{ enemyParams.moveSpd }}
      </li>
      <li>
        <span>攻击间隔</span> {{ enemyParams.atkTime }}s
      </li>
      <li>
        <span>生命回复</span> {{ enemyParams.hpRec }}/s
      </li>
      <li>
        <span>重量</span> {{ enemyParams.massLevel }}
      </li>
      <li>
        <span>射程</span> {{ enemyParams.rangeRadius }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'BaseInfo',
  props: {
    enemyParams: Object,
    enemyKey: String
  },
  computed: {
    imgUrl: function () {
      return require('../../../assets/images/enimgs/' + this.enemyKey + '.png')
    }
  }
}
</script>

<style lang="scss" scoped>
#en-img {
  display: inline-block;
  height: 100px;
  width: 100px;
}
div {
  padding: 3px;
  // 属性标题
  span {
    display: inline-block;
    height: 25px;
    width: 85px;
    font-weight: 700;
    line-height: 25px;
    text-align: center;
    background-color: rgba(172, 255, 47, 0.6);
    border-radius: 2px;
    box-shadow: 2px 2px 5px -2px rgba(0, 0, 0, 0.3);
    margin-right: 10px;
    margin-top: 3px;
  }
}
</style>
