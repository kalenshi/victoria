from forms import LoginForm
from victoria import app
from flask import render_template, flash, redirect, url_for


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
