from flask import flash, url_for, redirect, render_template
from flask_login import current_user

from victoria import bcrypt, db
from victoria.models import User
from victoria.users.routes import users_bp
from victoria.users.forms.register import RegistrationForm


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(location=url_for("main_bp.home"))
    if register_form.validate_on_submit():
        user = User(
            first_name=register_form.first_name.data,
            last_name=register_form.last_name.data,
            email=register_form.email.data,
            password=User.set_password_hash(register_form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {register_form.email.data}", category="success")
        return redirect(location=url_for("users_bp.login"))
    return render_template("register.html", title="Register", register_form=register_form)
