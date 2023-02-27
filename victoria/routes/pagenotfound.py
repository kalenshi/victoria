from victoria import app
import werkzeug
from flask import render_template


@app.errorhandler(werkzeug.exceptions.NotFound)
def pagenotfound(error):
    return render_template(
        "victoria/pagenotfound.html", title="Page Not Found", error=error
    )
