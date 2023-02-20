from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Database Connections
app.config["SECRET_KEY"] = "ddbbb12fff42fa84db757a1bf1027f63"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()
from .routes import home, about, register, login, pagenotfound
