from flask import render_template, request

from victoria import db

from victoria.models import Post, User
from victoria.users.routes import users_bp


@users_bp.route("/posts/<int:user_id>", methods=["GET", "POST"])
def user_posts(user_id):
    max_per_page = 10
    per_page = request.args.get("per_page", 3)
    page = request.args.get("page", 1, type=int)
    user = db.get_or_404(User, user_id)

    posts = db.paginate(
        db.select(Post).filter_by(author=user).order_by(Post.id),
        per_page=per_page,
        max_per_page=max_per_page,
        page=page
    )
    return render_template("user_posts.html", user=user, posts=posts)
