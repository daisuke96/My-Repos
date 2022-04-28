<template>
  <div>
    <h5>Email:
    <input type="text" v-model="emailAddress"></h5>
    {{emailAddress}}
    <h5>Password:
        <input type="text" v-model="password">
    </h5>
    <button @click="SignUp">ユーザー作成</button>

  </div>



</template>
<script>
import { getAuth, signInWithEmailAndPassword,signOut, createUserWithEmailAndPassword } from 'firebase/auth'
export default {
  data () {
    return {
      emailAddress: '',
      password: '',
    }
  },
  methods: {
    SignUp () {
        console.log('create start')
        console.log("email: "+this.emailAddress)
        console.log("pass: "+ this.password)
      const auth = getAuth()
      createUserWithEmailAndPassword(auth, this.emailAddress, this.password)
        .then((userCredential) => {
          console.log('user created')
          console.log('Sign info : '+JSON.stringify(userCredential))
          this.emailAddress = '';
          this.password = '';
        })
        .catch((error) => {
          alert(error.message)
          console.error(error)
        })
    },

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