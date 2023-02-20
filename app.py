import os
import json
from datetime import datetime

import werkzeug
from flask import (Flask, render_template, flash, redirect, url_for)
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# Database Connections
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # The directory where the app.py is
app.config["SECRET_KEY"] = "ddbbb12fff42fa84db757a1bf1027f63"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.app_context().push()


# Models
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


class Post(db.Model):
    """Class representing posts made to the application"""
    __tablename__ = "post"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        """String representation of the post"""
        return f"{self.title}, Post Date: {self.date_posted}"


posts_location = os.path.join(BASE_DIR, "posts.json")

with open(posts_location, "r") as fh:
    posts_data = json.load(fh)

posts = [

]


@app.route("/")
@app.route("/home")
def home():
    return render_template("victoria/home.html", posts=posts_data)


@app.route("/about")
def about():
    return render_template("victoria/about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        flash(f"Account created for {register_form.email.data}", category="success")
        return redirect(location=url_for("home"))
    return render_template("auth/register.html", title="Register", register_form=register_form)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "musonda@gmail.com" and login_form.password.data == "kalenshi":
            flash(f"Successfully logged in as {login_form.email.data}", category="success")
            return redirect(location=url_for("home"))
        else:
            flash("Login unsuccessful.Please check email and password", category="danger")
    return render_template("auth/login.html", title="Login", login_form=login_form)


@app.errorhandler(werkzeug.exceptions.NotFound)
def pagenotfound(e):
    return render_template("victoria/pagenotfound.html")


DEBUG = os.environ.get("FLASK_DEBUG", True)
PORT = os.environ.get("PORT", 5000)

if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
