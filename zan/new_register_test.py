from flask import render_template, Flask, request, redirect
import os
from datetime import timedelta
from wtforms import StringField, SelectMultipleField, RadioField, PasswordField, Form
from wtforms.validators import DataRequired, EqualTo, Length
import pymysql
class Sql_class():
    def get_conn(self):
        conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='wz')
        cur = conn.cursor()
        return conn, cur

    def close(self, conn,cur):
        cur.close()
        conn.close()

    def normal_ex(self, conn, cur, sql):
        cur.execute(sql)
        conn.commit()

    def query(self, cur, sql):
        cur.execute(sql)
        results = cur.fetchall()
        return results
class RegisterForm(Form):
    us = StringField(label=u'用户',
                     validators=[DataRequired(message='用户名不能为空...'),
                                 Length(min=2, max=12, message='长度为2-12位')],
                     render_kw={'class':'form-control',"style":"text-align=center"})
    ps = PasswordField(label=u'密码',
                       validators=[DataRequired(message='密码不能为空...'),
                                   Length(min=6, max=12, message='长度为6-12位'),
                                   EqualTo('ps2',message='密码不一致')],
                       render_kw={'class': 'form-control', "style": "text-align=center"})
    ps2 = PasswordField(label=u'确认密码',
                        validators=[DataRequired(message='密码不能为空...'),
                                    Length(min=6, max=12, message='长度为6-12位')],
                        render_kw={'class': 'form-control'})
    alias = StringField(label=u'笔名',
                        validators=[DataRequired(message='笔名不能为空...'),
                                    Length(max=100, message='别乱来')],
                        default='hahaha',
                        render_kw={"style": "text-align=center"})
    gender = RadioField(label=u'性别',
                        choices=((1, '男'), (2, '女')),
                        coerce=int,
                        default=1)
    hobby = SelectMultipleField(label=u'爱好',
                                choices=((1, '游戏'), (2, '学习'), (3,'运动'), (4, '吃饭'), (5, '睡觉')),
                                coerce=int,
                                default=[1, 3, 4, 5],
                                render_kw={'class':'form-control'})


app = Flask(__name__, template_folder='templates_2')
cls = Sql_class()
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 配置7天有效
@app.route('/', methods=['GET', 'POST'])
def join_3():
    form_obj = RegisterForm()
    if request.method == 'POST':
        print('request.form:')
        print(request.form)
        form_obj = RegisterForm(request.form)
        if form_obj.validate():
            ers = request.form.to_dict()
            print('ers:')
            print(ers)
            print('form_obj.data:')
            print(form_obj.data)
            return '注册成功'
    return render_template('register_3.html', form_obj=form_obj)

@app.route('/save_usr',methods=['post','get'])
def save_usr():
    username = request.form.get("us")
    password1 = request.form.get("ps")
    password2 = request.form.get("ps2")
    alias = request.form.get("alias")
    gender = request.form.get("gender")
    hobby = request.form.get("hobby")
    print('save_usr: username:'+username)
    print('save_usr: ps:'+password1)
    print('save_usr: ps2:'+password2)
    print('save_usr: alias:'+alias)
    print('save_usr: gender:'+gender)
    print('save_usr: hobby:'+hobby)
    return redirect("/")

if __name__ == '__main__':
    app.run()