from sayhello import app
app.secret_key = "1"
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/testdb'


# 设置成 True, SQLALchemy 将会追踪对象的修改并且发送信号
# 这需要额外的内存， 如果不必要的可以禁用他
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 查询时会显示原始的SQL语句， 需要知道
app.config['SQLALCHEMY_ECHO'] = True