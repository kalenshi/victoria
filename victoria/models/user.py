"""
User module for the application
"""
from flask_login import UserMixin
from victoria import db, bcrypt, login_manager


@login_manager.user_loader
def load_user(user_id):
    """
    Gets a user from the database by specified id
    Args:
        user_id (int): The users primary key id
    Returns:
        User: the user from the database
    """
    return User.query.get(int(user_id))


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

    def __repr__(self):
        """String representation of the user model"""
        return f"User: {self.email}"

    def check_password(self, password: str) -> bool:
        """
        Checks that the passed in password is identical to the hashed password via
        Bcrypt algorithm
        Returns:
            bool : true if successful, False otherwise

        """
        return bcrypt.check_password_hash(self.password, password)
