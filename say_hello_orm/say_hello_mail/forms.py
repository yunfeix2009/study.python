from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class SendForm(FlaskForm):
    subject = StringField('email subject:', validators=[DataRequired(), Length(1,50)])
    address = StringField('email address', validators=[DataRequired(), Length(1, 50)])
    content = TextAreaField('email', validators=[DataRequired(), Length(1, 500)])
    name = StringField('your name', validators=[DataRequired(), Length(1, 50)])
    email_address = StringField('your email address', validators=[DataRequired(), Length(1, 50)])
    submit = SubmitField()
