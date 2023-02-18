"""
Will contain python classes representing out forms
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    first_name = StringField(
        label="First Name", validators=[DataRequired(), Length(min=6, max=20)]
    )
    last_name = StringField(
        label="Last Name", validators=[DataRequired(), Length(min=6, max=20)]
    )

    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=6, max=20), ])
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), EqualTo('password'), ]
    )
    register = SubmitField(label="Register")


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), ])
    remember = BooleanField(label="Remember Me")
    login = SubmitField(label="Login")
