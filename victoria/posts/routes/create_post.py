from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from victoria import db

from victoria.models import Post
from victoria.posts.routes import posts_bp
from victoria.posts.forms.post import PostForm


@posts_bp.route("/post/new", methods=["GET", "POST"])
@login_required
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post = Post(
            title=post_form.title.data,
            content=post_form.content.data,
            author_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()
        flash("Post created successfully.", category="success")
        return redirect(url_for("main_bp.home"))
    return render_template(
        "create_post.html",
        title="Create Post",
        post_form=post_form,
        legend="New"
    )
