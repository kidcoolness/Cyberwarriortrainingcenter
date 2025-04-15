from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired
import json
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)

    # ✅ Profile Additions
    profile_picture = db.Column(db.String(255), nullable=True, default="default.jpg")  # Profile Image
    position = db.Column(db.String(100), nullable=True, default="Marine")  # Rank/Position
    accolades = db.Column(db.Text, nullable=True)  # Awards/Badges
    is_student = db.Column(db.Boolean, default=True)
    is_trainer = db.Column(db.Boolean, default=False)
    is_training_manager = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    platoon = db.Column(db.String(100), nullable=True)
    mission_element = db.Column(db.String(100), nullable=True)
    team = db.Column(db.String(100), nullable=True)
    
    def get_roles(self):
        roles = ["Student"]
        if self.is_trainer:
            roles.append("Trainer")
        if self.is_admin:
            roles.append("Admin")
        return roles

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    label = db.Column(db.String(50), nullable=False)  # e.g., "1.0", "1.1", "1.1.1"
    section_label = db.Column(db.String(50), nullable=True)  # deprecated
    parent_label = db.Column(db.String(50), nullable=True)  # ✅ NEW: true parent for sections/tasks
    is_section_header = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text, nullable=True)
    grading_type = db.Column(db.String(50), nullable=True)
    correct_answer = db.Column(db.Text, nullable=True)
    requires_upload = db.Column(db.Boolean, default=False)
    choices = db.Column(db.Text, nullable=True)  # For MCQ
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    @property
    def number(self):
        return self.label
    
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"))
    submission_text = db.Column(db.Text)
    status = db.Column(db.String(50))  # pending, approved, rejected
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # ✅ Relationships
    user = db.relationship("User", backref="submissions")
    task = db.relationship("Task", backref="submissions")

class TrainerReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    approved = db.Column(db.Boolean, nullable=False)
    reviewed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    points = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setting_name = db.Column(db.String(50), unique=True, nullable=False)
    setting_value = db.Column(db.Text, nullable=False)

class TaskAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)
    status = db.Column(db.String(20), default="incomplete")  # "incomplete", "in progress", "completed"
    assigned_at = db.Column(db.DateTime, default=datetime.utcnow)

    task = db.relationship("Task", backref="assignments")
    user = db.relationship("User", backref="assignments")

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

class CourseEnrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    progress = db.Column(db.Integer, default=0)  
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)  # ✅ Track if course is completed
    course = db.relationship("Course", backref="enrollments")
    user = db.relationship("User", backref="enrollments")  # ✅ Avoids circular dependency

class CourseTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)
    sequence = db.Column(db.Integer, nullable=False)  # ✅ Determines task order
    task = db.relationship("Task", backref="course_tasks")  # ✅ Allows accessing Task details
    course = db.relationship("Course", backref="course_tasks")  # ✅ Allows accessing Course details

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    label = db.Column(db.String(50))  # e.g. "1.2"
    title = db.Column(db.String(255))  # e.g. "Analyze Logs"
    sequence = db.Column(db.Integer)

