import os

import werkzeug
from flask import Flask
from flask import render_template

app = Flask(__name__)
posts = [
    {
        "author": "Kalenshi Katebe",
        "title": "blog post 1",
        "content": "The first post content",
        "date_posted": "November 26 2020"
    },
    {
        "author": "Musonda Chinyimba",
        "title": "Journey to Canada",
        "content": "The first step of the Journey is to actually take that first step",
        "date_posted": "December 5 2020"
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("victoria/home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("victoria/about.html", title="About")


@app.errorhandler(werkzeug.exceptions.NotFound)
def pagenotfound(e):
    return render_template("victoria/pagenotfound.html")


DEBUG = os.environ.get("FLASK_DEBUG", True)
PORT = 5000
if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
