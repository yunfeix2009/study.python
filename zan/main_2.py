from flask import flash
from flask import url_for
from flask import render_template
from flask import redirect
from flask import request
from flask import Flask
from flask import session
import os
from datetime import timedelta
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField
from wtforms import PasswordField
from wtforms import RadioField
from wtforms import SelectField
from wtforms.validators import DataRequired, EqualTo, Length
import pymysql


class Sql_class():
    def get_conn(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='wz')
        cur = conn.cursor()
        return conn, cur

    def close(self, conn, cur):
        cur.close()
        conn.close()

    def normal_ex(self, conn, cur, sql):
        cur.execute(sql)
        conn.commit()

    def query(self, cur, sql):
        cur.execute(sql)
        results = cur.fetchall()
        return results


def get_current_usr_zan_wz_list():
    get_now_usr_zan_list_sql = '''
    select t1.title  ,t1.usr_name as author, t2.usr_id as zaner, t1.content, t1.id as wz_id
    from
    (SELECT u.alias_name, w.title,w.content , u.usr_name, w.id
        FROM wz.usr u, wz.wz_all w 
        where u.usr_name=w.usr_name and w.usr_name='{current_usr}') t1
    left join
    (select z.wz_id,z.usr_id,u.alias_name
        from wz.zan z,  wz.usr u
        where z.usr_id=u.usr_name) t2
    on t1.id=t2.wz_id and t2.usr_id='{current_usr}';
    '''.format(current_usr=session.get('username'))
    conn, cur = cls.get_conn()
    now_usr_zan_list = cls.query(cur, get_now_usr_zan_list_sql)
    cls.close(conn, cur)
    return now_usr_zan_list


def get_all_display_wz_data():
    get_all_display_wz_data_sql = '''
    SELECT t3.title, t3.author, t3.content, Count(t3.zaner) as count_zan, t3.id
    FROM   
    (SELECT t1.usr_name as author, t1.content, t1.title, t1.id, t2.usr_id   as zaner
        FROM 
            (SELECT u.alias_name, w.title, w.content, u.usr_name, w.id
                FROM   wz.usr u, wz.wz_all w
                WHERE  u.usr_name = w.usr_name) t1
            LEFT OUTER JOIN 
            (SELECT z.wz_id, z.usr_id, u.alias_name
                FROM   wz.zan z, wz.usr u
                WHERE  z.usr_id = u.usr_name) t2
    ON t1.id = t2.wz_id) t3
    GROUP  BY t3.title,
              t3.author; 
    '''
    conn, cur = cls.get_conn()
    now_display_wz_data = cls.query(cur, get_all_display_wz_data_sql)
    print(now_display_wz_data)
    cls.close(conn, cur)
    return now_display_wz_data


def get_wz_html_data(id):
    wz_sql = '''
    SELECT w.usr_name as author, w.title, w.content
    FROM   wz.wz_all as w
    WHERE  id={current_id};
    '''.format(current_id=id)
    zan_sql = '''
    select z.usr_id as zaner
    from wz.zan as z
    where z.wz_id = {current_id};
    '''.format(current_id=id)
    conn, cur = cls.get_conn()
    wz_data = cls.query(cur, wz_sql)
    zan_data = cls.query(cur, zan_sql)
    print(wz_data)
    print(zan_data)
    cls.close(conn, cur)
    return wz_data, zan_data


class RegisterForm(FlaskForm):
    us = StringField(label=u'用户',
                     validators=[DataRequired(message='用户名不能为空...'),
                                 Length(min=2, max=12, message='长度为2-12位')],
                     render_kw={'placeholder': '请输入用户名...'})
    ps = PasswordField(label=u'密码',
                       validators=[DataRequired(message='密码不能为空...'),
                                   Length(min=6, max=12, message='长度为6-12位'),
                                   EqualTo('ps2', message='密码不一致')],
                       render_kw={'placeholder': '请输入密码...'})
    ps2 = PasswordField(label=u'确认密码',
                        validators=[DataRequired(message='密码不能为空...'),
                                    Length(min=6, max=12, message='长度为6-12位'), ],
                        render_kw={'placeholder': '请输入密码...'})
    alias = StringField(label=u'笔名',
                        validators=[DataRequired(message='笔名不能为空...'),
                                    Length(max=100, message='别乱来'), ],
                        render_kw={'placeholder': '请输入笔名...'})
    submit = SubmitField(u'提交')


app = Flask(__name__, template_folder='templates_2')
cls = Sql_class()
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 配置7天有效


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('logins_2.html')


@app.route('/homepage', methods=['post', 'get'])
def logins():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get("password")
        print('homepage: username:' + str(username), 'password:' + str(password))
        get_now_user_pwd_sql = "select count(*) from usr where usr_name='" + username + "' and pwd='" + password + "'"
        print('homepage: get_now_user_pwd:' + get_now_user_pwd_sql)
        conn, cur = cls.get_conn()
        now_user_pwd = cls.query(cur, get_now_user_pwd_sql)
        print('homepage: n:' + str(now_user_pwd))
        cls.close(conn, cur)
        if int(now_user_pwd[0][0]) > 0:
            session['username'] = username
            session['password'] = password
            session.permanent = True
            session[username] = "success"
            return render_template('homepage.html', value=get_current_usr_zan_wz_list())
        else:
            return '<h1><span style="color:red"> 用户名或密码错误<span><h1>'
    else:
        return render_template('homepage.html', value=get_current_usr_zan_wz_list())


@app.route('/wz_list')
def wz_list():
    return render_template('wz_list.html', value=get_all_display_wz_data())


@app.route('/wz')
def wz():
    id = request.args.get('id')
    print(id)
    wz, zan = get_wz_html_data(id)
    print('wz')
    print(wz)
    print('***')
    print('zan')
    print(zan)
    print('***')
    author = wz[0][0]
    title = wz[0][1]
    content = wz[0][2]
    ls = []
    for i in zan:
        ls.append(i[0])
    likes = len(ls)
    usr = session['username']
    print('author')
    print(author)
    print('title')
    print(title)
    print('content')
    print(content)
    print('ls')
    print(ls)
    print('likes')
    print(likes)
    print('current_usr')
    print(usr)
    return render_template('wz.html', author=author, title=title, content=content, zaner=ls, likes=likes, usr=usr, id=id)


@app.route('/author')
def author():
    return render_template('wz.html', value=get_all_display_wz_data())


@app.route('/publish')
def publish():
    return render_template('publish_2.html')


@app.route('/publish_content', methods=['post'])
def publish_content():
    username = session.get('username')
    title = request.form.get('title')
    arc_contents = request.form.get('arc_contents')
    conn, cur = cls.get_conn()
    publish_sql = "insert into wz_all(title,usr_name,content) values('" + title + "','" + username + "','" + arc_contents + "')"
    print('publish_content: publish_sql:' + publish_sql)
    cls.normal_ex(conn, cur, publish_sql)
    cls.close(conn, cur)
    return render_template('publish_content.html')


@app.route('/join', methods=['GET', 'POST'])
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
    return render_template('register_2.html', form=form)


@app.route('/save_usr', methods=['post', 'get'])
def save_usr():
    username = request.form.get("us")
    password1 = request.form.get("ps")
    password2 = request.form.get("ps2")
    alias = request.form.get("alias")
    print('save_usr: usr_information:' + username)
    print('save_usr: usr_information:' + password1)
    print('save_usr: usr_information:' + password2)
    print('save_usr: usr_information:' + alias)
    if password1 == password2:
        conn, cur = cls.get_conn()
        save_usr_sql = "insert into usr values('" + username + "','" + password1 + "','" + alias + "')"
        print(save_usr_sql)
        cls.normal_ex(conn, cur, save_usr_sql)
        cls.close(conn, cur)
    return redirect("/")


@app.route('/dian_zan')
def dian_zan():
    username = session['username']
    wz_id = request.args.get('wz_id')
    dian_zan_sql = "insert into zan values('" + username + "','" + wz_id + "')"
    conn, cur = cls.get_conn()
    cls.normal_ex(conn, cur, dian_zan_sql)
    cls.close(conn, cur)
    return render_template('homepage.html', value=get_current_usr_zan_wz_list())


@app.route('/qu_xiao', methods=['post', 'get'])
def qu_xiao():
    username = session['username']
    wz_id = request.args.get('wz_id')
    dian_zan_sql = "delete from zan where wz_id='" + wz_id + "' and usr_id='" + username + "'"
    conn, cur = cls.get_conn()
    cls.normal_ex(conn, cur, dian_zan_sql)
    cls.close(conn, cur)
    return render_template('homepage.html', value=get_current_usr_zan_wz_list())


@app.after_request
def after_request(response):
    print('Access to : ' + request.full_path)
    return response


@app.before_request
def before_request():
    username = session.get('username')
    if request.path != "/login":
        if request.path == "/":
            pass
        elif request.path == "/homepage":
            pass
        elif request.path == "/join":
            pass
        elif request.path == "/save_usr":
            pass
        elif username == None or session.get(username) != 'success':
            return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
