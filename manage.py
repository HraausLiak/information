from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import db, create_app
from config import config_dict

# 创建app,并传入配置模式:development / production
app = create_app('development')

# 管理app对象及数据库迁移
manager = Manager(app)

# 创建迁移对象
migrate = Migrate(app, db)

# 注册
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return 'Hello World 8888'


if __name__ == '__main__':
    manager.run()
