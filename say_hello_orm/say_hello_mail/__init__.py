from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config.from_pyfile('settings.py')

mail = Mail(app)
