from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, Optional
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("confirm_password", message="Passwords must match.")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class TaskForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired()])
    label = StringField("Task Label (e.g. 1.1.3)", validators=[DataRequired()])
    section_label = StringField("Parent Section Label (e.g. 1.1)")
    description = TextAreaField("Task Description", validators=[DataRequired()])
    tryhackme_room = StringField("TryHackMe Room URL or ID")
    grading_type = SelectField("Grading Type", choices=[])
    parent_label = SelectField("Parent Section / Module", choices=[], validators=[Optional()])


    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.grading_type.choices = [
            ("auto", "Auto-Graded (Text)"),
            ("mcq", "Auto-Graded (Multiple Choice)"),
            ("trainer", "Trainer-Graded"),
            ("api", "TryHackMe API-Graded"),
            ("ai", "AI Auto-grading")
        ]

    
    correct_answer = StringField("Correct Answer", description="Case-sensitive answer.")
    mcq_choices = TextAreaField("MCQ Options (One per line)", description="Only used for MCQ tasks.")
    
    is_section_header = BooleanField("Is this a Section Header?")
    requires_upload = BooleanField("Requires Upload?")
    
    submit = SubmitField("Save Task")

class EditProfileForm(FlaskForm):
    name = StringField('Display Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField("Email", validators=[Optional(), Email()])
    current_password = PasswordField("Current Password", validators=[Optional()])
    new_password = PasswordField("New Password", validators=[Optional()])
    confirm_password = PasswordField("Confirm New Password", validators=[
        Optional(), EqualTo('new_password', message="Passwords must match.")
    ])

    position = StringField("Position", validators=[DataRequired()])
    accolades = TextAreaField("Accolades", validators=[Optional()])
    profile_picture = FileField("Profile Picture (JPG/PNG)", validators=[Optional(), FileAllowed(['jpg', 'png'])])
    password = current_password
    submit = SubmitField("Update Profile")

class OrgAssignmentForm(FlaskForm):
    platoon = StringField("Platoon")
    mission_element = StringField("Mission Element")
    team = StringField("Team")
    submit = SubmitField("Assign")

class AnswerForm(FlaskForm):
    answer = TextAreaField("Your Answer", validators=[DataRequired()])
    submit = SubmitField("Submit")

class MCQForm(FlaskForm):
    answer = RadioField("Choose an answer", validators=[DataRequired()])
    submit = SubmitField("Submit")

class TrainerAnswerForm(FlaskForm):
    answer = TextAreaField("Answer", validators=[DataRequired()])

class EditModuleForm(FlaskForm):
    name = StringField("Module Name", validators=[DataRequired()])
    submit = SubmitField("Save Changes")

class EditSectionForm(FlaskForm):
    name = StringField("Section Name", validators=[DataRequired()])
    submit = SubmitField("Save Changes")

class EditLabelForm(FlaskForm):
    label = StringField("New Label", validators=[DataRequired()])
    name = StringField("New Name", validators=[DataRequired()])
    submit = SubmitField("Update")