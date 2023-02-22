from flask import render_template, url_for
from flask_login import login_required

from victoria import app


@app.route("/account")
@login_required
def account():
    return render_template("auth/account.html", title="Account")
