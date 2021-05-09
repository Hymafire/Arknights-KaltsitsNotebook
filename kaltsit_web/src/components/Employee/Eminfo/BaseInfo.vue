<template>
  <div class="base-info card-style">
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
    <div id="range-show">
      射程展示
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseInfo',
  data () {
    return {
      baseInfo: {
        elite: 0,
        potentialLevel: 0,
        levelValue: 1,
        favorValue: 100
      }
    }
  },
  props: {
    potential: Number,
    maxLevel: Array,
    showParam: Array
  },
  methods: {
    submitInfo () {
      this.$emit('submitInfo', this.baseInfo)
    },
    eliteClick (elt) {
      this.baseInfo.elite = elt
    },
    potClick (pot) {
      this.baseInfo.potentialLevel = pot
    }
  },
  watch: {
    baseInfo: {
      handler () {
        this.submitInfo()
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style lang="scss" scoped>
.base-info {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  >div {
    text-align: left;
    min-width: 360px;
    height: 160px;
    margin-left: 10px;
  }
}
// 卡片
.card-style {
  margin-bottom: 5px;
  background-color: white;
  border: 1px solid #ebeef5;
  border-radius: 4px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.15);
}
</style>
