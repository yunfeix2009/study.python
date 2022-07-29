from say_hello_mail import app

app.secret_key = '1'

app.config.update(
    MAIL_SERVER='smtp.163.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='yunfeix2009@163.com',
    MAIL_PASSWORD='VQXNQTMMGOBHCAAO'
)
