■仮想環境の作成（任意のディレクトリで下記を実行）
python -m venv venv

■仮想環境の有効化
venv\Scripts\Activate.ps1

■無効化
deactivate

■エンドポイント
flaskのエンドポイントはAPIアクセスのためのURLではなく、URIと紐づいた関数名を指す

■flask shellコマンド
pythonのインタラクティブシェルを使用できるコマンド

■lint機能
コードチェックしてくれる機能
多々設定が可能



■コマンド（--helpをつけてオプション確認が可能）
　　flask run
  　flask routes

■P65　env:FLASK_APP="app.py"
エンドポイントの指定は下記でも可
set FLASK_APP=app.py

■.envファイルでアプリごとに環境変数を設定可能

■ルーティング
@app.route("routename")
def index():
で各ルートを作成することが可能
※キーワード：エンドポイント、methods, rule

■テンプレートエンジン
html（テンプレート）とデータを用いて画面描写させるエンジン
jinja2
→html内にif文等を記述することが可能

■エンドポイントURLの表示
url_for("indexやendpointname")

■CSSの設定
apps\minimalapp\templetes
上記と同じ階層にstaticフォルダを作成し、そこにCSSを格納
html内<header>に下記を記載
   <link rel="stylesheet" href="{{url_for('static', filename='style.css')}}" />
※staticは変更不可

■アプリケーションコンテキスト
【コンテキスト】
もうこれ以上は意味付け出来ない場合や、抽象的な表現が必要な時に使う、
同じ処理が行われる [状態] を表すネーミング
→アプリケーションのデータ状態を確認できるようにするためのもの

【アプリケーションレベルのデータ】
current_app：実行中アプリのインスタンス
g：グローバルテンポラリー領域（一時的なグローバル変数みたいなもの）
リクエストごとにリセット
ctx=app.app_context()
ctx.push()
print(current_app.name)

■テスト用関数
→実際にリクエストせずに動作確認できる関数
test_request_context()
ex.)with app.test_request_context():
       print(url_for("endpointname"))
	   
■リクエストコンテキスト
リクエストの間リクエストレベルのデータを利用できるようにするもの
（パラメータとかの値を調べるときに利用？）
リクエストレベルのデータ2種類：request,session
test_request_contextを用いて使用する
使用例：
with app.test_request_context("/users?updated=ture"):
    #trueが表示
    print(request.args.get("updated"))

※コンテキストのライフサイクル（pushからリクエスト処理終了までの流れ）
はスタック（後入れ先出し=先入れ後出し）方式
push：application_context, request_contextの順
pop：request_context, application_contextの順

■PRGパターン
POST/REDIRECT/GET　パターンの略
例：
1．最初の問い合わせフォーム画面を表示：Get
2．問い合わせ内容（フォームデータ）を送信：Post
3．問い合わせ完了画面へリダイレクトする：Redirect
4．問い合わせ完了画面を表示する：Get

■CSRF対策
Cross-Site Request Forgeriesの略
ウェブアプリの脆弱性の一種で意図しないリクエストを処理しないよう対策する必要がある
from flask_wtf.csrf import CSRFProtect
上記で使用可能にし、htmlファイル上でトークンを生成（{{form.csrf_token}}）することで対策が可能


■HTMLフォームのお作法
1．input項目（テキストボックス等）にはname属性をつける
2．submitはボタンを作成し、押下時にformブロックの内容を送信する。
<input type="submit" name="識別するための名前" value="ボタン名(typeがtext等変数の場合は{{データ名}})" /> 

■ルーティングのメソッドに関して
GET,POSTの判断基準：そのルーターがPOSTを使って表示されるならPOST付与（データを受け取るなら付与）
例：問い合わせフォーム画面自体はPOSTで送るためのデータを保持するが、POSTメソッドは付与しない
　　その代わり、画面遷移後の完了画面（何もデータを保持しない画面）ではデータを受け取るためPOSTメソッドを付与する
  
■Flashメッセージ
flash関数を使って設定、テンプレートでget_flashed_messages関数で取得表示
必要なもの：セッション（コンフィグのSECRET_KEYが必要）
例：app.config["SECRET_KEY"] = "ランダムな文字列"

使用例：
バリデーション（入力チェック）してエラーだった場合のflashメッセージを表示する
flash("メッセージ")で設定
★設定するのは遷移先のエンドポイント関数内、受け取るときは遷移前のテンプレートhtml


■email-validator（メールアドレス入力チェックパッケージ）
from email_validator import EmailNotValidError, validate_email
※pip installでパッケージをインストールすること

■ローカル変数の設定？（テンプレートエンジンjinja2）
{% with hoge=piyo %}{% endwith %}
hogeをwith内でのみ利用可能にする

■ロギング
ロガーを使用してログレベル別にログを出力できる
ログレベルを設定するとそれ以上のレベルが出力
CRITICAL > ERROR > WARNING > INFO > DEBUG

flaskではpython標準のloggingモジュールを使用している
ログレベルの指定：import loggingとapp.logger.setLevel関数を使用

ログ出力(Debugでの例)：app.logger.debug("debug")

■ログツール
flask-debugtoolbarモジュールがある
リダイレクトするとtoolbarでリクエスト値の確認ができなくなる
→リダイレクトを中断する(True)設定になっている
→app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
でリダイレクトを中断しない（リクエスト値が見れる）ようにする
★toolbar利用手順
toolbarをimport > ログレベルの設定 > リダイレクトの継続設定 > DebugToolbarExtensionにアプリケーションをセット


■メール送信機能
flask-mail

■flask-mailの設定
設定：デフォルト：説明
MAIL_SERVER：localhost：メールサーバーホスト名
MAIL_PORT：25：ポート
MAIL_USE_TLS：False：TLSを有効にするか
MAIL_USE_SSL：False：SSLを有効にするか
MAIL_DEBUG：app.debug：デバッグモード
MAIL_USERNAME：None：送信元メールアドレス
MAIL_PASSWORD：None：送信元メールアドレスのパス
MAIL_DEFAULT_SENDER：None：メールの送信者名およびアドレス

■Cookie
ブラウザに保存された情報とその仕組み
cookieから値を取得：requestオブジェクトを使用：request.cookies.get("keyname")
値の設定：
response=make_response(render_template("hoge.html"))
#key,valueを設定
response.set_cookie("keyname","valuename")

値の削除：
response.delete_cookie("keyname")


■セッション
一連の処理を継続する仕組みのこと、Cookieを使ってセッション管理の仕組みを構築できる
コンフィグにSECRET_KEYを設定することで使用可能

値を設定する
★ここから要復習

--------
p184
■ユーザー新規作成
手順
1．新規作成・更新フォームのクラスを作成（forms.py）
2．ユーザー新規作成画面のエンドポイント作成（view.py）
3．新規作成画面のテンプレートを作成（~.html  ：viewでルーティングしたページごとに作成）
4．動確
※前提としてapp.pyに追加設定していることもあり

■ユーザー一覧
1．ユーザー一覧画面のエンドポイント作成
2．テンプレート作成
3．スタイルシート作成
4．動確

■ユーザー編集画面の作成
1．ユーザー編集画面のエンドポイント作成
2．テンプレート作成
3．動確

■ユーザー削除機能の作成
1．削除エンドポイントを作成
2．ユーザー編集画面に削除フォームのテンプレートを追加
3．動確

■formタグ
入力フォーム全体(ブロック)を指し、下記のアクションを実行
actionでフォーム送信先を指定
input type="submit"等でボタン設定

■テンプレートの共通化
重複しているHTMLを記述しなくてよくなる
1．共通テンプレートの作成
→{% block title%}{% endblock %}, {% block content %}{% endblock %}で共通化したいところを表す
2．継承
→{% extends"crud/base.html" %}の書き方で継承宣言、その後上記の間で個別要素を記述


■config
config.pyを作成し、そこにクラスを作成
共通部分は親クラスとし、個別設定を子クラスとして継承させる
最後にconfig辞書にマッピングさせることで他ファイルから呼び出しを可能にする
→app.pyよりapp.config.from_object(config[config_key])でconfigkeyを指定、そのコンフィグを呼び出す

※ほかにもfrom_mapping, from_envvar, from_pyfile, from_fileを使う場合もある


■認証機能の作成
・サインアップ機能、ログイン機能、ログアウト機能
上記三つを作成

1．アプリに認証機能を登録する
app.pyでインポート、blueprintでviews(router)のauthを登録
2．認証機能のエンドポイントを作成
→blueprintでauthを生成、indexのエンドポイントを作成
3．テンプレートを作成
4．認証ページ表示確認画面の作成
5．動確

■サインアップ機能
1．flask-loginと連携
2．サインアップ機能のフォームクラスを作成する
3．Userモデルを更新する
4．サインアップ機能のエンドポイントを作成する
5．テンプレートを作成する
6．crudアプリをログイン必須にする（既存アプリとの連携）
7．動確

■ログイン機能の実装
1．フォームクラスを作成
2．エンドポイントを作成
3．テンプレートを作成
4．動作確認


■ログアウト機能の作成
1．エンドポイント作成
2．ログインステータスの表示








