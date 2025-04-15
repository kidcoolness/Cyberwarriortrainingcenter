import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Course

app = create_app()
app.app_context().push()

# Your course seeding logic...
courses = [
    {"name": "Host Basic", "description": "Foundational training for Host Analysts"},
    {"name": "Host Senior", "description": "Advanced Host Analyst capabilities and mission readiness"},
    {"name": "Network Basic", "description": "Foundational training for Network Analysts"},
    {"name": "Network Senior", "description": "Advanced Network Analyst capabilities and mission execution"},
]

for c in courses:
    existing = Course.query.filter_by(name=c["name"]).first()
    if not existing:
        course = Course(name=c["name"], description=c["description"])
        db.session.add(course)

db.session.commit()
print("✅ Courses created!")