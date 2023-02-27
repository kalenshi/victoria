from flask import url_for, redirect, render_template

from victoria import db, app
from victoria.models import Post, User


@app.route("/posts/<int:user_id>", methods=["GET", "POST"])
def user_posts(user_id):
    posts = db.session.execute(db.select(Post).filter_by(author_id=user_id)).scalars()
    user = db.get_or_404(User, user_id)
    return render_template("victoria/user_posts.html", user=user, posts=posts)
