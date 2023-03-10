from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from sqlalchemy.exc import NoResultFound

from victoria import db
from victoria.users.forms.request_reset_form import RequestResetForm
from victoria.models import User
from victoria.users.routes import users_bp
from victoria.users.utils.send_mail import send_reset_email


@users_bp.route("/request_reset", methods=["GET", "POST"])
def request_reset():
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.home"))
    reset_form = RequestResetForm()
    if reset_form.validate_on_submit():
        try:
            user = db.session.execute(
                db.select(User).filter_by(email=reset_form.email.data)).scalar_one()
            send_reset_email(user)
            flash("Check your email for the reset link", category="success")
            return redirect(url_for("main_bp.home"))
        except NoResultFound:
            flash("We cannot find an account with that e-mail address!", category="danger")
    return render_template("request_reset.html", reset_form=reset_form, title="Request reset")
