import os
import secrets

from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user

from victoria import app, db
from victoria.forms.account_update import AccountUpdateForm


def save_picture(form_picture):
    """
    Saves the picture provided as th current users profile picture
    Args:
        form_picture (str): the location on the user's machine to the picture
    Return:
        file_name (str) : The name of the new profile picture
    """
    random_hex = secrets.token_hex(16)
    _, file_ext = os.path.splitext(form_picture.filename)
    file_name = f"{random_hex}{file_ext.lower()}"
    picture_path = os.path.join(app.root_path, "static", "media", "profile_pics", file_name)
    # Resize the image before saving it
    output_size = (125, 125)  # The dimensions of the photo we want
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)
    return file_name


@app.route("/account", methods=["GET", "POST"])
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
        return redirect(url_for("account"))
    elif request.method == "GET":
        update_form.first_name.data = current_user.first_name
        update_form.last_name.data = current_user.last_name
        update_form.email.data = current_user.email
    profile_pic = url_for("static", filename=f"media/profile_pics/{current_user.image_file}")
    return render_template(
        "auth/account.html", title="Account", profile_pic=profile_pic, update_form=update_form
    )
