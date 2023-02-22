from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user

from victoria.models import User
from victoria.forms import LoginForm
from victoria import app, bcrypt


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(location=url_for("home"))
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get("next")

            return redirect(next_page) if next_page else redirect(location=url_for("home"))
        else:
            flash("Login unsuccessful.Please check email and password", category="danger")
    return render_template("auth/login.html", title="Login", login_form=login_form)
