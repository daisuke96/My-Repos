■ダイアログ（見た目）の切り替え
→V-ifで真偽チェックで切り替え可能

■日付等初期表示させたいもの
data()内の定義で初期値を設定してしまう。

■配列にオブジェクト（リスト）を追加
【配列】.push(【オブジェクトの変数】)

オブジェクトはkey:valueを持てる{}でdata内に定義(初期化)しておき、（task:{}等）
templateでv-model=task.nameとすることでname keyを追加&入力すればvalueも入る
※push後はオブジェクトを初期化することを忘れずに
→そのままmodelに入力すると配列内のオブジェクトも変わってしまう


■V-modelの使い方
★タグを変数化できる（テキストボックスやボタン、フォームなど）
★imputタグやformタグ、textarea, selectbox等様々な入力項目に対してvue.jsのdataと紐づけることが可能
dataで初期設定しているならそれを{{【v-modelの名前】}}で呼び出せるし（template側）
逆に下記のようにdataを操作することも可能
task.taskIdとすることでtask{}にtaskIdという要素を持たせている
task辞書にkeyとvalueを同時に格納しているイメージ

<div class="col-6 pb-3">
  <label>作業内容</label>
  <select-box v-model="task.taskId" :options="optionsTaskName" emptyword="--" />
</div>
~~~~~~~~~~
data(){
    task: {}
}

■v-for :keyに関して
v-bind:key(:key)がないとテーブルなどの要素すべてを上書きしてしまう
inputタグがv-for内で使われていたりすると、input部分だけ変わらなくなってしまう（削除とかされない）
また、keyの指定はindexではなく、idなど要素を特定できるものを指定したほうが良い
→indexだとkeyなしと同じになってしまう。
（indexは要素を特定するものではないという点が注意）
indexにするとオブジェクトが変わった際に何が変わったのかわからない
→indexではなく、オブジェクトのidとかにしてあげる必要がある★

■findメソッド
リストに対して実行し、条件に一致する要素を返却する
taskName(id){
    return this.taskList.find(function(v){return v.id == id}).name
}
※もしくは
taskName(id){
    return this.tasklist.find(v => v.id == id).name
}


■アロー関数
※要確認

■$emit, props
$emit
子から親へ値を渡すときに使用（記載は子コンポ）
※子から受け取った値は$eventまたは任意の関数で受け取り可能


props
親から子へ値を渡すときに使用（記載は子コンポ）

【props例】
・親コンポ
<【子で定義しているexport default名】 :【子コンポで使う変数名】="親コンポから渡す変数"/>
※「:hoge="hoge"」のようにデータ授受に「:」「""」は必須

・子コンポ
export default{
    props:{
	    hoge（受け取った変数名）:{
		    type（バリデーションチェック）:Object
		}
    }
}
※参照する際は{{hoge}}でおｋ


■リアクティブ
その値が監視され、変更が検知される状態のこと


■computed
算出プロパティ：メソッドのように定義することが可能
リアクティブでキャッシュされる
→一度計算してしまえば２回目以降は即時応答

■CSS(bootstrap)
row:行
col:列

■mounted()
DOM作成後に呼び出し？

■インポート
import {exportで公開したデータ} from 'path' 
exportdefaultで公開したものはどんな名前でimportしてもよい

----------------------------------
★超入門　開始
■ビルド
npm run build
公開するファイルを作成する→サーバにこれだけあげればよい
distフォルダ内に作成される

■V-Node
render:(element)=>{}で作成されるオブジェクト

■render更新タイミング
{{}}が更新されないと画面更新がされない？

■map
配列からV-Node配列を作成することができる、簡単にリストを作成できる。
配列.map(引数 => 新たな値)
ex.
items: ["hoge",""fuga]
var li = data.items.map(item => element("li",item));
※dataオブジェクトにitemsがあるとする
※itemに配列の要素を代入し、VNODEを作成

■element()
render:(element)=>{
  elemnt("タグ名",属性情報,表示内容)
}
※上記は入れ子にすることができる
※elementはhで置き換えられる
render:(h)=>{
  return h(tag,h(tag2,zokusei,hyouji))
  
}

■v-html
<div>
<ol v-html="messages"></ol>
</div>

<script>
    var data = {
        messages:'<li style="color:red;">vue.js sample message.</li>'
    };

→dataのmessagesで設定した値が格納される


■v-bind
属性に値を付与できる
ex)v-bind:style="hoge"
→省略ver）:style="hoge"

■オブジェクト構文
classなどをv-bindする際に使用
　↓
:class="{classname : 変数, classname2 : 変数2...}"
★変数には真偽値をいれる
→変数が真の時、対象クラスが活性化

★真偽の反転は【!】を用いるとよい

★条件が多くなる場合はclass="任意オブジェクト変数名(dataのプロパティであること)"
で別途任意オブジェクトを作成し、プロパティにクラス名を定義する
各プロパティの真偽値がtrueの場合、そのプロパティ(class)が実行
→オブジェクトプロパティがfalseだと実行されない？？
→v-ifと同じような使い方（疑似v-if）ができる？？
★下記はもともと
→:class="{classname : 変数, classname2 : 変数2...}"
のように真偽値でクラスが適用される、それを下記のようにわけただけ

<p :class="classes">
~~~~~~~~~~~~~~~~~~~~~~
    var classObj = {
        red: true, //styleで定義したクラス名であること！
        blue: false,
    };
    var data = {
        message: 'Hello Vue!',
        classes: classObj,
    };

■style属性のオブジェクト構文
<!--属性のプロパティでハイフンがついているものは削除し、後ろの文字を大文字にする  例：fontSize-->
<p :style="{fontSize:'20pt', color:'orange', border:'2px solid cyan'}">
※オブジェクトを指定することも可能
　↓
<p :style="styles">
~~~~~~~~~~
    var stylelist = {
        fontSize: '20pt',
        color: 'orange',
        border: '2px solid',
    };

    var data = {
        message: 'hello vue',
        styles: stylelist,
    };
	
■v-if
上記クラスのオブジェクト構文はv-ifをつかってもできる
違いは上記：クラスの適用（タグは残る）、今回：タグごと消える
liタグとかはすべてにifを適用させないといけないがそれは不可
→<template>ならそれが可能
        <template v-if="flag">
            <p>データをテーブル表示</p>
            <table>
                <tr><th>Name</th><th>mail</th></tr>
                <tr><td>Taro</td><td>taro@yamada</td></tr>
                <tr><td>hanako</td><td>hanako@sato</td></tr>
            </table>
        </template>
		
■v-for
タグを繰り返し生成する,
例：
<li v-for="hoge in 配列">
    {{hoge.prop}}

★下記のようにインデックスを持ってくることも可能
<li v-for=(hoge, index) in 配列>

■オブジェクトのv-for
v-for="(value, key) in object"
※keyはオブジェクトのプロパティ
※key,valueではなく、value,keyな点に注意

■オブジェクトとプロパティ
オブジェクトのプロパティはユニークであり、順番はない

■v-ifとv-forの順序
2系ではv-forが優先


■コンポーネント
vueオブジェクトを再利用するための仕組み

・定義
Vue.component(名前 , {設定情報});
例：
    Vue.component('hello',
    {
        template: '<p class="hello">Hello!</p>'
    })

・呼び出し
<コンポーネント名 />
例：<hello />

■変数をコンポーネントに渡す
data: function(){ return {変数の情報}; }

    Vue.component('hello',
    {
        data:function(){
            return {
                message: 'This is new message'
            };

        },
        template: '<p class="hello">Hello! {{message}}</p>'
    });


■同一コンポーネントの複数表示
list3-3：23,25行目<div></div>にしないと動かないのはなぜ？


■属性およびタイプの指定
HTML内で属性を使用し、template（コンポ内）で呼び出したい場合に使用（nameだったら{{name}}で呼び出し可）

【属性指定】
template:と同じ並びでprops:['属性名',...]の配列で可能

    Vue.component('hello',
    {
        template: '<p class="hello">Hello! {{name}}</p>',
        props: [
            'name',
        ],
    })

→呼び出しはhtml部で<hello name="hoge"/>で可能

★コンポーネント呼び出しのnameは、{{name}}とprops内のnameいずれにも保持されている

【タイプ（型）指定】
props:[]ではなく、props:{name:type, ...}のオブジェクトで表記

※typeは「String, Number, Boolean, Array, Object」等が用意

■v-bind（再掲）
属性に値を付与する→コンポーネントタグでも使用可能
★Vueオブジェクト作成時（コンポじゃない）のプロパティ値を付与できる
例：name属性にdataプロパティのhogeを付与
<component_name :name="hoge"/>
※コンポーネントのpropsでprops:['name'] （or props:{name:String}）、
Vueオブジェクトのdataでdata: {hoge:default_value}を定義していることが前提

■v-model
inputで入力された値をVueオブジェクトのdataプロパティにバインドする
<input v-model="hoge">
data:{hoge:default_value}が前提


■v-on
v-on:hoge="式"
※@hoge="式"でも可能
hoge=click等
clickならクリックしたときにjs処理が可能
イベントハンドラ：v-onしたときに何か他の動作をさせたい場合

■methods
v-on:click等で発火させる、定義は下記の通り
methods:{
    functionName: function(){
	    return hoge
	}
}

■computed
//methodsを使う場合はボックスのフォーカスアウトでイベントを発火していたが、
//computedにすることでプロパティとして{{computed_name}}で呼び出せる
//※タイミングは「関数内で使われている値が変化したときのみ」になる点に注意
computed:{
    func_name:function(){
	    return hoge
	}
}

■グローバルコンポーネントとローカルコンポーネント
【グローバルコンポーネント】
Vue.component('comp_name',{template:'',data:function(){return{}},props:[],methods:{}...})
※script内ならどこでも可

【ローカルコンポーネント】
vueインスタンス作成内に定義
components:{
    comp_name:{
	    template:'',
	},
	comp_name2:{
	    xxxx
	}
}
■プロジェクト
VueCLI等プロジェクトを作ると、プロジェクト自体がwebサーバとして動く
一般的なWebサーバで公開するときはビルドが必要


■export default
importで呼び出したときにデフォルトで用意してくれるもの

■index.html
実際の画面表示を行っている
→なぜJSとかの記載がないのに動くのか
→プロジェクトがwebサーバだから
→indexの中にwebサーバ内でapp.vueとつなげるscriptがある？

■props（再掲？）
プロパティを定義
★コンポーネント呼び出し時に属性として使用可能
ex))props:{prop_name: String}※子コンポーネント内
<comp_name prop_name="hoge"></comp_name>※親コンポーネント

★子コンポーネント内でthis.prop_nameとかはダメ（thisはdataしか無理）
→あくまでコンポーネントタグで属性として使えるようにするだけ

★--まとめ--★
・v-bind：親が親のdataから子のpropsに値を渡したいときに使う！！
:name="hoge"※親で記述
　↓
親が子のname propsにhoge（親data）をバインド

・props：他のコンポーネント（親）からpropsのコンポ（子）を呼び出す際に文字列等を渡せるようにする
※親のdataを渡すときはv-bind:data_valueとすること


・v-model：inputやフォームなどに、そのコンポのdata内変数を結び付けられる（変数にできる）
※data()内で定義してあることが前提

・v-on：eventハンドラ、タグとかinput, button等に付与できる
v-on:hoge（hoge=JSのonclickとかonhoge関連）
@hogeで省略可能
★----------★

■子コンポーネントから親コンポーネントへの値受け渡し
v:bindの逆
1．子コンポーネントに下記を記述
this.$emit('event_name', arg)
arg：引数(子コンポdata)

2．親コンポ側で下記を記述
<component_name v-on:event_name="method_name" ></component_name>
<component_name @event_name="method_name" ></component_name>でも可
★メソッド名は()つけない！
"method_name();"　→　X
"method_name"　　 →　〇

3．親コンポ内でmethod_nameをmethodsに記載
method_name(arg){}
argは特に宣言する必要なし

■trim()
前後の空白を削除するメソッド

■create, mount
vueインスタンスの初期化時に実行される
createの方がmountより先、他の処理に関してはライフサイクルを参照
create：DOMが作られる前※vueインスタンスは作成されている→data内のプロパティを更新することが可能
→DOMに対する各要素の操作不可
mount：DOMが作られた後
→DOMに対する各要素の操作可能

■computed
常にDOMを監視しておきたいときに使用
例：テーブルの変更があったら更新する
<table v-html="computed_func_name">

■unshift()
配列の最初に要素を追加、返すのは要素数

■props（プロパティ）の詳細設定
props_name: {}のオブジェクト形式で設定可能
例) num: {type:String, default:XXXX, ...}

type:
→型を指定

default:
タグに記載がない（設定されていない）ときのデフォルト値

validator: function(arg){return hogehoge}
詳細チェック用関数→hogehogeに条件式を記載、戻り値は真偽値
arg=設定された値
ex)
validator: function(value){
return value == parseInt(value) && value >= 0 && value <=100;
}

■Getter, Setter
v-modelでprops_nameを監視
v-modelは本来変数化するだけだが、computedのプロパティ（getter,setter）を指定すると、
変数が関数のようなふるまいをする


computed:{
    props_name: {
	    get: function(){xxx},
		set: function(){xxx}
	},
	}
	
	
	
■監視プロパティwatch:
いくつもの値を監視し、まとめて複雑な処理させたいときに使用

watch:{
    data_name : function(value){xxxxx},
	...
}
data_name＝特定のデータが変更されたときにfunction内の処理を実行
valueはその時の特定のデータそのものが入ってくる

■イベントの伝達
下記の場合、C>B>A（上中下）となり、Cのイベントが発火した場合はB、Aも発火する
（BだとB,A,　AだとAのみ）
<div>a
  <div>b
    <div>c</div>
  </div>
</div>

■イベント修飾子
stop：伝達をストップ
@click.stop="hoge_func"
→下のタグに伝達されなくなる

self：自身で発火したときのみ実施する
→下にタグがあれば自分をスキップし下は実行する

■キーイベント修飾子
enter
tab
delete
esc
space
up,down,left,right
例）
@keydown.hoge
※hoge=上記修飾子

■キーイベント種類
keypress：機能キーshiftなどは検知されない
keydown：機能キーも検知される
keyup等

■マウスイベント
right, middle, left

■その他
prevent：イベント消費修飾子
@click.right.prevent="hoge"
→その後の右クリック処理が行われない
→イベント消費


■スロット
子コンポーネントから親コンポーネント要素（呼び出しタグ内にあるもの限定）を表示させたい場合
・親コンポ
<child_comp>hogehoge</child_comp>
→hogehogeは消えてしまう

・子コンポ
<slot />
→親のhogehogeをタグ位置に表示


==
・asyncData
サーバサイドレンダリング用メソッド
mountedはブラウザ側（クライアント側）の処理なので、dataに値を設定できない？
→解消用のメソッド、画面表示前にデータセットが可能


