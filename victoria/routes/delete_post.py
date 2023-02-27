from flask import redirect, url_for, abort, flash
from flask_login import login_required, current_user

from victoria import app, db
from victoria.models import Post


@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = db.get_or_404(Post, post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully.", category="success")
    return redirect(url_for("home"))
