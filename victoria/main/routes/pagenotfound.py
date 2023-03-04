import werkzeug
from flask import render_template

from victoria.main.routes import main_bp


@main_bp.errorhandler(werkzeug.exceptions.NotFound)
def pagenotfound(error):
    return render_template(
        "victoria/pagenotfound.html", title="Page Not Found", error=error
    )
