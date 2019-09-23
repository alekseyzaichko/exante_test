import Vue from 'vue'
import Vuex from 'vuex'

import VueRouter from 'vue-router'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(VueRouter)

import App from './App.vue'
import NewsList from './components/NewsList.vue'
import NewsDetails from './components/NewsDetails.vue'

const store = new Vuex.Store({
  state: {
    categoryList: {},
    newsList: [],
    currentCategoryId: 0,
    currentNewsId: 0
  },
  mutations: {
    initCategoryList (state, payload) {
      state.categoryList = payload
    },
    updateNewsList (state, payload) {
      state.newsList = payload
    }
  },
  actions: {
  }
})


const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/', name: 'mainPage', component: NewsList },
    { path: '/:categorySlug/', name: 'byCategory', component: NewsList },
    { path: '/:categorySlug/:newsId/', name: 'newsDetails', component: NewsDetails }
  ]
})

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
