<template>
  <!-- 敌人的基础信息 -->
  <div>
    <img id="en-img" :src="imgUrl" alt="Worry!"/>
    <ul>
      <li>
        <span>最大血量</span> {{ enemy.maxHp[0] }}
      </li>
      <li>
        <span>攻击</span> {{ enemy.atk[0] }}
      </li>
      <li>
        <span>防御</span> {{ enemy.def[0] }}
      </li>
      <li>
        <span>法抗</span> {{ enemy.magRes[0] }}
      </li>
      <li>
        <span>移速</span> {{ enemy.moveSpd }}
      </li>
      <li>
        <span>攻击间隔</span> {{ enemy.atkTime }}s
      </li>
      <li>
        <span>生命回复</span> {{ enemy.hpRec }}/s
      </li>
      <li>
        <span>重量</span> {{ enemy.massLevel }}
      </li>
      <li>
        <span>射程</span> {{ enemy.rangeRadius }}
      </li>
    </ul>
    {{ enemy }}
  </div>
</template>

<script>
export default {
  name: 'BaseInfo',
  computed: {
    enemy () {
      return this.$store.state.en.enData
    },
    imgUrl: function () {
      const Key = this.$store.state.en.enKey
      return require('../../../assets/images/enimgs/' + Key + '.png')
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
