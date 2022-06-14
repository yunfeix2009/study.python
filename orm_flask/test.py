from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/test1'

db = SQLAlchemy(app)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    #     定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    us = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s' % self.name


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    ro1 = Role(name='admin')
    ro2 = Role(name='user1')
    ro3 = Role(name='user2')
    ro4 = Role(name='user3')
    ro5 = Role(name='user4')
    ro6 = Role(name='user5')
    ro7 = Role(name='user6')
    db.session.add_all([ro1, ro2, ro3, ro4, ro5, ro6, ro7])
    db.session.commit()
    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='li', email='li@189.com', pswd='asdfjkl;', role_id=ro3.id)
    us4 = User(name='zhu', email='zhuzhu@163.com', pswd=';lkjfdsa', role_id=ro4.id)
    us5 = User(name='xia', email='x@189.com', pswd='fjdksla;', role_id=ro5.id)
    us6 = User(name='yao', email='yaaaaao@189.com', pswd=';alskdjf', role_id=ro6.id)
    us7 = User(name='liang', email='lg@189.com', pswd='zzm', role_id=ro7.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7])
    db.session.commit()
    db.session.query_property()
    #
    # pr_all = User.query.filter_by().all()
    # pr_count = User.query.filter().count()
    # for i in range(pr_count):
    #     print('all:' + '\n' +
    #           'id:' + str(pr_all[i].id) +
    #           '    name:' + pr_all[i].name +
    #           '    email:' + pr_all[i].email +
    #           '    password:' + pr_all[i].pswd + '\n')
    #
    # pr_first = User.query.filter_by(name='zhang').first()
    # print('first:' + '\n' +
    #       'id:' + str(pr_first.id) +
    #       '    name:' + pr_first.name +
    #       '    email:' + pr_first.email +
    #       '    password:' + pr_first.pswd + '\n')
    #
    # pr_first_or_404 = User.query.filter_by(name='li').first_or_404()
    # print('first_or_404:' + '\n' +
    #       'id:' + str(pr_first_or_404.id) +
    #       '    name:' + pr_first_or_404.name +
    #       '    email:' + pr_first_or_404.email +
    #       '    password:' + pr_first_or_404.pswd + '\n')
    #
    # pr_get = User.query.get(6)
    # print('get:' + '\n' +
    #       'id:' + str(pr_get.id) +
    #       '    name:' + pr_get.name +
    #       '    email:' + pr_get.email +
    #       '    password:' + pr_get.pswd + '\n')
    #
    # pr_get_or_404 = User.query.get_or_404(4)
    # print('get_or_404:' + '\n' +
    #       'id:' + str(pr_get_or_404.id) +
    #       '    name:' + pr_get_or_404.name +
    #       '    email:' + pr_get_or_404.email +
    #       '    password:' + pr_get_or_404.pswd + '\n')
    #
    # pr_first = User.query.filter().all()
    # pr_count = User.query.filter_by(name='wang', id=0).count()
    # print('pr_first:', pr_first)
    # id_list = []
    # for i in pr_first:
    #     id_list.append(i.id)
    # print(id_list)
    # pr_count = User.query.filter(id > 3).count()
    # # print("count_id"+str(pr_first.id))
    # print('count:' + '\n' + str(pr_count))
    #
    # pr_paginate = User.query.filter().paginate(page=1, per_page=3)
    #
    # # pr_all = User.query.filter().all()
    # # pr_count = User.query.filter().count()
    # # for i in range(pr_count):
    # #     print('all:' + '\n' +
    # #           'id:' + str(pr_all[i].id) +
    # #           '    name:' + pr_all[i].name +
    # #           '    email:' + pr_all[i].email +
    # #           '    password:' + pr_all[i].pswd + '\n')
    # # # 把过滤器添加到原查询上，返回一个新查询
    # #
    # # pr_all = User.query.filter_by(name='wang').all()
    # # pr_count = User.query.filter().count()
    # # for i in range(pr_count):
    # #     print('all:' + '\n' +
    # #           'id:' + str(pr_all[i].id) +
    # #           '    name:' + pr_all[i].name +
    # #           '    email:' + pr_all[i].email +
    # #           '    password:' + pr_all[i].pswd + '\n')
    # # # 把等值过滤器添加到原查询上，返回一个新查询
    # #
    # # pr_all = User.query.limit
    # # pr_count = User.query.filter().count()
    # # for i in range(pr_count):
    # #     print('all:' + '\n' +
    # #           'id:' + str(pr_all[i].id) +
    # #           '    name:' + pr_all[i].name +
    # #           '    email:' + pr_all[i].email +
    # #           '    password:' + pr_all[i].pswd + '\n')
    # # # 使用指定的值限定原查询返回的结果
    # #
    # # pr_all = User.query.offset().first()
    # # pr_count = User.query.filter().count()
    # # for i in range(pr_count):
    # #     print('all:' + '\n' +
    # #           'id:' + str(pr_all[i].id) +
    # #           '    name:' + pr_all[i].name +
    # #           '    email:' + pr_all[i].email +
    # #           '    password:' + pr_all[i].pswd + '\n')
    # # # 偏移原查询返回的结果，返回一个新查询
    # #
    # # pr_all = User.query.order_by().all()
    # # pr_count = User.query.filter().count()
    # # for i in range(pr_count):
    # #     print('all:' + '\n' +
    # #           'id:' + str(pr_all[i].id) +
    # #           '    name:' + pr_all[i].name +
    # #           '    email:' + pr_all[i].email +
    # #           '    password:' + pr_all[i].pswd + '\n')
    # # # 根据指定条件对原查询结果进行排序，返回一个新查询
    # #
    # pr_all = User.query.group_by().all()
    # pr_count = User.query.filter().count()
    # for i in range(pr_count):
    #     print('all:' + '\n' +
    #           'id:' + str(pr_all[i].id) +
    #           '    name:' + pr_all[i].name +
    #           '    email:' + pr_all[i].email +
    #           '    password:' + pr_all[i].pswd + '\n')
    # # # 根据指定条件对原查询结果进行分组，返回一个新查询

    pr_pages = User.query.filter(User.name='wang' and id>5)all()
    pr_page = User.query.filter().paginate.page(page=1, per_page=3)
    pr_has_next = User.query.filter().paginate.has_next(page=1, per_page=3)
    pr_has_prev = User.query.filter().paginate.has_prev(page=1, per_page=3)
    pr_next_num = User.query.filter().paginate.next_num(page=1, per_page=3)
    pr_prev_num = User.query.filter().paginate.prev_num(page=1, per_page=3)
    pr_items = User.query.filter().paginate.items(page=1, per_page=3)
    paginate = User.query.filter().paginate(page=1, per_page=3)
    print(paginate.pages) #总共能生成多少页
    print(paginate.page) #当前页码数
    print(paginate.has_next) #True
    print(paginate.has_prev) #Flase
    print(paginate.next_num) #获取下一页的页码数
    print(paginate.prev_num) #获取上一页的页码数
    print(paginate.items) #获当前页的对象 列表
    app.run(debug=True)
