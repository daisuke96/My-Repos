<template>
  <div class="hello">
    <h1>{{title}}</h1>
    <pre @click="clear">{{ message }}</pre>
    <hr>
    <!--C＞B>Aの順（上・中・下）で重なっている
        イベントは上から下へ流れる-->
    <div id="out" class="out" @click="a_event">A
      <div id="mid" class="mid" @click.self="b_event">B
      <div id="in" class="in" @click="c_event">C
      </div>
      </div>
    </div>
    <hr>
    <div>キー入力<input type="text"
      @keypress="type"
      @keydown.delete="clear"
      @keydown.space="space"
      @keydown.enter="enter">
    </div>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    title: String,
  },
  data(){
    return {
      message: '',
    }
  },
  methods:{
    //イベント発生要素→イベントハンドラ登録要素
    a_event(event){
      this.message += "a-event ["+ event.target.id + ' → ' + event.currentTarget.id + "]\n";
    },
    b_event(event){
      this.message += "b-event ["+ event.target.id + ' → ' + event.currentTarget.id + "]\n";
    },
    c_event(event){
      this.message += "c-event ["+ event.target.id + ' → ' + event.currentTarget.id + "]\n";
    },
    clear(){
      this.message='';
    },
    type(event){
        if (event.key == "Enter"){return;}
      this.message += event.key + ' ';

      event.target.value = '';
    },
    space(){
      this.message += '_ ';
    },
    enter(event){
      var res = this.message.split(' ').join('');
      this.message = res.split('_').join(' ');
      event.target.value = '';
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
pre {
  font-size: 14pt;
  line-height: 1.25;
}
div.out {
  padding: 5px 0px;
  background-color: #eee;
  width: 300px;
  height: 200px;
}
div.mid {
  padding: 5px 0px;
  background-color: #ddd;
  width: 200px;
  height: 175px;
}
div.in {
  padding: 5px 0px;
  background-color: #ccc;
  width: 100px;
  height: 150px;
}



</style>
