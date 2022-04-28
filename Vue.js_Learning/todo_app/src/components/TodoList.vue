<template>
    <div>
        <h1>Todo App</h1>
        <h3>{{this.taskName}}</h3><br>
        <!--@keyup.enter＝エンターキーを押下したとき、addTodoListを実行-->
        <input v-model="human.name" placeholder="name"><br>
        {{human.name}}
        <br>
        <input v-model="human.age" placeholder="age"><br>
        {{human.age}}
        <br>
        <button @click="addhuman">追加</button><br>
        {{humans}}
        <br>


        <input v-model="taskName" placeholder="edit me" @keyup.enter="addTodoList">
        <ul style="list-style: none;">
            <li v-for="(todo, index) in todos" :key="todo.index">
              <a>{{todo.ID}}.</a>
              <a v-if="updateId!=todo.ID">{{todo.name}}</a>
              <input v-else v-model="todo.name" @keyup.enter="updateTodo">
              {{todo.date}}
            
              <button @click="deleteTodo(index)">削除</button>
              <button @click="updateId=todo.ID">変更</button>
              


            </li>
            
        </ul>

    </div>
</template>

<script>
import dayjs from 'dayjs';
export default{
    name: 'TodoList',
    data(){
        return{
            //各種変数,リストの初期化
            taskName: '',
            todos: [],
            id: 1,
            updateId: null,
            human: {},
            humans: [],

        }
    },
    methods: {
        addTodoList(){
            //push()=配列追加メソッド
            this.todos.push({
                'ID': this.id++,
                'name': this.taskName,
                'date': dayjs().format('YYYY-MM-DD hh:mm:ss')
            })
            console.log(this.todos)
            //テキストボックス初期化
            this.taskName = null
        },
        deleteTodo(index){
            this.todos.splice(index,1)
        },
        updateTodo(){
            
            this.updateId=null

        },
        addhuman(){
            this.humans.push(this.human)
            this.human={}
        }

    }

}
</script>

