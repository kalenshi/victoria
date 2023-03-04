import werkzeug
from flask import render_template

from victoria.main.routes import main_bp


@main_bp.errorhandler(werkzeug.exceptions.Forbidden)
def forbidden(error):
    print(error.description)
    return render_template(
        "victoria/pagenotfound.html", title="Page Not Found", error=error
    )
