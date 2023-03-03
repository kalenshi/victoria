from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class RequestResetForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    reset = SubmitField(label="Reset Password")
