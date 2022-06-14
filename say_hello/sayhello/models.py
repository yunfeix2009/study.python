from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(20))
    body = db.Column(db.string(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True)