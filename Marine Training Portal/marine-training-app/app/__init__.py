from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from app.routes import main
from app.models import db, User
from config import Config

migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ✅ Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # ✅ Import blueprints *after* app + db are ready
    from app.auth import auth
    from app.routes import main
    from app.admin import admin

    # ✅ Register blueprints here
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix="/admin")

    return app

