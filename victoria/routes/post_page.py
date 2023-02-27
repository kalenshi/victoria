from flask import url_for, redirect, render_template, request
from flask_login import login_required

from victoria import app, db
from victoria.models import Post


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
@login_required
def post_page(post_id):
    post = db.get_or_404(Post, post_id)
    return render_template("victoria/post_page.html", title=f"Post {post.id}", post=post)
