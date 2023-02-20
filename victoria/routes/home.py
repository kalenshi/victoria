from victoria import app
from flask import render_template

posts_data = [
    {
        "title": "My Updated Post",
        "content": "My first updated post!\r\n\r\nThis is exciting!",
        "user_id": 1
    },
    {
        "title": "A Second Post",
        "content": "This is a post from a different user...",
        "user_id": 2
    }]


@app.route("/")
@app.route("/home")
def home():
    return render_template("victoria/home.html", posts=posts_data)
