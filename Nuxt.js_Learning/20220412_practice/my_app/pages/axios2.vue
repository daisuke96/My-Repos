<template>
    <section class="container">
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        <!--
        <pre>{{ html_data }}</pre>
        -->

        <div>
            <input v-model="find">
            <button @click="getData">click</button>
        </div>
        <hr>
        <ul v-for="(data, key) in json_data" :key="data.name" >
            <li>{{data. name}} ({{data.age}}) [{{key}}]</li>
        </ul>
        {{json_data}}

    </section>
</template>

<script>
import axios from 'axios';
//import { getDatabase, ref, child, get } from "firebase/database";

//staticフォルダ内にあるファイルは直指定が可能
//let url = "http://localhost:3000/README.md";
//test
//let url ="https://jsonplaceholder.typicode.com/posts/";
//検索対象のvalueだけ返すイメージ
//let url = "https://vue-practice-0411-default-rtdb.firebaseio.com/person/";
//検索対象をkey:valueで返すイメージ
let url = "https://vue-practice-0411-default-rtdb.firebaseio.com/person.json?orderBy=%22$key%22&equalTo=%22";


export default{
    data(){
        return {
            title:'Axios',
            message:'axios sample.',
            msg:'',
            json_data: {},
            find: '',
        };
    },
/** 
    async asyncData(){
        console.log('start')
        let result = await axios.get(url);
        //return { html_data: result.data};
        //let id = 1;
        //let result = await axios.get(url + id);
        console.log('end')
        return { json_data: result.data }

    },*/

    methods:{
        getData(){
            //let id_url = url + this.find + '.json';
            let id_url = url + this.find + '%22';
            console.log('id_url:'+id_url)
            axios.get(id_url).then((res)=>{
                this.message = 'get ID='+ this.find;
                this.json_data = res.data;
            }).catch((error)=>{
                this.message = 'ERROR!';
                this.json_data = {};
            });
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