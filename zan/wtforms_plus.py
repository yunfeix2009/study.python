### 视图
from wtforms import Form, RadioField, SelectMultipleField
from wtforms.fields import simple
from wtforms import validators
from flask import Flask,request,render_template

class RegForm(Form):
    username = simple.StringField(label="用户名",
                                  validators=[
                                      validators.DataRequired(message="数据不能为空！"),
                                      validators.length(min=4, max=6, message="用户名不能少于4位且不能大于6位")],
                                  render_kw={"class": "form-control", "style": "text-align:center"})
    password = simple.PasswordField(label="密码",
                                    validators=[
                                        validators.DataRequired(message="密码不能为空！"),
                                        validators.length(min=6, max=16, message="密码不能少于6位且不能大于6位"),
                                        validators.Regexp(regex="\d+", message="密码必须是数字")],
                                    render_kw={"class": "form-control", "style": "text-align:center"})
    re_password = simple.PasswordField(label="确认密码",
                                       validators=[
                                           validators.EqualTo(fieldname="password", message="两次密码不一致")],
                                       render_kw={"class": "form-control"})
    gender = RadioField(label="性别",
                             validators=[
                                 validators.DataRequired(message="请先选择一个性别！")],
                             choices=((1, "男"), (2, "女")),
                             coerce=int)
                             ### default=1,
    hobby = SelectMultipleField(label="爱好",
                                     choices=((1, "游戏"), (2, "妹子"), (3, "汉子")),
                                     coerce=int,
                                     default=[1, 2],
                                     render_kw={"class": "form-control"})

app=Flask(__name__)

@app.route("/register", methods=("GET", "POST"))
def reg():
    form_obj = RegForm()
    if request.method == "POST":
        print(request.form)
        form_obj = RegForm(request.form)
        if form_obj.validate():
            ers = request.form.to_dict()
            print(ers)
            print(form_obj.data)
            return "注册成功"
    return render_template("reg.html", form_obj=form_obj)


if __name__ == '__main__':
    app.run(debug=True)