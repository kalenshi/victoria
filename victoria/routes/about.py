from victoria import app
from flask import render_template


@app.route("/about")
def about():
    return render_template("victoria/about.html", title="About")
