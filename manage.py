from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 导入配置文件
from config import Config

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
