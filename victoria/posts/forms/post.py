from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateTimeField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), ])
    date_posted = DateTimeField(label="Date Posted")
    date_updated = DateTimeField(label="Updated On")
    content = TextAreaField(label="Content", validators=[DataRequired(), ])
    submit = SubmitField(label="Post")
