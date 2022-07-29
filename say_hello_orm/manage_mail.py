from flask_mail import Message
from flask import render_template
from flask import request
from say_hello_mail import app, mail
from say_hello_mail.forms import SendForm


@app.route('/')
def mainpage():
    form = SendForm()
    # return 'hhh'
    return render_template('main_page.html', form=form)

@app.route('/send', methods=['POST'])
def send_mail():
    subject = request.form.get('subject')
    to = request.form.get('address')
    body = request.form.get('content')
    name = request.form.get('name')
    address = request.form.get('email_address')
    app.config.update(MAIL_DEFAULT_SENDER=(name, address))
    message = Message(subject, recipients=[to], sender=address, body=body)
    try:
        mail.send(message)
    except Exception as e:
        print(str(e))
        return 'failed'
    return 'successed'


if __name__ == '__main__':
    app.run(port=4445)