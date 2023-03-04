from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user

from victoria import db
from victoria.users.routes import users_bp
from victoria.users.forms.account_update import AccountUpdateForm
from victoria.users.utils.save_picture import save_picture


@users_bp.route("/account", methods=["GET", "POST"])
@login_required
def account():
    update_form = AccountUpdateForm()
    if update_form.validate_on_submit():
        if update_form.picture.data:
            current_user.image_file = save_picture(update_form.picture.data)
        current_user.first_name = update_form.first_name.data
        current_user.last_name = update_form.last_name.data
        current_user.email = update_form.email.data
        db.session.commit()
        flash(f"Your Account has been updated", category="success")
        return redirect(url_for("users_bp.account"))
    elif request.method == "GET":
        update_form.first_name.data = current_user.first_name
        update_form.last_name.data = current_user.last_name
        update_form.email.data = current_user.email
    profile_pic = url_for("static", filename=f"media/profile_pics/{current_user.image_file}")
    return render_template(
        "account.html", title="Account", profile_pic=profile_pic, update_form=update_form
    )
