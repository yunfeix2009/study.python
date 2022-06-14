from flask import Flask
from flask import redirect
from flask import request
from mysql_fuc import *

app = Flask(__name__)
get_conn("zan")
temp = query("select ip from zan_1")
user_ips = []
for i in temp:
    user_ips.append(i[0])
close()
print(user_ips)

get_conn("zan")
zan = query("select count(*) from zan_1")
zan = zan[0][0]
close()


@app.route("/")
def index():
    ip = request.remote_addr
    if ip in user_ips:
        Label = '''<button style="color:grey">  取消  </button> <span class="zan">'''+str(zan)+'''</span> '''
    else:
        Label = '''<button style="color:red">  点赞  </button> <span class="zan">'''+str(zan)+'''</span> '''
    return '''
                <h1>今日话题 Topic of Today</h1>
                <div>
                    <form action="/savezan" method="post">
                        <span class="topic">《复仇者联盟》这个电影很赞！</span> ''' + Label + '''
                    </form>
                </div>
           '''


@app.route("/savezan", methods=['POST'])
def savezan():
    global zan
    ip = request.remote_addr
    print('ip:'+ip)
    if ip in user_ips:
        user_ips.remove(ip)
        zan = zan - 1
        get_conn('zan')
        normal_ex("delete from zan_1 where ip = '"+ip+"'")
        close()
        return redirect("/")
    else:
        user_ips.append(ip)
        print('user_ips:'+str(user_ips))
        zan = zan + 1
        print('zan:'+str(zan))
        get_conn('zan')
        normal_ex("insert into zan_1(ip) values ('"+ip+"')")
        close()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)