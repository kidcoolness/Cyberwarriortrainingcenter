import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..app import create_app
from ..app.models import db, User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    if not User.query.filter_by(email="admin@cyber.local").first():
        admin = User(
            name="Admin",
            email="admin@cyber.local",
            password_hash=generate_password_hash("admin123"),
            is_admin=True,
            is_trainer=True,
            is_training_manager=True
        )
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin user created.")
    else:
        print("ℹ️ Admin user already exists.")
