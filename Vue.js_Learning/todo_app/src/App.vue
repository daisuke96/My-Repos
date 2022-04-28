<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
      <div>
      <router-link to="/TodoList">TodoList</router-link>
      <a>←HOME→</a>
      <router-link to="/MemoList">MemoList</router-link>
      </div>
      <router-view /> 
    
  </div>




</template>

<script>

export default {
  name: 'App'
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
