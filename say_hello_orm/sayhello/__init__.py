from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
# settings中的配置参数都会给app的属性
app.config.from_pyfile('settings.py')

# 环境变量，意思是去掉模板语言中占据的空行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

moment = Moment(app)
bootstrap = Bootstrap(app)

from sayhello.views import sayhello

# app.register_blueprint(sayhello, url_prefix='/app1')
app.register_blueprint(sayhello, url_prefix='/app1')


#
# 1. python 基础语法，包括：六大数据类型，int,str,tuple,list,dict,set
# 2. 基本讲法的复习，主要讲的，排序，
# 3. 函数，面向对象
# 4. 正则，装饰器，飞机大战，百度翻译，元类等
# 5. flask的web开发