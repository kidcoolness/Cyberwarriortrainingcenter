from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from .routes import main
from .models import db, User
from ..config import Config
from .uploads import uploads
from .bugs import bugs
from .memes import memes
from itsdangerous import URLSafeTimedSerializer

#from .utils import natural_key  # or .utils if same-level

migrate = Migrate()
login_manager = LoginManager()
mail = Mail()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    #fdyu gkci lvjo kpvx
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'cyberwarriortrainingcenter@gmail.com'
    app.config['MAIL_PASSWORD'] = 'fdyu gkci lvjo kpvx'
    app.config['MAIL_DEFAULT_SENDER'] = 'cyberwarriortrainingcenter@gmail.com'
   
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    # ✅ Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    mail.init_app(app)

    # ✅ Import blueprints *after* app + db are ready
    from .auth import auth
    from .routes import main
    from .admin import admin

    # ✅ Register blueprints here
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(uploads)
    app.register_blueprint(bugs)
    app.register_blueprint(memes)

    return app

