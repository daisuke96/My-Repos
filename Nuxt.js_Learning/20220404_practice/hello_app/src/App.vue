<template>
  <div id="app">
    <!--propsで定義した属性に値を付与, APPのdataを使う場合はv-bindを使用-->
    <!--<HelloWorld title="parent → child" :num="num"></HelloWorld>-->
    <HelloWorld :title="newTitle" @input-msg="sendMessage" ></HelloWorld>
    <hr>
    <button @click="doChange" >change title</button>
    <hr>
    <p>Message from child comp : {{ result }}</p>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data(){
    return{
      newTitle:'Hello',
      result:'',
      num: 10,
    }
    
  },
  components: {
    HelloWorld
  },
  methods:{
    doChange(){
      console.log('change')
      //prompt()でテキストダイアログを表示
      var input = prompt("New Title:");
      this.newTitle = input; 
    },
    sendMessage(msg){
      console.log('emit')
      this.result = msg;
    }

  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
  margin-top: 60px;
}
</style>
