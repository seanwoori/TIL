import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const axios = require('axios');

export default new Vuex.Store({
  state: {
    cats : [],
  },
  getters: {
  },
  mutations: {
    CHANGE_CATS(state, catsList){
      state.cats = catsList
    }
  },
  actions: {
    fetchCats(context, payload){
      const {a, b, c} = payload
      console.log(a)
      console.log(b)
      console.log(c)
      
      const url = 'https://api.thecatapi.com/v1/images/search?limit=10'
      axios.get(url)
      .then(res => {
        // state를 변경하고 싶어.
        const catsList = res.data.map(el => el.url)

        context.commit('CHANGE_CATS', catsList)
      })
    }
  },
  modules: {
  }
})
