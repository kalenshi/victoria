import werkzeug
from flask import render_template

from victoria.error_handlers.routes import error_bp


@error_bp.app_errorhandler(werkzeug.exceptions.NotFound)
def error_404(error):
    return render_template(
        "error_404.html", title="Page Not Found", error=error
    )
