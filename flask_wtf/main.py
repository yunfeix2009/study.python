from tkinter.tix import Form

from flask import Flask, render_template, redirect, url_for, session, request, flash

# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField

import pymysql
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo, InputRequired, ValidationError, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = '1'






def my_length_check(form, field):
    if len(field.data) > 50:
        raise ValidationError('Field must be less than 50 characters')

def save_user(username,like_name,pwd):
    db = pymysql.connect(host="localhost", user="root", password="123456", database="wz",autocommit="on")

    db_curs = db.cursor()
    insert_sql = "INSERT INTO `wz`.`usr` (`usr_name`, `pwd`,`alias_name`) VALUES ('"+username+"', '"+pwd+"', '"+like_name+"');"
    try:
        db_curs.execute(insert_sql)
         # db.commit()
        print("ok")
    except:
        db.rollback()
        print("insert error")
    finally:
        db.close()



# ### 自定义表单类，文本字段、密码字段、提交按钮
# class Login(FlaskForm):
#     # us = StringField(label=u'用户：',validators=[DataRequired()])
#
#     # name = StringField('Name', [InputRequired(), my_length_check])
#     us = StringField(label=u'用户：',validators=[my_length_check()])
#     ps = PasswordField(label=u'密码', validators=[DataRequired(),
#                                                 EqualTo('ps2', message='密码不一致')])
#     ps2 = PasswordField(label=u'确认密码', validators=[DataRequired()])
#     submit = SubmitField(u'提交')


class Login(FlaskForm):
    us = StringField(label=u'用户：',validators=[DataRequired(message='用户名不能为空...')
                                            ,Length(min=6,max=12,message='长度为-612位')],
                     render_kw={'placeholder':'请输入用户名...','maxlength':12})

    like_name = StringField(label=u'别名：',validators=[DataRequired(message='别名不能为空...')
                                            ,Length(min=6,max=12,message='长度为6-12位')],
                     render_kw={'placeholder':'请输入别名...','maxlength':12})
    ps = PasswordField(label=u'密码', validators=[DataRequired(),
                                                EqualTo('ps2', message='密码不一致')])
    ps2 = PasswordField(label=u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'提交')



### 定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Login()
    if form.validate_on_submit():
        name = form.us.data
        like_name = form.like_name.data
        pswd = form.ps.data
        pswd2 = form.ps2.data
        print(name, like_name, pswd, pswd2)
        save_user(name,like_name, pswd)
        return '注册成功'
    else:
        if request.method == 'POST':
            flash(u'信息有误，请重新输入！')
        print(form.validate_on_submit())
    return render_template('register.html', form=form)



class MyForm(Form):
    name = StringField('Name', [InputRequired(), my_length_check])


if __name__ == '__main__':
    app.run()
#
print('testabc\n')
print(r'testabc\n')
name = "test"
age = 123
print(f"my name is {name},age is {age}")
print("中文".encode(encoding="gbk"))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode(encoding='utf-8'))
print(b'\xd6\xd0\xce\xc4'.decode())
us = StringField(label=u'用户：', validators=[DataRequired()])