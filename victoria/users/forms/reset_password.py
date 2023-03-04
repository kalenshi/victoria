from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class ResetPasswordForm(FlaskForm):
    password = PasswordField(label="New Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(fieldname="password", message="The passwords must match!")
        ]
    )
    reset = SubmitField(label="Reset Password")
