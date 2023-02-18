import json
import os

import werkzeug
from flask import (Flask, render_template, flash, redirect, url_for)

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "ddbbb12fff42fa84db757a1bf1027f63"
BASE_DIR = os.path.dirname(__file__)  # The directory where the app.py is

posts_location = os.path.join(BASE_DIR, "posts.json")

with open(posts_location, "r") as fh:
    posts_data = json.load(fh)

posts = [
    {
        "author": "Kalenshi Katebe",
        "title": "blog post 1",
        "content": "The first post content",
        "date_posted": "November 26 2020"
    },
    {
        "author": "Musonda Chinyimba",
        "title": "Journey to Canada",
        "content": "The first step of the Journey is to actually take that first step",
        "date_posted": "December 5 2020"
    },
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
