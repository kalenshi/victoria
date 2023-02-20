from victoria import app
from flask import flash, url_for, redirect, render_template

from forms import RegistrationForm


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        flash(f"Account created for {register_form.email.data}", category="success")
        return redirect(location=url_for("home"))
    return render_template("auth/register.html", title="Register", register_form=register_form)
