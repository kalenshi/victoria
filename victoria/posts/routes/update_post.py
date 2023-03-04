from datetime import datetime

from flask import render_template, url_for, redirect, flash, abort, request
from flask_login import current_user, login_required

from victoria import db

from victoria.models import Post
from victoria.posts.routes import posts_bp
from victoria.posts.forms.post import PostForm


@posts_bp.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = db.get_or_404(Post, post_id)
    if post.author != current_user:
        abort(403)
    post_form = PostForm()
    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.content = post_form.content.data
        post.date_updated = datetime.utcnow()
        db.session.commit()
        flash("Post has been Successfully Updated!", category="success")
        return redirect(url_for("posts_bp.post_page", post_id=post_id))
    elif request.method == "GET":
        post_form.title.data = post.title
        post_form.content.data = post.content

    return render_template(
        "create_post.html",
        post=post,
        post_form=post_form,
        legend="Update"
    )
