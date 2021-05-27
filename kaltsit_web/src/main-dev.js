import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import './registerServiceWorker'
import './assets/styles/styles.scss'
import './assets/styles/global.scss'
import './plugins/element.js'

Vue.use(ElementUI)

Vue.config.productionTip = false
Vue.config.performance = true

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
