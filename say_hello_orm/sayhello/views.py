from flask import flash, redirect, url_for, render_template
from sayhello import db
from sayhello.forms import HelloForm
from flask import Blueprint
from .models import Message

# 创建蓝图
sayhello = Blueprint('sayhello', __name__, template_folder='templates', static_folder='static')


@sayhello.route('/', methods=['GET', 'POST'])
def index():
    print("*"*100)
    print(Message.timestamp)
    print(type(Message.timestamp))
    print("*"*100)

    messages = Message.query.order_by(Message.timestamp.desc()).all()
    print(messages)
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)
        db.session.commit()
        flash('Success！Your message have been sent to the world!')
        return redirect(url_for('sayhello.index'))
    return render_template('index.html', form=form, messages=messages)
