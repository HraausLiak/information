from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config

# 创建app对象
app = Flask(__name__)

#  配置
app.config.from_object(Config)

# 创建数据库对象
db = SQLAlchemy(app)

# redis数据交互
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 请求提的请求都开启CSRF
CSRFProtect(app)
# 设置session保存位置
Session(app)