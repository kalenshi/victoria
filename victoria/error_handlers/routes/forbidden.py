import werkzeug
from flask import render_template

from victoria.error_handlers.routes import error_bp


@error_bp.app_errorhandler(werkzeug.exceptions.Forbidden)
def error_403(error):
    print(error.description)
    return render_template(
        "error_404.html", title="Page Not Found", error=error
    )
