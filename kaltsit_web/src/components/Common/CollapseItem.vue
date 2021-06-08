<template>
  <div class="collapse-box">
    <div :class="getStyleClass()">
      <span>{{ compontentName }}</span>
      <button
        @click="isActive = !isActive"
        :class="{'el-icon-arrow-right': !isActive, 'el-icon-arrow-down': isActive}"
      />
    </div>
    <el-collapse-transition>
      <div v-if="isActive">
        <slot></slot>
      </div>
    </el-collapse-transition>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isActive: false
    }
  },
  props: {
    layer: {
      type: Number,
      default: 1
    },
    compontentName: String
  },
  methods: {
    getStyleClass () {
      if (this.layer === 1) {
        return 'collapse-title'
      } else if (this.layer === 2) {
        return 'class-collapse-title'
      } else if (this.layer === 3) {
        return 'skill-collapse-title'
      } else if (this.layer === 4) {
        return 'skill-class-collapse-title'
      } else if (this.layer === 5) {
        return 'skill-chart-collapse-title'
      }
    }
  }
}
</script>

<style lang="scss" scoped>
/* 抽屉样式 */
.collapse-box {
  border-top: 1px solid #ebeef5;
}
.skill-collapse-title,
.skill-class-collapse-title,
.skill-chart-collapse-title,
.class-collapse-title,
.collapse-title {
  display: flex;
  justify-content: space-between;
  box-sizing: border-box;
  button {
    border: 0px solid transparent;
    background-color: #fff;
    padding: 0px;
    color: #666;
  }
}
// first-layer
.collapse-title {
  height: 36px;
  span {
    line-height: 36px;
    font-weight: 700;
    padding-left: 13px;
    font-size: 17px;
    letter-spacing: 2px;
  }
  button {
    width: 36px;
    font-weight: 700;
    font-size: 15px;
  }
}
// second-layer
.class-collapse-title {
  height: 30px;
  span {
    line-height: 30px;
    font-weight: 600;
    padding-left: 20px;
    font-size: 15px;
    letter-spacing: 1px;
  }
  button {
    width: 30px;
    font-weight: 600;
    font-size: 13px;
    margin-right: 3px;
  }
}
// (second) skill-layer
.skill-collapse-title {
  height: 34px;
  span {
    line-height: 34px;
    font-weight: 600;
    padding-left: 16px;
    font-size: 16px;
    letter-spacing: 1px;
  }
  button {
    width: 34px;
    font-weight: 600;
    font-size: 14px;
    margin-right: 1px;
  }
}
// (third) skill-class-layer
.skill-class-collapse-title {
  height: 32px;
  span {
    line-height: 32px;
    font-weight: 600;
    padding-left: 20px;
    font-size: 15px;
    letter-spacing: 1px;
  }
  button {
    width: 32px;
    font-weight: 600;
    font-size: 13px;
    margin-right: 2px;
  }
}
// (forth) skill-chart-layer
.skill-chart-collapse-title {
  height: 30px;
  span {
    line-height: 30px;
    font-weight: 600;
    padding-left: 25px;
    font-size: 15px;
    letter-spacing: 1px;
  }
  button {
    width: 30px;
    font-weight: 600;
    font-size: 13px;
    margin-right: 3px;
  }
}
</style>
