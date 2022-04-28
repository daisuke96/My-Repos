import Vue from 'vue'
import VueRouter from 'vue-router'

//あらかじめ必要なコンポーネントをimport

import TodoList from '../components/TodoList.vue'
import MemoList from '../components/MemoList.vue'

//ルーターを使用
Vue.use(VueRouter)


//ルーターの設定
const routes = [{
    path: '/todolist', //URLの末尾
    name: 'Todolist', //名称
    component: TodoList //コンポーネント名
},
{
    path: '/memolist',
    name: 'MemoList',
    component: MemoList
}
]

//historyモードで実行
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

//ルーターの適用
export default router
