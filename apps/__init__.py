from importlib import import_module
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from .database import db
from .config import Config


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "root.login"
login_manager.login_message_category = "info"

bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    
    from .views import bp
    app.register_blueprint(bp)
    
    return app