from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    """项目配置信息"""
    DEBUG = True

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information18"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis项目配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session配置信息
    SECRET_KEY = "AJDICE2CHDJ3UjfcGhd"
    # 指定session保存到redis中
    SESSION_TPYE = 'redis'
    # 让cookie中的session_id 被加密签名处理
    SESSION_USE_SIGNER = True
    # 使用redis实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_HOST)
    # session的有效期,单位是秒
    PERMANENT_SESSION_LIFETIME = 86400


# 创建app对象
app = Flask(__name__)
app.config.from_object(Config)

# 创建数据库对象
db = SQLAlchemy(app)

# redis数据交互
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 请求提的请求都开启CSRF
CSRFProtect(app)
Session(app)

# 管理app对象及数据库迁移
manager = Manager(app)

# 创建迁移对象
migrate = Migrate(app, db)

# 注册
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    manager.run()
