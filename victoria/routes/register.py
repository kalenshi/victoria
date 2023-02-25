from victoria import app, bcrypt, db
from flask import flash, url_for, redirect, render_template
from flask_login import current_user
from victoria.forms import RegistrationForm
from victoria.models import User


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(location=url_for("home"))
    if register_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            register_form.password.data
        ).decode("utf-8")
        # Create the user and encrypt the password
        user = User(
            first_name=register_form.first_name.data,
            last_name=register_form.last_name.data,
            email=register_form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {register_form.email.data}", category="success")
        return redirect(location=url_for("login"))
    return render_template("auth/register.html", title="Register", register_form=register_form)
