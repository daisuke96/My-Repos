■変数
var：グローバル変数、再宣言可能
let：再代入可、再宣言不可、ローカル変数
const：定数（再代入不可）、再宣言不可、ローカル変数


■関数
・通常の定義
function hoge(){}

・変数として定義
var hoge=function(){}

・アロー関数
hoge((引数)=>{実行する関数本体})
※hogeは引数に関数を持つ関数

■オブジェクト
プロパティを定義可能
let obj={prop1:hoge, prop2:huga}

■コンストラクタ

関数＋オブジェクト
newでオブジェクトを生成（クラスと同様）

function obj(x,y){
this.hoge=x; 
this.fuga=y;
this.func=function(){return this.hoge+this.fuga}
}

function(){コンストラクタ変数定義、メソッド定義※}
※this.method=function(){}で定義

■クラス
newでインスタンス化
class classname{
  constructor(hoge){
    this.prop=hoge;
  }

  method(){
  //メソッドはthisとfunction必要なくなる
  }
  
}

■getter,setter
クラス内でget hoge(){}メソッドとして定義すると
クラス内ではthis.hoge、クラス外（インスタンス化後）ではobj.hogeで変数のように呼び出せる
※let obj=new class名が済んでいること

■モジュールのimport export
export function funcName(){}
(script.jsに記載し別ファイルからimport)
　　↓
import {funcName} from './script.js'

-----
export default function(){}
※関数名は必要なし
　　↓
import 適当な名前 from './script.js'
※任意の名前で呼び出し可能
