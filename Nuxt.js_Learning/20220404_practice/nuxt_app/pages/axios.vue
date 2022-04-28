<template>
    <section class="container">
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        <!--
        <pre>{{ html_data }}</pre>
        -->
        <div>
            <input type="text" v-model="msg">
            <button @click="doClick">click</button>
        </div>

        <table>
            <tbody>
            <tr>
                <th>User ID</th>
                <td>{{ json_data.userId }}</td>
            </tr>
            <tr>
                <th>ID</th>
                <td>{{ json_data.id }}</td>
            </tr>
            <tr>
                <th>Title</th>
                <td>{{ json_data.title }}</td>
            </tr>
            <tr>
                <th>Body</th>
                <td>{{ json_data.body }}</td>
            </tr>
            </tbody>
        </table>
        <hr>
        <ul v-for="(data, key) in json_data">
            <li>{{data. name}} ({{data.age}}) [{{key}}]</li>
        </ul>
    </section>
</template>

<script>
import axios from 'axios';

//staticフォルダ内にあるファイルは直指定が可能
//let url = "http://localhost:3000/README.md";
//test
//let url ="https://jsonplaceholder.typicode.com/posts/";
let url = "https://vue-practice-0411-default-rtdb.firebaseio.com/person.json";


export default{
    data(){
        return {
            title:'Axios',
            message:'axios sample.',
            msg:'',
            json_data: {}
        };
    },

    async asyncData(){
        let result = await axios.get(url);
        //return { html_data: result.data};
        //let id = 1;
        //let result = await axios.get(url + id);
        return { json_data: result.data }
    },

    methods:{
        doClick(event){
            axios.get(url+this.msg).then((res)=>{
                this.message = 'get ID' + this.msg;
                this.json_data = res.data;
            }).catch((error) => {
                this.message = 'ERROR!';
                this.json_data = {};
            });

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