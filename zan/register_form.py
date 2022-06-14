# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField
# 导入wtf扩展的表单验证器
from wtforms.validators import DataRequired, EqualTo, Length
from flask import Flask, render_template, redirect, url_for, session, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '1'
class RegisterForm(FlaskForm):
    us = StringField(label=u'用户',
                     validators=[DataRequired(message='用户名不能为空...'),
                                 Length(min=2, max=12, message='长度为2-12位')],
                     render_kw={'placeholder':'请输入用户名...'})
    ps = PasswordField(label=u'密码',
                     validators=[DataRequired(message='密码不能为空...'),
                                 Length(min=6, max=12, message='长度为6-12位'),
                                 EqualTo('ps2',message='密码不一致')],
                     render_kw={'placeholder':'请输入密码...'})
    ps2 = PasswordField(label=u'确认密码',
                     validators=[DataRequired(message='密码不能为空...'),
                                 Length(min=6, max=12, message='长度为6-12位'),],
                     render_kw={'placeholder':'请输入密码...'})
    submit = SubmitField(u'提交')
@app.route('/', methods=['GET', 'POST'])
def root():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.us.data
        pswd = form.ps.data
        pswd2 = form.ps2.data
        print(name, pswd, pswd2)
        return '注册成功'
    else:
        if request.method == 'POST':
            flash(u'信息有误，请重新输入！')
        print(form.validate_on_submit())
    return render_template('register.html', form=form)


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RegisterForm()
    if request.method=='GET':
        return render_template('register.html', form=form)
    else:
        if form.validate_on_submit():
            name = form.us.data
            pswd = form.ps.data
            pswd2 = form.ps2.data
            print(name, pswd, pswd2)
            return '注册成功'
        return render_template('register.html', form=form)

@app.route('/index2', methods=['GET', 'POST'])
def index2():
    form = request.method()
    username = form.get("username")
    password = form.get("password")
    if not username:
        flash(u'用户名为空')
        return render_template("register.html")
    if not username:
        flash(u'密码为空')
        return render_template("register.html")
    if not username:
        flash(u'注册成功')
        return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()