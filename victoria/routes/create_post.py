from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from victoria import app, db
from victoria.forms import PostForm
from victoria.models import Post


@app.route("/post/new", methods=["GET", "POST"])
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
        return redirect(url_for("home"))
    return render_template(
        "victoria/create_post.html",
        title="Create Post",
        post_form=post_form,
        legend="New"
    )
