from victoria import app, bcrypt, db
from flask import flash, url_for, redirect, render_template
from flask_login import current_user
from victoria.forms import RegistrationForm
from victoria.models import User


@app.route("/register", methods=["GET", "POST"])
def register():
    update_form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(location=url_for("home"))
    if update_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            update_form.password.data
        ).decode("utf-8")
        # Create the user and encrypt the password
        user = User(
            first_name=update_form.first_name.data,
            last_name=update_form.last_name.data,
            email=update_form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {update_form.email.data}", category="success")
        return redirect(location=url_for("login"))
    return render_template("auth/register.html", title="Register", update_form=update_form)
