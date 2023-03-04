"""
User module for the application
"""
from datetime import timedelta, datetime

from flask import abort, current_app
from flask_login import UserMixin
import jwt
from victoria import db, bcrypt, login_manager


@login_manager.user_loader
def load_user(user_id):
    """
    Gets a user from the database by specified id

    Args:
        user_id (int): The users_bp primary key id

    Returns:
        User: the user from the database
    """
    return db.get_or_404(User, user_id)


class User(db.Model, UserMixin):
    """
    This will represent the user model to your application
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default="default.png", nullable=True)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)  # This isn't an actual attribute
    # It runs an extra query on the Posts model to grab any posts by this user

    def __int__(self, first_name, last_name, email, password, image_file="default.png"):
        """
        Initializes the User model

        Returns:
             None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.normalize_email(email)
        self.image_file = image_file
        self.password = self.set_password_hash(password)

    @staticmethod
    def normalize_email(email):
        """
        Normalizes the email

        ARgs:
            email(str) : the email provided
        Returns:
            str : The normalized email
        """
        try:
            em, domain = email.split("@")
            normalized_email = f"{em}{domain.lower()}"
        except ValueError:
            abort(400)
        return normalized_email

    def __repr__(self):
        """
        String representation of the user model

        Returns:
            str : A string representation of the user model
        """
        return f"User: {self.email}"

    @staticmethod
    def set_password_hash(password):
        """
        Hashes the password using bcrypt algorithm for database storage

        Args:
            password (str): the password string to be hashed

        Returns:
            str : The hashed password

        """
        return bcrypt.generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Checks that the passed in password is identical to the hashed password via
        Bcrypt algorithm

        Args:
            password(str): the password string to be checked

        Returns:
            bool : true if successful, False otherwise
        """
        return bcrypt.check_password_hash(self.password, password)

    def get_reset_token(self, expires_delta=1800):
        """
        Creates the access token  To be used to reset the user password

        Args:
            expires_delta (timedelta) : Time to live for the created token

        Returns:
            str : JSON web token
        """
        payload = {
            "user_id": self.id,
            "exp": datetime.utcnow() + timedelta(seconds=expires_delta)
        }
        token = jwt.encode(
            payload=payload,
            key=current_app.config.get("SECRET_KEY"),
            algorithm="HS256"
        )
        return token

    @staticmethod
    def verify_reset_token(token):
        """
        Verifies that the provided token belongs to the user

        Args:
            token (str): The payload in encoded form

        Returns:
            User : A User instance if verification else None

       Throws:
            ExpiredSignatureError: when signature has expired
        """
        try:
            serialized = jwt.decode(
                jwt=token,
                key=current_app.config.get("SECRET_KEY"),
                algorithms=["HS256"]
            )
            return db.get_or_404(User, serialized["user_id"])
        except jwt.ExpiredSignatureError:
            return None
