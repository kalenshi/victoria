from flask import render_template

from victoria import app, db
from victoria.models import Post


@app.route("/")
@app.route("/home")
def home():
    posts = db.session.execute(db.select(Post).order_by(Post.id)).scalars()
    return render_template("victoria/home.html", posts=posts, title="Home")
