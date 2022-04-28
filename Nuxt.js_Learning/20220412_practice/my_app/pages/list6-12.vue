<template>
    <section class="container">
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        <table>
            <tbody>
            <tr>
                <th>Email</th>
                <td><input v-model="email"></td>
            </tr>
            <tr>
                <th></th>
                <td><button @click="delData">click</button></td>
            </tr>

            </tbody>
        </table>

        <hr>
        <ul v-for="(data, key) in json_data" :key="data.name" >
            <li><strong>{{key}}</strong><br>{{data}}</li>
        </ul>
        {{json_data}}

    </section>
</template>

<script>
import axios from 'axios';
let url = "https://vue-practice-0411-default-rtdb.firebaseio.com/person";


export default{
    data(){
        return {
            title:'Axios',
            message:'axios sample.',
            json_data: {},
            username: '',
            age: 0,
            tel: '',
            email: '',

        };
    },

    methods:{
        delData(){
            let del_url = url + '/' + this.email + '.json';

            axios.delete(del_url).then((re)=>{
                this.message = this.email + '.json';
                this.email = '';
                this.getData();
            });
        },
        getData(){
            axios.get(url + '.json').then((res)=>{
                this.message = 'get all data';
                this.json_data = res.data;
                console.log('get end')
            }).catch((error)=>{
                this.message = 'ERROR';
                this.json_data = {};
            })
        }
    },
    created:function(){
        this.getData();
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