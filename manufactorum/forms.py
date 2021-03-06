from flask_wtf import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')


class UpdateTextForm(Form):
    file_name = StringField('File name', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
