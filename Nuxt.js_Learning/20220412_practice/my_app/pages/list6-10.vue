<template>
    <section class="container">
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        <div>
            <input v-model="find">
            <button @click="getData">click</button>
        </div>
        <hr>
        <ul v-for="(data, key) in json_data" :key="data.name" >
            <li><strong>{{key}}</strong><br>{{data}}</li>
        </ul>
        {{json_data}}

    </section>
</template>

<script>
import axios from 'axios';
let url = "https://vue-practice-0411-default-rtdb.firebaseio.com/person.json?orderBy=%22age%22";


export default{
    data(){
        return {
            title:'Axios',
            message:'axios sample.',
            json_data: {},
            find: '',
        };
    },

    methods:{
        getData(){
            let range = this.find.split(',');
            let age_url = url + '&startAt='+range[0] + '&endAt=' + range[1];
            console.log('age_url:'+age_url)
            axios.get(age_url).then((res)=>{
                this.message = 'get='+ range[0] + '< age <'+range[1]
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