from flask import redirect, url_for
from flask_login import logout_user, current_user

from victoria import app


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
