from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sayhello import db
from sayhello import app

manager = Manager(app)

Migrate(app, db)

# manager是Flask-Script的实例
# 这条语句在flask-Script中添加一个db命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()