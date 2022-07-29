from flask import Flask,render_template,url_for,flash

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired

from flask_bootstrap import Bootstrap


import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='secret key'


db = SQLAlchemy(app)
bootstrap=Bootstrap(app)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(64))

    def __repr__(self):
        return '<Post.>%s'%self.title


#定义表单类
class PostForm(FlaskForm):
    title = StringField('姓名',validators=[DataRequired()])
    category=SelectField('维护状态',choices=[('未维护','未维护'),('维护中','维护中'),('已维护','已维护')])
    submit = SubmitField('提交')


@app.route('/post/<int:post_id>',methods=['GET','POST'])
def show_post(post_id):
    form = PostForm()
    return render_template('post.html',form=form)


if __name__ == '__main__':
    app.run()