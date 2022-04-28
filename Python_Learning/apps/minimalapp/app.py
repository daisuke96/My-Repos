# ロギングをimport
import logging
import os
from urllib import response

# flaskクラスをimport
from email_validator import EmailNotValidError, validate_email
from flask import (
    Flask,
    current_app,
    flash,
    g,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

# Flaskクラスをインスタンス化
app = Flask(__name__)
# セッションを使用するための秘密鍵設定
app.config["SECRET_KEY"] = "qwertyuiop"
# ログレベルの設定
app.logger.setLevel(logging.DEBUG)

# リダイレクトを中断しないようにする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# DebugToolbarExtensionにアプリケーションをセットする
toolbar = DebugToolbarExtension(app)

# Mailクラスのコンフィグを設定


app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
print("configs------------")
print(os.environ.get("MAIL_SERVER"))
print(os.environ.get("MAIL_PORT"))
print(os.environ.get("MAIL_USE_TLS"))
print(os.environ.get("MAIL_USERNAME"))
print(os.environ.get("MAIL_PASSWORD"))


# flask-mail拡張を登録する
mail = Mail(app)


# URLと実行する関数をマッピング
@app.route("/", methods=["GET", "POST"])
def index():
    return "hello flask"


@app.route("/hello/<name>", endpoint="hello-endpoint", methods=["GET", "POST"])
def hello(name):
    return f"hello,{name}!"


@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # form属性を使ってフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        descliption = request.form["description"]
        print("username：" + username)
        print("email：" + email)
        print("descliption：" + descliption)

        # 入力チェック
        is_valid = True

        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not descliption:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # メールを送る

        send_mail(
            email,
            "お問い合わせいただきありがとうございました。",
            "contact_mail",
            username=username,
            descliption=descliption,
        )

        # contact_completeエンドポイントへリダイレクトする
        flash("お問い合わせいただき、ありがとうございました")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


def send_mail(to, subject, template, **kwargs):
    # メール送信関数
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    # print("msg::")
    # print(msg)
    mail.send(msg)


# ========================
with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello-endpoint", name="world"))
    print(url_for("show_name", name="ichiro", page="1"))
    print(url_for("static", filename="style.css"))


# アプリケーションコンテキストの確認
# applicationContext=リクエストの間アプリレベルのデータを利用できること
# コンテキストの取得→スタックへpushする（積む）
ctx = app.app_context()
ctx.push()

print(current_app.name)


# グローバルなテンポラリー領域に値を設定する
g.connection = "connection"
print(g.connection)

with app.test_request_context("/users?updated=ture"):
    # trueが表示
    print(request.args.get("updated"))

# ===========================
# cookieから値を取得する, keyを指定する
"""
username = request.cookies.get("username")
print("Cookie" + username)
# Cookieへ値をセットする
response = make_response(render_template("contact.html"))

# key, valueをセットする
response.set_cookie("username", "ichiro")
"""
