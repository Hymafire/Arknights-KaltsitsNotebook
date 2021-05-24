<template>
  <div id="damage-class">
    <!--
    <el-collapse v-model="activeName" class="collapse-title">
      <el-collapse-item title="伤害类排名" name="1">
        <RankRadar />
      </el-collapse-item>
      <el-collapse-item title="秒伤害量" name="2">
        <PerDamage
          :atk="emParam.atk"
          :atkTime="emParam.atkTime"
          :isActive="isActive('1')"
        />
      </el-collapse-item>
      <el-collapse-item title="总伤害量" name="3">
        <DamageTotal
          :avgDef="pretreated.enAvgDef"
          :atk="emParam.atk"
          :atkTime="emParam.atkTime"
          :isActive="isActive('2')"
        />
      </el-collapse-item>
    </el-collapse>
    -->
    <PerDamage
      :atk="emParam.atk"
      :atkTime="emParam.atkTime"
      :isActive="isActive('1')"
    />
  </div>
</template>

<script>
// import DamageTotal from '../../Echarts/DamageClass/DamageTotal.vue'
import PerDamage from '../../Echarts/DamageClass/PerDamage.vue'
// import RankRadar from '../../Echarts/RankClass/RankRadar.vue'

export default {
  name: 'DamageClass',
  data () {
    return {
      activeName: []
    }
  },
  props: {
    employeeName: String,
    emParam: Array,
    pretreated: Array,
    isClassActive: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    emParamTmp: function () {
      return this.emParam
    }
  },
  components: {
    // DamageTotal,
    PerDamage
    // RankRadar
  },
  methods: {
    // 判断折叠面板是否处于激活状态
    isActive (name) {
      for (let i = 0; i < this.activeName.length; i++) {
        if (name === this.activeName[i]) {
          return true
        }
      }
      return false
    }
  },
  watch: {
    emParamTmp: {
      handler () {
        this.$forceUpdate()
      },
      deep: true
    }
  }
}
</script>

<style lang="scss" scroped>
.collapse-title {
  height: 30px;
}
//
/deep/.el-collapse-item__header {
  height: 39px;
  font-size: 16px;
  font-weight: 700;
  padding-left: 20px;
  letter-spacing: 2px;
}
//
/deep/.el-collapse-item__content {
  padding: 0px;
}
</style>
