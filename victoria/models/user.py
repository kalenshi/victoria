"""
User module for the application
"""
from victoria import db


class User(db.Model):
    """
    This will represent the user model to your application
    """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    image_file = db.Column(db.String(20), default="default.jpg", nullable=True)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)  # This isn't an actual attribute

    # It runs an extra query on the Posts model to grab any posts by this user

    def __repr__(self):
        """String representation of the user model"""
        return f"User: {self.email}"
