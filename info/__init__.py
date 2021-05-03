from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config
from config import config

# 创建数据库对象
db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """通过传入不同的配置名字,初始化其对应配置的应用实例"""

    # 创建app对象
    app = Flask(__name__)

    #  配置
    app.config.from_object(config[config_name])

    # 配置数据库
    db.init_app(app)

    # 配置redis
    global redis_store

    # redis数据交互
    redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

    # 请求提的请求都开启CSRF
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)

    return app
