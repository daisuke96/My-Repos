<template>
  <div id="app">
    <calc :title="message" @result-event="appAction"></calc>
    <hr>
    <div><table v-html="log"></table></div>
  </div>
</template>

<script>
import calc from './components/calc.vue'

export default {
  name: 'App',
  components: {
    calc
  },
  data(){
    return{
      message: 'CALC',
      result: [],
    };
  },
  computed:{
    //算出プロパティで常にテーブルを監視
    log(){
      var table = '<tr><th class="head">Expression</th><th class="head">Value</th></tr>';
      for(var i in this.result){
        table += '<tr><td>' + this.result[i][0] + '</td><th>' + this.result[i][1] + '</th></tr>';
      }
      return table;
    }
  },

  created: function(){
    console.log('【created start】')
    var items = localStorage.getItem('log');
    console.log('★items::'+items)
    var logs = JSON.parse(items);
    console.log('logs::'+logs)
    //result=テーブルにストレージデータを格納
    if (logs != null){ this.result = logs; }

  },

  methods:{
    appAction(exp, res){
      console.log('【appAction】exp,res::'+exp+'&'+res)
      this.result.unshift([exp, res]);
      if(this.result.length > 10){
        this.result.pop();
      }
      var log = JSON.stringify(this.result);
      console.log('result::'+this.result)
      console.log('log::'+log)
      localStorage.setItem('log', log);

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 5px;
}
tr td {
  padding: 5px;
  border:1px solid gray;
}
tr th {
  padding: 5px;
  border:1px solid gray;
}
tr th.head {
  background-color: blue;
  color: white;
}
</style>
