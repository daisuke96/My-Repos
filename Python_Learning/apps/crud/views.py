from apps.app import db
from apps.crud.forms import UserForm
from apps.crud.models import User
from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required

# brueprintでcrudアプリを生成する
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# indexエンドポイントを作成し、index.htmlを返す
@crud.route("/")
#デコレーターの追加
@login_required
def index():
    return render_template("crud/index.html")


@crud.route("/sql")
@login_required
def sql():
    db.session.query(User).all()
    return "コンソールログを確認してください。"


@crud.route("/users/new", methods=["GET", "POST"])
@login_required
def create_user():
    # UserFormをインスタンス化
    form = UserForm()

    # フォームの値をバリデート
    if form.validate_on_submit():
        # ユーザーを作成する
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        # ユーザーを追加してコミットする
        db.session.add(user)
        db.session.commit()

        # ユーザーの一覧画面へリダイレクト
        return redirect(url_for("crud.users"))

    return render_template("crud/create.html", form=form)


@crud.route("/users")
@login_required
def users():
    # ユーザー一覧の取得
    users = User.query.all()

    return render_template("crud/index.html", users=users)


@crud.route("users/<user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    form = UserForm()

    # Userモデルを利用してユーザーを取得する
    user = User.query.filter_by(id=user_id).first()
    print("if前")

    # formからsubmitされた場合はユーザーを更新し、ユーザーの一覧画面へリダイレクト
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        print("リダイレクト前")
        return redirect(url_for("crud.users"))
    # getの場合はHTMLを返す
    return render_template("crud/edit.html", user=user, form=form)


@crud.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    print("■削除対象者■")
    print(user)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("crud.users"))
