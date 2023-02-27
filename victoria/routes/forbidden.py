from victoria import app
import werkzeug
from flask import render_template


@app.errorhandler(werkzeug.exceptions.Forbidden)
def forbidden(error):
    print(error.description)
    return render_template(
        "victoria/pagenotfound.html", title="Page Not Found", error=error
    )
