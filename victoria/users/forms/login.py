from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), ])
    remember = BooleanField(label="Remember Me")
    login = SubmitField(label="Login")
