"""
Module to hold the post model fro the application
"""
from datetime import datetime
from victoria import db


class Post(db.Model):
    """Class representing posts made to the application"""
    __tablename__ = "post"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, nullable=True)
    content = db.Column(db.Text(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        """String representation of the post"""
        return f"{self.title}, Post Date: {self.date_posted}"
