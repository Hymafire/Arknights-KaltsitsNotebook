<template>
  <div>
    <div class="baseinfo-container">
      <img id="en-img" :src="imgUrl" alt="Worry!"/>
      <div style="display: inline-block">
        <h2>
          <span>{{ enData.enemyIndex }}</span>
          {{ enData.name }}
        </h2>
        <h4>{{ enData.enemyRace }}</h4>
        <div class="class-box">
          <span>{{ enData.endure }}</span>
          <span>{{ enData.attack }}</span>
          <span>{{ enData.defence }}</span>
          <span>{{ enData.resistance }}</span>
        </div>
      </div>
    </div>
    <div>
      <h4>描述：</h4>
      <div>{{ enData.description }}</div>
    </div>
    <div v-if="enData.ability !== null">
      <h4>能力：</h4>
      <div>{{ enData.ability }}</div>
    </div>
    <div v-if="enData.talentBlackboard !== null">
      <h4>天赋：</h4>
      <div>{{ enData.talentBlackboard }}</div>
    </div>
    <div>
      <h4>属性：</h4>
      <div class="paraminfo-container">
        <div v-for="param in showList" :key="param" class="param-box">
          <h5>{{ enParamList[param] }}</h5>
          <div>{{ enData[param] }}</div>
        </div>
        <div class="immune-box"></div>
      </div>
    </div>
    <div v-if="enData.skills !== null">
      <h4>技能：</h4>
      <div>{{ enData.skills }}</div>
    </div>
    <hr>
    <div>{{ enData }}</div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      showList: ['maxHp', 'atk', 'def', 'magRes', 'atkTime', 'moveSpd', 'hpRec', 'spRec', 'rangeRadius', 'massLv', 'lifePointReduce']
    }
  },
  computed: {
    enData () {
      return this.$store.state.en.enData
    },
    imgUrl: function () {
      let imgUrl = null
      const Key = this.$store.state.en.enKey
      try {
        imgUrl = require('../../../assets/images/enimgs/' + Key + '.png')
      } catch {}
      return imgUrl
    },
    enParamList () {
      const enParamLists = require('../../../assets/locales/en_param_list.json')
      const local = this.$store.state.loc.localesId
      return enParamLists[local]
    }
  }
}
</script>

<style lang="scss" scoped>
.baseinfo-container {
  display: flex;
  justify-content: space-around;
  margin-top: 2px;
}
#en-img {
  display: inline-block;
  height: 100px;
  width: 100px;
}
h2 {
  margin-bottom: 3px;
  span{
    height: 20px;
    width: 20px;
    font-size: 18px;
    border: 5px solid #ccc;
  }
}
.class-box {
   span {
    display: inline-block;
    margin: 0 5px;
    height: 50px;
    width: 50px;
    background-color: #ddd;
  }
}
</style>
