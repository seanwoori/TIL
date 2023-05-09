<template>
  <img :src="catUrl" alt="">
</template>

<script>
export default {
  name:"CatImg",
  props:{
    catUrl : String
  }
}
</script>

<style>
  img{
    width: 100px;
    height: 100px;
  }
</style>