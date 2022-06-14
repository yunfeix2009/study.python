from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")
@app.route("/user/<username>")
def shou_user_info(username):
    return render_template("user.html",list1=['amy','steven','duu','fly'])

@app.route("/test")
def test():
    return render_template("test.html",list1=['amy','steven','duu','fly'])
if __name__=='__main__':
    app.run()