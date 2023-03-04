from flask import render_template
from flask_login import login_required

from victoria import db
from victoria.models import Post
from victoria.posts.routes import posts_bp


@posts_bp.route("/post/<int:post_id>", methods=["GET", "POST"])
@login_required
def post_page(post_id):
    post = db.get_or_404(Post, post_id)
    return render_template("post_page.html", title=f"Post {post.id}", post=post)
