from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from victoria.config import Config

# App initializations


db = SQLAlchemy()

bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = "users_bp.login"
login_manager.login_message_category = "info"


def creat_app(config_class=Config):
    """
    Creates  the victoria app with the passed in configuration

    Args:
        config_class (object): the config class to use; options are dev, local,stage prod and test

    Returns:
        object: Returns a flask app with set configuration
    """
    # create the app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    # Routes
    from victoria.users.routes import users_bp
    from victoria.main.routes import main_bp
    from victoria.posts.routes import posts_bp
    from victoria.error_handlers.routes import error_bp

    # Register blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(error_bp)

    return app
