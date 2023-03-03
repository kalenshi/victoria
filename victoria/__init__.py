import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# App initializations
app = Flask(__name__)

app.config["SECRET_KEY"] = "ddbbb12fff42fa84db757a1bf1027f63"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Mail configs
mail_conf = {
    "MAIL_SERVER": "server170.web-hosting.com",
    "MAIL_PORT": 465,
    "MAIL_USE_SSL": True,
    "MAIL_USE_TLS": False,
    "MAIL_USERNAME": os.environ.get("MAIL_USERNAME"),
    "MAIL_PASSWORD": os.environ.get("MAIL_PASSWORD"),
}
app.config.update(mail_conf)
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# Routes
from .routes import home, about, register, login, pagenotfound
