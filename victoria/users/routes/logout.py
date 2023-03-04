from flask import redirect, url_for
from flask_login import logout_user

from victoria.users.routes import users_bp


@users_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main_bp.home"))
