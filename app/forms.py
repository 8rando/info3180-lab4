from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from app.forms import UploadForm


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    image= FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg','png'], 'Images only!')
    ])