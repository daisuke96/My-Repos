<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <hr>
    <div>
      <!--入力欄をv-modelでバインディング-->
      <div><textarea v-model="fomula" cols="40" row="5"></textarea></div>
      <!--計算ボタンクリック時にメソッドを発火-->
      <div><button @click="doAction">CALC</button></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CALC',
  data(){
    return{
      fomula: '0',
      message: 'enter expression',
    }
  },
  props: {
    title: String
  },
  methods:{
    doAction(){
      console.log('【doAction】')
      console.log('fomula: ' + this.fomula)
      //入力欄のデータを改行で分割、textareaは一つのデータになっている
      var arr = this.fomula.trim().split('\n');
      console.log('arr::' + arr);
      //最後の要を取り除き、lastに格納
      var last = arr.pop();
      //fnにテキストとして関数を作成
      var fn = '';
      for (var n in arr){
        console.log('arr[n].trim()::' + arr[n].trim());
        if (arr[n].trim() != ''){
          fn += 'var ' + arr[n] + ';';
        }
      }
      console.log('fn::' + fn)
      fn += 'return ' + last + ';';
      var exp = 'function f(){' + fn + '} f();';
      console.log('exp::'+exp);
      var ans = eval(exp);
      console.log('ans::'+ ans);
      this. message = 'answer: '+ ans;
      var re = arr.join(';').trim();
      console.log('re::' + re);
      if (re != ''){
        re += ';'
      }
      re += last;
      //計算式と答えを全て親コンポーネントに送信
      this.$emit('result-event', re, ans);

    }
  }
}
</script>




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
</style>
