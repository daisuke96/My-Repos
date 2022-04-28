<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <hr>
    <div>
      <input type="text" v-model="input">
      <button @click="doClick();">click</button>
    </div>
    <hr>
    <p>Number: {{ num }}</p>
    <p>val:{{ val }}</p>
    <div>*2: <input type="number" v-model="propA"></div>
    <div>^2: <input type="number" v-model="propB"></div>
    <hr>
    <div style="height:10px;"></div>
    <div>val::<input type="number" v-model="val"></div>
    <table>
      <tr><th>add:</th><td>{{ add }}</td></tr>
      <tr><th>sub:</th><td>{{ sub }}</td></tr>
      <tr><th>mult:</th><td>{{ mult }}</td></tr>
      <tr><th>div:</th><td>{{ div }}</td></tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data(){
    return {
      message:'default message',
      input:'name?',
      val: 0,
      add:0,
      sub:0,
      mult:0,
      div:0
    };
  },
  watch:{
    val: function(value){
      console.log('this.value::'+value);
      //this.val = value;
      console.log("this.val::"+ this.val);
      var val = parseInt(value);
      console.log('val::'+val);
      this.add=Math.floor(val+2);
      this.sub=Math.floor(val-2);
      this.mult=Math.floor(val*2);
      this.div=Math.floor(val/2);
    }

  },
  //propsでプロパティを定義、= コンポーネント呼び出し時に属性として使用可能
  props: {
    title: String,
    //num: Number,
    num :{
      //型指定
      type: Number,
      //デフォルト値指定
      default: 100,
      //値の検証を行う関数/ valueが整数かつ0以上100以下かどうかを真偽値で返す
      validator: function(value){
        return value == parseInt(value) && value >= 0 && value <=100;
      },

    },
  },
  methods:{
    doClick(){
      this.message='Hello! '+this.input+'!!';
      this.$emit('input-msg', this.input);
    }

  },
  computed:{
    propA:{
      get: function(){
        return this.val * 2;
      },
      set:function(value){
        this.val = Math.floor(value / 2);

      },
    },
      propB:{
        get: function(){
          return this.val * this.val;
        },
        set: function(value){
          this.val = Math.floor(Math.sqrt(value))
        },
      },
    },
  created: function(){
    this.val = 10;
  },  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
div {
  margin:0px;
  padding: 0px;
  text-align: left;
}

h1 {
  font-size: 72pt;
  font-weight: bold;
  text-align: right;
  letter-spacing: -8px;
  color: #f0f0f0;
  margin: 0px;
}
p {
  margin: 0px;
  color: orange;
  font-size: 16px;
}

</style>
