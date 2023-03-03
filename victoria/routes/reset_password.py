from flask import render_template, flash, redirect, url_for
from flask_login import current_user

from victoria import app, db
from victoria.forms.reset_password import ResetPasswordForm
from victoria.models import User


@app.route("/reset_password<string:token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    user = User.verify_reset_token(token)
    if not user:
        flash("Token is invalid or expired", category="warning")
        return redirect(url_for("request_reset"))

    reset_password_form = ResetPasswordForm()
    if reset_password_form.validate_on_submit():
        user.password = User.set_password_hash(reset_password_form.password.data)
        db.session.commit()
        flash(
            "Your password has been successfully Updated. Login with your new password",
            category="success"
        )
        return redirect(url_for("login"))
    return render_template(
        "auth/reset_password.html",
        reset_password_form=reset_password_form,
        title="reset_password"
    )
