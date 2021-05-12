import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import './registerServiceWorker'
import './assets/styles/styles.scss'
import './plugins/element.js'
import './assets/css/global.css'

Vue.use(ElementUI)

Vue.config.productionTip = false

Vue.prototype.$getViewportSize = function () {
  return {
    width: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
    height: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
  }
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
