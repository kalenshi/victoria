from flask import render_template, request


from victoria import app, db
from victoria.models import Post


@app.route("/")
@app.route("/home")
def home():
    max_per_page = 10
    per_page = request.args.get("per_page", 5)
    page = request.args.get("page", 1, type=int)
    posts = db.paginate(
        db.select(Post).order_by(Post.id.asc()),
        page=page, per_page=per_page,
        max_per_page=max_per_page
    )

    return render_template("victoria/home.html", posts=posts, title="Home")
