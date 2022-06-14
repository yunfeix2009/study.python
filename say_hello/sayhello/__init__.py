from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')

# 环境变量， 意思是去掉模板语言中占据的空行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
# Flask扩展一般都在创建实例时初始化， 这行代码是Flask-Bootstrap的初始化方法
bootstrap = Bootstrap(app)
# 这行代码是Flask-Bootstrap的初始化方法
moment = Moment(app)

# 蓝图
# from sayhello.views import sayhello
# app.register_blueprint(sayhello, url_prefix='/app1')