<template>
    <div class="board" v-if="userInfo.uid">
        <h1>Message Board</h1>
        <div class="login-out"><button @click="signOut">Logout</button>
        <br>Login User：{{ username }}
        </div>
        <div class="input-box">
            <label for="input-box">New Message：</label>
            <input type="text" v-model="msg">
            <button @click="add">send</button>
        </div>
        
        <div class="board-title">
            <strong>Message</strong>
        </div>
        <div class="board-view">    
        <ul v-for="data in datas" :key="data.id">
          <li><div class="msg">{{ data.message }}</div>
              <div class="user">{{ data.username }} ({{ data.date }})</div>
          </li>
          <hr>
        </ul>
        </div>

    </div>
    <div v-else-if="isSignup">
        <div class="login">
          <div class="form-input">
            <h1>Please Login</h1>
            <label for="email">Email</label>
            <input type="text" v-model="email">
          </div>
          <div class="form-input">
            <label for="password">password</label>
            <input type="password" v-model="password">
          </div>
          <div class="form-button">
            <button @click="login">Login</button>
          </div>
          <div class="form-button">
              <button @click="goSignup">create user?</button>
          </div>
        </div>
    </div>
    <div v-else>
        <div class="login">
          <div class="form-input">
            <h1>Create New User</h1>
          </div>
          <div class="form-input">
            <label for="email">Email</label>
            <input type="text" v-model="email">
          </div>
          <div class="form-input">
            <label for="User Name">User Name</label>
            <input type="text" v-model="username">
          </div>
          <div class="form-input">
            <label for="password">password</label>
            <input type="password" v-model="password">
          </div>
          <div class="form-button">
              <button @click="signUp">create</button>
          </div>
        </div>
    </div>
</template>

<script>
import {getAuth, signInWithEmailAndPassword, signOut, onAuthStateChanged, createUserWithEmailAndPassword} from 'firebase/auth'
import axios from 'axios';
//let url = "https://vue-practice-0411-default-rtdb.firebaseio.com/person";
import { getDatabase, ref, onValue, child, get, set, equalTo, query, orderByChild, limitToLast, orderByKey, push} from "firebase/database";


export default{
    data(){
        return{
            isSignup: true,
            email: '',
            password: '',
            username: '',
            users: [],
            msg: '',
            id: '',
            datas: {},
            userInfo: {},
            date:'',
        }
    },
    mounted(){
        console.log('mount start')
        //ログインチェック
        const auth = getAuth();
        onAuthStateChanged(auth, (user)=>{
            if (user) {
                this.userInfo = user;
                this.email = user.email
                this.getUserData();
            }else{
                this.userInfo = {};
            }
            console.log(this.userInfo)

            //DB接続&伝言データ取得
            const dbRef = query(ref(getDatabase(),'board'),limitToLast(10),orderByKey());
            onValue(dbRef, (snapshot) => {
                this.datas = snapshot.val();
                //idをプロパティに追加
                for(let data in this.datas){
                    this.datas[data].id = data;
                }
                var sorts = Object.entries(this.datas);
                sorts.reverse(function(p1,p2){
                    var p1key = p1[0], p2key = p2[0];
                    if(p1key < p2key){ return 1; }
                    if(p1key > p1key){ return -1; }
                    return 0;
                })
                //console.log(sorts)
                this.datas = Object.fromEntries(sorts);
                //console.log('datas'+JSON.stringify(this.datas))
            })
        })

    },
    methods:{
        login(){
            try{
                const auth = getAuth();
                signInWithEmailAndPassword(auth, this.email, this.password)
                .then((users)=>{
                    console.log('uuuu'+JSON.stringify(users))
                    //ユーザーメール等　情報多
                    //this.username = userCredential.user;
                    //alert(JSON.stringify(this.username));
                    //this.user = auth.currentUser;
                    //alert(JSON.stringify(this.user))
                    //ログインユーザー情報をDBから取得
                    //伝言一覧を取

                }).catch((error)=>{
                    alert(error);
                })
            }catch(e){
                console.error(e)
            }

        },
        signOut(){
            const auth = getAuth();
            signOut(auth).then(()=>{
                alert('Logout user : ' + this.username)                
            }).catch((error)=>{
                console.error(error);
            })

        },
        goSignup(){
            this.isSignup=false
        },
        signUp(){
            const auth = getAuth();
            createUserWithEmailAndPassword(auth, this.email, this.password)
            .then((userCredential) => {
                //this.userInfo = userCredential.user;
                //console.log('info::'+ this.userInfo)
                const db = getDatabase();
                const listRef = ref(db, 'member');
                const newMember = push(listRef);
                set(newMember,{
                    email: this.email,
                    name: this.username,
                })
                alert('create user!');
                this.isSignup=true;
            }).catch((error) =>{
                console.error(error);
            })


        },
        getUserData(){
            console.log('getData start');   
            const dbRef = ref(getDatabase());
            get(child(dbRef, `member`)).then((snapshot)=>{
                if(snapshot.exists()){
                    var data = snapshot.val()
                    //item = 1,2,...  data[item]=数字をキーにオブジェクトを取得
                    //[{name:hoge,email:hoge},{...}]の形でリストを作成
                    for (let item in data){
                        this.users.push(data[item])
                    }

                    //console.log(snapshot.val());
                    console.log(this.users)
                    //リスト内からemailが一致した場合usernameを割り当て
                    for (let item in this.users){
                        console.log('users[item]'+ JSON.stringify(this.users[item]))
                        if(this.users[item].email==this.email){
                            console.log('equal')
                            this.username = this.users[item].name
                            console.log('username  '+this.username)
                            this.users=[]
                            return
                        }
                    }
                    
                }else{
                    console.log('no data')
                }
            }).catch((error)=>{
                console.error('getdata'+error);
            }); 
        },

        add(){
            //id付与（DBkey）
            this.id=Date.now();
            //ユーザー名は下記利用
            this.username
            //messageは下記利用
            this.msg
            //時刻フォーマット
            let day = new Date();
            let year = day.getFullYear();
            let mon = ('0' + (day.getMonth() + 1)).slice(-2);
            let d = ('0' + day.getDate()).slice(-2);
            let h = ('0' + day.getHours()).slice(-2);
            let m = ('0' + day.getMinutes()).slice(-2);
            this.date = year + '/' + mon + '/' + d
            + '-' + h + ':' + m;

            const db = getDatabase();
            set(ref(db, 'board'+'/'+this.id), {
                date: this.date,
                message: this.msg,
                username: this.username,
            }).then(() => {
                alert('Message send!!')
                this.msg = '';
            }).catch((error) => {
                console.error(error)
            })
        },

    },

}
</script>

<style>
.container{
    padding:5px 10px;
}
h1 {
    font-size: 30pt;
    color: #345980;
}
p {
    padding:5px 10px;
    font-size: 10pt;
    text-align: right;
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
.form-input {
  margin: 0 auto;
  text-align: center;
  padding: 5px;
  width:400px;
}
.login .form-button {
  margin:auto;
  text-align: center;
  padding: 2px;
  width:200px;
}
.input-box{
    text-align: right;
    padding: 10px 200px;
    margin: auto;
}
.input-box input{
    padding: 2px;
    text-align: left;
    width:400px;
}
.board{
    text-align: center;
}
.login-out{
    padding:10px 200px;
    text-align: right;
}
.board button{
    text-align: center;
}
.board-view{
    padding: 2px 200px;
}

.board-title{
    line-height: 100px;
    color: orange;
    font-size: 20pt;
}
.msg{
    text-align: left;
    font-size: 14pt;

}
.user{
    text-align: right;
    font-size: 10pt;
}
li {
    padding: 2px 10px;
}
</style>