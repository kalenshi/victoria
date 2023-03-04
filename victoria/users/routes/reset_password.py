from flask import render_template, flash, redirect, url_for
from flask_login import current_user

from victoria import db
from victoria.users.forms.reset_password import ResetPasswordForm
from victoria.models import User
from victoria.users.routes import users_bp


@users_bp.route("/reset_password<string:token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.home"))
    user = User.verify_reset_token(token)
    if not user:
        flash("Token is invalid or expired", category="warning")
        return redirect(url_for("users_bp.request_reset"))

    reset_password_form = ResetPasswordForm()
    if reset_password_form.validate_on_submit():
        user.password = User.set_password_hash(reset_password_form.password.data)
        db.session.commit()
        flash(
            "Your password has been successfully Updated. Login with your new password",
            category="success"
        )
        return redirect(url_for("users_bp.login"))
    return render_template(
        "auth/reset_password.html",
        reset_password_form=reset_password_form,
        title="reset_password"
    )
