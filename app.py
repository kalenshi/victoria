import os

import werkzeug
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello World!</h1>"


@app.route("/about")
def about():
    return "<h1>About Page!</h1>"


@app.errorhandler(werkzeug.exceptions.NotFound)
def pagenotfound(e):
    return "<h1>OOPS Page Not Found!!</h1>"


DEBUG = os.environ.get("FLASK_DEBUG", True)
PORT = 5000
if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
