from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user

from victoria.models import User

from victoria import bcrypt, db
from victoria.users.forms.login import LoginForm
from victoria.users.routes import users_bp


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if current_user.is_authenticated:
        return redirect(location=url_for("main_bp.home"))
    if login_form.validate_on_submit():
        user = db.session.execute(
            db.select(User).filter_by(email=login_form.email.data)
        ).scalar_one()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(location=url_for("main_bp.home"))
        else:
            flash("Login unsuccessful.Please check email and password", category="danger")
    return render_template("login.html", title="Login", login_form=login_form)
