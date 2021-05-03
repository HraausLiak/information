from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db


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
