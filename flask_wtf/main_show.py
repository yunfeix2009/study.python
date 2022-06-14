from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField,DecimalField,IntegerField\
    ,RadioField,SelectField,TextAreaField,DateField,HiddenField,DateTimeField,FloatField,SelectMultipleField

from wtforms.validators import DataRequired, EqualTo, InputRequired, ValidationError, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = '1'

class form_show(FlaskForm):
    name = StringField(label=u'姓名：',validators=[DataRequired(message='姓名不能为空...')
                                            ,Length(min=2,max=4,message='长度为2-4位')],
                     render_kw={'placeholder':'请输入姓名...','maxlength':4})

    alias = StringField(label=u'昵称（可不填）：', validators=[Length(min=2, max=4, message='长度为2-4位')],
                               render_kw={'placeholder': '请输入别名...', 'maxlength': 4})


    pwd = PasswordField(label=u'密码:', validators=[DataRequired(message='密码不能为空')
                                            ,Length(min=6,max=12,message='密码长度为6-12位')])

    is_useful = BooleanField(label=u'是否好用（可不填）:')

    math_q = FloatField(label=u'1+1.5的答案（可不填）:')


    height = DecimalField(label=u'身高:',validators=[DataRequired(message='身高不能为空...')],render_kw={'placeholder':'请输入身高...'})

    weight = DecimalField(label=u'体重',validators=[DataRequired(message='体重不能为空...')],render_kw={'placeholder':'请输入体重...'})

    age = IntegerField(label=u'年龄',validators=[DataRequired(message='年龄不能为空...')],render_kw={'placeholder':'请输入年龄...'})

    gender = RadioField('性别', choices = [('male','男'),('female','女')],validators=[DataRequired()])

    nationality = SelectField('国籍（可不填）:', choices = [('请选择', 'unknow'), ('中国', 'china'), ('美国', 'American'), ('加拿大', 'Canadian')])

    education = SelectMultipleField(label=u'学历（可不填）:',choices = [('1','小学及以下'),('2','初中'),('3','高中'),('4','大学及以上')])

    submit = SubmitField("提交")

    resp = TextAreaField(label='评价（可不填）:')

    date_field = DateField(label=u'当前时间',validators=[DataRequired(message='时间不能为空...')])


@app.route('/')
def index():
    form = form_show()
    return render_template('test_show.html', form=form)

if __name__ == '__main__':
    app.run()





