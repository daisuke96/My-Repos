from pathlib import Path

basedir = Path(__file__).parent.parent

#Baseconfigクラスを作成する
class BaseConfig:
    SECRET_KEY = "QWERTYUIOP"
    WTF_CSRF_SECRET_KEY = "qwertyuiop"

#Baseconfigクラスを継承してlacalconfigクラスを作成する
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    

#Baseconfigクラスを継承してTestConfigクラスを作成する
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

#Config辞書にマッピングする
config = {
    "testing" : TestingConfig,
    "local" : LocalConfig
}
