from flask import render_template

from victoria.main.routes import main_bp


@main_bp.route("/about")
def about():
    return render_template("about.html", title="About")
