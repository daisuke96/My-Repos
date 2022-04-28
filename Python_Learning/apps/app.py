from pathlib import Path

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config


# DB:SQLAlchemyをインスタンス化
db = SQLAlchemy()
csrf = CSRFProtect()

#loginmanagerをインスタンス化する
login_manager = LoginManager()

#login_view属性に未ログイン時にリダイレクトするエンドポイントを指定する
login_manager.login_view = "auth.signup"

#login_message属性にログイン後に表示するメッセージを指定する
#ここではなにも表示しないよう空を設定する
login_manager.login_message = ""


#コンフィグのキーを渡す
def create_app(config_key):
    # Flaskインスタンスの作成
    app = Flask(__name__)

    # アプリのコンフィグ設定をする
    app.config.from_object(config[config_key])
    
    """
    下記べた書き
    app.config.from_mapping(
        SECRET_KEY="qwertyuiop",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # SQLをコンソールログに出力する設定
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SELECT_KEY="qwertyuiop",
    )
    """
    csrf.init_app(app)

    # SQLAlchemyとアプリを連携する
    db.init_app(app)

    # Migrateとアプリを連携する
    Migrate(app, db)

    login_manager.init_app(app)

    # crudパッケージからviewsをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    #これから作成するauthパッケージからviewsをimportする

    from apps.auth import views as auth_views

    #register_blueprintを使い、viewsのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    #login_managerをアプリケーションと連携する
    







    return app
