from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from victoria.models import User


class RegistrationForm(FlaskForm):
    first_name = StringField(
        label="First Name", validators=[DataRequired(), Length(min=3, max=30)]
    )
    last_name = StringField(
        label="Last Name", validators=[DataRequired(), Length(min=3, max=30)]
    )

    email = EmailField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=6, max=20), ])
    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), EqualTo('password'), ]
    )
    register = SubmitField(label="Register")

    def validate_email(self, email):
        """
        Confirms that No user with the given email already exists in the Database

        Args:
            email (str) : A string representing the email
        Returns:
            bool : Returns false if the user doesn't exist
        Raises:
            ValidationError : if the user exists, raise ValidationError
        """
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("The email Address is already in Use.Please use another Email")

