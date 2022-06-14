from flask import render_template
from flask import redirect
from flask import request
from flask import Flask

class Sql_class():
    def get_conn(self):
        import pymysql
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

app = Flask(__name__)
cls = Sql_class()

def find_all_user():
    conn, cur = cls.get_conn()
    result = cls.query(cur, 'SELECT usr_name, pwd FROM usr')
    print('result:'+str(result))
    ret = {}
    for r in result:
        ret[r[0]]=r[1]
    print('ret:'+str(ret))
    return ret


def find_all_data():
    all_contents_list=[]
    with open('D:\\dev\projs\\flask_study\\wz_publish_list_main', 'r',encoding='UTF-8') as f:
        for line in f:
            all_contents_list.append(line.split('/'))
    return all_contents_list

app = Flask(__name__)
creater = find_all_user()



@app.route('/')
def index():
    return render_template('logins.html')

@app.route('/get_login')
def logins():
    username = request.args.get('username')
    password = request.args.get("password")
    print(username,password)
    if username in creater.keys():
        if password==creater[username]:
            global ip
            ip = request.remote_addr
            return redirect('/menu')
        else:
            return '<h1><span style="color:red"> 用户名或密码错误<span><h1>'
    else:
        return '<h1><span style="color:blue"> 用户名或密码错误<span><h1>'

@app.route('/post_logins',methods=['post'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username,password)
    if username in creater.keys():
        if password==creater[username]:
            return redirect('/menu')
        else:
            return '<h1><span style="color:red"> 用户名或密码错误<span><h1>'
    else:
        return '<h1><span style="color:blue"> 用户名或密码错误<span><h1>'

@app.route('/display_all')
def display_all():
    all_zan_usr = []
    with open('C:\\Users\\steven\\PycharmProjects\\zan\\wz_publish_list_main', 'r',encoding='UTF-8') as f:
        for line in f:
            try:
                a = list(line.split('/')[3])
            except:
                continue
            b = line.split('/')[3]
            temp = b.replace('\n','')
            all_zan_usr.append(temp)
        print(str(all_zan_usr))
    if usr in all_zan_usr:
        label = '<button style="color:grey">  取消  </button> <span class="zan">'''+str(len(user_ips))
        return render_template('display_list.html', value=find_all_data(), label=label)
    else:
        label = '<button style="color:"red">  点赞  </button> <span class="zan">'''+str(len(user_ips))
        return render_template('display_list.html', value=find_all_data(), label=label)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/search')
def main():
    """首页"""
    return render_template('search.html')

@app.route('/display')
def display():
    keyword_list=[]
    ls = find_all_data()
    key_word = request.args.get("key_word")
    for i in ls:
        if key_word in i[1]:
            keyword_list.append(i)
    all_zan_usr = []
    with open('C:\\Users\\steven\\PycharmProjects\\zan\\wz_publish_list_main', 'r',encoding='UTF-8') as f:
        for line in f:
            try:
                a = list(line.split('/')[3])
            except:
                continue
            b = line.split('/')[3]
            temp = b.replace('\n','')
            all_zan_usr.append(temp)

    if ip in all_zan_usr:
        label = '<button style="color:g"rey">  取消  </button> <span class="zan">'''+str(len(user_ips))
        return render_template('display_list.html', value=keyword_list, label=label)
    else:
        label = '<button style="color:"red">  点赞  </button> <span class="zan">'''+str(len(user_ips))
        return render_template('display_list.html', value=keyword_list, label=label)

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/publish_content',methods=['post'])
def publish_content():
    """首页"""
    creater = request.form.get('creater')
    title = request.form.get('title')
    arc_contents = request.form.get('arc_contents')
    str = creater+"/"+title+"/"+arc_contents+"/"+'[]'+'\n'
    with open('D:\\dev\projs\\flask_study\\wz_publish_list_main','a',encoding='UTF-8') as f:
        f.write(str)
    if ip in user_ips:
        label = '<button style="color:g"rey">  取消  </button> <span class="zan">'''+str(len(user_ips))
        return render_template('display_list.html', value=find_all_data(), label=label)
    else:
        label = '<button style="color:"red">  点赞  </button> <span class="zan">'''+str(len(user_ips))
        return render_template('display_list.html', value=find_all_data(), label=label)



@app.route("/save_zan", methods=['POST'])
def save_zan():
    global zan
    ip = request.remote_addr
    print('ip:'+ip)
    if ip in user_ips:
        user_ips.remove(ip)
        zan = zan - 1
        conn, cur = cls.get_conn()
        cls.normal_ex(conn, cur, "delete from usr where ip = '"+ip+"'")
        cls.close(conn, cur)
        return redirect("/menu")
    else:
        user_ips.append(ip)
        print('user_ips:'+str(user_ips))
        zan = zan + 1
        print('zan:'+str(zan))
        conn, cur = cls.get_conn()
        cls.normal_ex(conn, cur, "insert into zan_wz(ip) values ('"+ip+"')")
        cls.close(conn, cur)
        return redirect("/menu")


@app.route('/join')
def join():
    return render_template("join.html")

@app.route('/save_usr',methods=['post','get'])
def save_usr():
    username = request.args.get("usr_name")
    password1 = request.args.get("pw")
    password2 = request.args.get("p2")
    alise = request.args.get("alise")
    ip = request.remote_addr
    print(username, password1, password2, alise)
    if password1==password2:
        conn, cur = cls.get_conn()
        cls.normal_ex(conn, cur, "insert into usr values('"+ip+"','"+username+"','"+password1+"','"+alise+"')")
        cls.close(conn, cur)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)