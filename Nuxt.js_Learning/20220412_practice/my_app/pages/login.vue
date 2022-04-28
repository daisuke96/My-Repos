<template>
  <div>
    <h5>Email:
    <input type="text" v-model="emailAddress"></h5>
    <h5>Password:
        <input type="text" v-model="password">
    </h5>

    <button @click="SignIn">ログイン</button>
    <hr>
    <button @click="SignOut">ログアウト</button>
        <hr>
    <button @click="check">チェック</button>
    {{ message }}
  </div>



</template>
<script>
import { getAuth, signInWithEmailAndPassword,signOut, createUserWithEmailAndPassword } from 'firebase/auth'
export default {
  data () {
    return {
      emailAddress: '',
      password: '',
      message: '',

    }
  },
  methods: {
    SignIn () {
        console.log("email"+this.emailAddress)
      try {
        //APIkey, authDomain等を取得
        const auth = getAuth();
        console.log('auth: '+JSON.stringify(auth))
        //ログイン処理
        signInWithEmailAndPassword(auth, this.emailAddress, this.password)
          .then((user) => {
            console.log('ログイン成功')
            console.log('user info : '+JSON.stringify(user))
          })
          .catch((error) => {
            console.error(error)
          })
      } catch (e) {
        console.log('error')
        console.error(e)
      }
    },
    SignOut(){
        const auth = getAuth()
        console.log('auth: '+JSON.stringify(auth))
        signOut(auth).then(()=>{
            alert('Sign Out')
            this.emailAddress = '';
            this.password = '';
        }).catch((error)=>{
            console.error(error)
        })
    },
    check(){
      //alert(JSON.stringify(getAuth()))
      //alert(JSON.stringify(getAuth().currentUser))
      const isLogin = getAuth().currentUser 
      if (isLogin != null){
        this.message = 'login'
      }else{
        this.message = 'please login'
      }
    }

  }
}
</script>

<style>
.container{
    padding:5px 10px;
}
h1 {
    font-size: 60pt;
    color: #345980;
}
p {
    padding-top:5px;
    font-size: 20pt;
}
div {
    font-size: 14pt;
}
pre {
    padding: 10px;
    font-size: 18pt;
    background-color: #efefef;
    white-space: pre-wrap;
}
hr { 
    margin: 10px 0px;
}
tr th {
    width: 150px;
    background-color: darkblue;
    color: white;
    font-size: 16pt;
}
tr td {
    padding: 5px 10px;
    background-color: #eef;
    font-size: 14pt;
}

</style>