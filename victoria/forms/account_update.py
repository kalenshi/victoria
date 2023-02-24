from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, StringField, EmailField, PasswordField
from wtforms.validators import Length, Email, ValidationError
from flask_login import current_user

from victoria.models import User


class AccountUpdateForm(FlaskForm):
    first_name = StringField(
        label="First Name", validators=[Length(min=3, max=30)]
    )
    last_name = StringField(label="Last Name", validators=[Length(min=3, max=30)])

    email = EmailField(label="Email", validators=[Email()])
    picture = FileField(
        label="Update Profile Picture",
        validators=[FileAllowed(["jpg", "png", "jpeg"])]
    )
    update = SubmitField(label="Update Account")

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
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "The email Address is already in Use.Please use another Email"
                )
