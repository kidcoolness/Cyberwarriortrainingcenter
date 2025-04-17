import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..app import create_app
from ..app.models import db, User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    admin = User.query.filter_by(email="admin@example.com").first()
    if not admin:
        print("Creating admin...")
        admin = User(
            name="Admin User",
            email="admin@example.com",
            is_admin=True,
            is_trainer=True,
            is_training_manager=True,
        )
        admin.password_hash = generate_password_hash("admin123")
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin user created.")
    else:
        print("🔁 Admin user already exists. Resetting password...")
        admin.password_hash = generate_password_hash("admin123")
        db.session.commit()
        print("✅ Admin password reset.")
