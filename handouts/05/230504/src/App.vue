<template>
  <div id="app">
    app.vue
    <button @click="fetchCats">클릭</button>

    <!-- <img 
      v-for="(catUrl, index) in cats" 
      :key="index"
      :src="catUrl" 
    > -->
    <CatImg
      v-for="(catUrl, index) in cats" 
      :key="index"
      :catUrl="catUrl"
    />

  </div>
</template>

<script>
import CatImg from './components/CatImg.vue'

export default {
  name: 'App',
  components: {
    CatImg
  },
  methods:{
    fetchCats(){
      // state를 변경하고 싶은 거거든요?
      // cats라고 하는 state를 axios 요청을 통해서 채우고 싶음
      const a = 10
      const b= 100
      const c= 1000
      const payload = {
        a,
        b,
        c
      }
      this.$store.dispatch('fetchCats', payload)


    }
  },
  computed:{
    cats(){
      return this.$store.state.cats
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
