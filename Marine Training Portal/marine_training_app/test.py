from app import db
from app.models import Task

# ✅ Create a new task
new_task = Task(title="Cyber Defense Training", description="Complete a simulated cyber defense exercise.", category="Security")

# ✅ Add to database
db.session.add(new_task)
db.session.commit()

# ✅ Confirm task was added
Task.query.all()

