from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User, Task, Course, CourseTask, CourseEnrollment, Submission,TaskAssignment, TrainerReview, Platoon, MissionElement, Team
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional
from .forms import TaskForm, OrgAssignmentForm
import json
from .utils import natural_key
import os
admin = Blueprint("admin", __name__)

# ✅ Admin Dashboard
@admin.route("/admin")
@login_required
def dashboard():
    if not current_user.is_admin:  # ✅ Use is_admin instead of role
        return "Unauthorized", 403

    users = User.query.all()
    tasks = Task.query.all()
    return render_template("admin/dashboard.html", users=users, tasks=tasks)

# ✅ Manage Users Page
@admin.route("/admin/manage_users")
@login_required
def manage_users():
    if not (current_user.is_admin or current_user.is_training_manager):
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))

    # If Admin → see all users
    if current_user.is_admin:
        users_query = User.query.filter(User.is_student == True)

        # 🚨 Apply scoping if Training Manager (non-admin)
        if current_user.is_training_manager and not current_user.is_admin:
            if current_user.platoon_id:
                users_query = users_query.filter(User.platoon_id == current_user.platoon_id)
            if current_user.mission_element_id:
                users_query = users_query.filter(User.mission_element_id == current_user.mission_element_id)
            if current_user.team_id:
                users_query = users_query.filter(User.team_id == current_user.team_id)

        users = users_query.all()
    else:
        # Training Manager → filter by their assigned Platoon / ME / Team
        query = User.query

        if current_user.platoon_id:
            query = query.filter(User.platoon_id == current_user.platoon_id)
        if current_user.mission_element_id:
            query = query.filter(User.mission_element_id == current_user.mission_element_id)
        if current_user.team_id:
            query = query.filter(User.team_id == current_user.team_id)

        users = query.all()

    return render_template("admin/manage_users.html", users=users)

# ✅ Update User Role
@admin.route("admin/update_role/<int:user_id>", methods=["POST"])
@login_required
def update_role(user_id):
    if not current_user.is_admin:  # ✅ Use is_admin instead of role
        flash("Access denied: Admins only.", "danger")
        return redirect(url_for("main.dashboard"))

    user = User.query.get_or_404(user_id)
    
    user.is_trainer = "is_trainer" in request.form
    user.is_admin = "is_admin" in request.form
    user.is_training_manager = "is_training_manager" in request.form

    db.session.commit()

    flash(f"Roles updated for {user.name}.", "success")
    return redirect(url_for("admin.manage_users"))

@admin.route("admin/manage_courses")
@login_required
def manage_courses():
    if not (current_user.is_admin or current_user.is_training_manager):
        flash("Access denied: Admins only.", "danger")
        return redirect(url_for("main.dashboard"))

    courses = Course.query.all()
    return render_template("admin/manage_courses.html", courses=courses)

@admin.route("admin/create_course", methods=["GET", "POST"])
@login_required
def create_course():
    if not (current_user.is_admin or current_user.is_training_manager):
        flash("Access denied: Admins only.", "danger")
        return redirect(url_for("main.dashboard"))

    form = CourseForm()

    if form.validate_on_submit():
        new_course = Course(name=form.name.data, description=form.description.data)
        db.session.add(new_course)
        db.session.commit()
        flash("Course created successfully!", "success")
        return redirect(url_for("admin.manage_courses"))

    return render_template("admin/create_course.html", form=form)

@admin.route("/edit_course/<int:course_id>", methods=["GET", "POST"])
@login_required
def edit_course(course_id):
    if not (current_user.is_trainer or current_user.is_admin or current_user.is_training_manager):
        abort(403)
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    task_form = TaskForm()

    # Populate grading_type choices if needed dynamically
    task_form.grading_type.choices = [
        ("auto", "Auto-Graded (Text)"),
        ("mcq", "Auto-Graded (Multiple Choice)"),
        ("trainer", "Trainer-Graded"),
        ("api", "TryHackMe API-Graded")
    ]

    tasks = sorted(
        Task.query.filter_by(course_id=course_id).all(),
        key=lambda t: natural_key(t.label)
    )

    if form.validate_on_submit():
        course.name = form.name.data
        course.description = form.description.data
        db.session.commit()
        flash("Course updated successfully!", "success")
        return redirect(url_for("admin.edit_course", course_id=course.id))

    return render_template("admin/edit_course.html", form=form, task_form=task_form, course=course, tasks=tasks)

@admin.route("/delete_course/<int:course_id>", methods=["POST"])
@login_required
def delete_course(course_id):
    if not current_user.is_admin:
        flash("Access denied: Admins only.", "danger")
        return redirect(url_for("main.dashboard"))

    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash("Course deleted successfully!", "success")
    return redirect(url_for("admin.manage_courses"))

from .forms import TaskForm

@admin.route("/create_task/<int:course_id>", methods=["GET", "POST"])
@login_required
def create_task(course_id):
    form = TaskForm()

    if form.validate_on_submit():
        label = form.label.data.strip()
        title = form.title.data.strip()
        is_section = form.is_section_header.data
        parent_label = form.parent_label.data.strip() if form.parent_label.data else None

        if not parent_label:
            if label.count(".") == 1:
                parent_label = label.rsplit(".", 1)[0] + ".0"
            elif label.count(".") == 2:
                parent_label = label.rsplit(".", 1)[0]

        # 🔐 Failsafe
        if not parent_label:
            parent_label = label

        new_task = Task(
            course_id=course_id,
            label=label,
            title=title,
            description=form.description.data,
            grading_type=form.grading_type.data,
            correct_answer=form.correct_answer.data,
            is_section_header=is_section,
            requires_upload=form.requires_upload.data,
            parent_label=parent_label
        )

        # ✅ SAVE MCQ OPTIONS
        if form.grading_type.data == "mcq" and form.mcq_choices.data:
            choices = [c.strip() for c in form.mcq_choices.data.splitlines() if c.strip()]
            new_task.choices = json.dumps(choices)

        db.session.add(new_task)
        db.session.commit()

        flash("✅ Task created and saved!", "success")
        return redirect(url_for("admin.edit_course", course_id=course_id))

    return render_template("admin/create_task.html", form=form)

@admin.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    if not (current_user.is_admin or current_user.is_training_manager):
        flash("Access denied", "danger")
        return redirect(url_for("main.dashboard"))

    task = Task.query.get_or_404(task_id)
    form = TaskForm(obj=task)

    # ✅ Build parent options from all tasks in same course (excluding self)
    all_tasks = Task.query.filter(Task.course_id == task.course_id, Task.id != task.id).all()
    parent_choices = [("", "— No Parent —")]
    for t in all_tasks:
        if t.label.count(".") <= 2:  # only modules and sections
            parent_choices.append((t.label, f"{t.label} – {t.title}"))

    form.parent_label.choices = parent_choices

    # ✅ Refill grading type choices
    form.grading_type.choices = [
        ("auto", "Auto-Graded (Text)"),
        ("mcq", "Auto-Graded (Multiple Choice)"),
        ("trainer", "Trainer-Graded"),
        ("api", "TryHackMe API-Graded")
    ]

    # ✅ Load saved MCQ options
    if form.grading_type.data == "mcq" and form.mcq_choices.data:
        choices = [c.strip() for c in form.mcq_choices.data.splitlines() if c.strip()]
        task.choices = json.dumps(choices)
    else:
        task.choices = None


    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.grading_type = form.grading_type.data
        task.correct_answer = form.correct_answer.data
        task.requires_upload = form.requires_upload.data
        task.tryhackme_room = form.tryhackme_room.data
        task.parent_label = form.parent_label.data or None

        # Save MCQ
        if form.grading_type.data == "mcq" and form.mcq_choices.data:
            lines = [l.strip() for l in form.mcq_choices.data.splitlines() if l.strip()]
            task.choices = json.dumps(lines)
        else:
            task.choices = None

        db.session.commit()
        flash("✅ Task updated", "success")
        return redirect(url_for("admin.edit_course", course_id=task.course_id))

    return render_template("admin/edit_task.html", form=form, task=task, course_id=task.course_id)

class CourseForm(FlaskForm):
    name = StringField("Course Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    submit = SubmitField("Create Course")

@admin.route("/assign_unit/<int:user_id>", methods=["GET", "POST"])
@login_required
def assign_unit(user_id):
    if not (current_user.is_admin or current_user.has_role("training_manager")):
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))

    user = User.query.get_or_404(user_id)
    form = OrgAssignmentForm(obj=user)

    if form.validate_on_submit():
        user.platoon = form.platoon.data
        user.mission_element = form.mission_element.data
        user.team = form.team.data
        db.session.commit()
        flash("User assigned to unit successfully!", "success")
        return redirect(url_for("admin.manage_users"))

    return render_template("admin/assign_unit.html", user=user, form=form)

@admin.route("/unit_progress")
@login_required
def unit_progress():
    if not (current_user.is_admin or current_user.is_training_manager):
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))

    users = User.query.all()
    report = {}

    for user in users:
        key = f"{user.platoon or 'Unassigned'} → {user.mission_element or 'Unassigned'} → {user.team or 'Unassigned'}"
        if key not in report:
            report[key] = {"users": [], "completed": 0, "total": 0}

        report[key]["users"].append(user)
        enrollments = CourseEnrollment.query.filter_by(user_id=user.id).all()
        for e in enrollments:
            report[key]["total"] += 1
            if e.completed:
                report[key]["completed"] += 1

    return render_template("admin/unit_progress.html", report=report)

@admin.route("/admin/create_module/<int:course_id>", methods=["POST"])
@login_required
def create_module(course_id):
    label = request.form.get("label").strip()
    title = request.form.get("title").strip()

    module = Task(
        course_id=course_id,
        label=label,
        title=title,
        description="",
        grading_type="trainer",  # placeholder
        is_section_header=True,
        parent_label=label,      # ✅ Module's parent is itself
        section_label=None
    )

    db.session.add(module)
    db.session.commit()
    flash("✅ Module created!", "success")
    return redirect(url_for("admin.edit_course", course_id=course_id))

@admin.route("/admin/create_section/<int:course_id>", methods=["POST"])
@login_required
def create_section(course_id):
    module_label = request.form.get("module_label").strip()
    label = request.form.get("label").strip()
    title = request.form.get("title").strip()

    section = Task(
        course_id=course_id,
        label=label,
        title=title,
        description="",
        grading_type="trainer",  # placeholder
        is_section_header=True,
        parent_label=module_label,   # ✅ Section's parent is module
        section_label=module_label   # (optional for clarity, used in older logic)
    )

    db.session.add(section)
    db.session.commit()
    flash("✅ Section created!", "success")
    return redirect(url_for("admin.edit_course", course_id=course_id))

@admin.route("/edit_module/<int:module_id>", methods=["GET", "POST"])
@login_required
def edit_module(module_id):
    module = Module.query.get_or_404(module_id)
    form = EditModuleForm(obj=module)
    if form.validate_on_submit():
        module.name = form.name.data
        db.session.commit()
        flash("Module updated successfully!", "success")
        return redirect(request.referrer or url_for("admin.manage_courses"))
    return render_template("admin/edit_module.html", form=form)

@admin.route("/edit_section/<int:section_id>", methods=["GET", "POST"])
@login_required
def edit_section(section_id):
    section = Section.query.get_or_404(section_id)
    form = EditSectionForm(obj=section)
    if form.validate_on_submit():
        section.name = form.name.data
        db.session.commit()
        flash("Section updated successfully!", "success")
        return redirect(request.referrer or url_for("admin.manage_courses"))
    return render_template("admin/edit_section.html", form=form)

@admin.route("/edit_label/<int:label_id>", methods=["GET", "POST"])
@login_required
def edit_label(label_id):
    label = Label.query.get_or_404(label_id)
    form = EditLabelForm(obj=label)

    if form.validate_on_submit():
        label.label = form.label.data
        label.name = form.name.data
        db.session.commit()
        flash("Label updated successfully!", "success")
        return redirect(url_for("admin.manage_courses"))

    return render_template("admin/edit_label.html", form=form, label=label)

@admin.route('/edit_module_section/<int:item_id>', methods=['GET', 'POST'])
@login_required
def edit_module_section(item_id):
    if not (current_user.is_trainer or current_user.is_admin or current_user.is_training_manager):
        abort(403)
    
    item = Task.query.get_or_404(item_id)
    if request.method == 'POST':
        new_label = request.form.get("label")
        new_title = request.form.get("title")
        item.label = new_label
        item.title = new_title
        db.session.commit()
        flash("Module/Section name updated.", "success")
        return redirect(url_for('admin.manage_courses'))

    return render_template("admin/edit_module_section.html", item=item)

@admin.route("/rename_label", methods=["POST"])
@login_required
def rename_label():
    if not (current_user.is_admin or current_user.is_trainer or current_user.is_training_manager):
        abort(403)

    label_id = request.form.get("label_id")
    new_title = request.form.get("new_name")
    label_type = request.form.get("label_type")

    task = Task.query.get_or_404(label_id)

    if label_type not in ["module", "section"]:
        flash("Invalid label type", "danger")
        return redirect(url_for("admin.manage_courses"))

    task.title = new_title
    db.session.commit()
    flash(f"{label_type.capitalize()} renamed successfully!", "success")

    return redirect(url_for("admin.edit_course", course_id=task.course_id))

@admin.route("/delete_task/<int:task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    # Delete submissions linked to this task
    Submission.query.filter_by(task_id=task.id).delete()
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully.", "success")
    return redirect(url_for("admin.edit_course", course_id=task.course_id))

@admin.route("/delete_section/<int:course_id>/<string:section_label>", methods=["POST"])
@login_required
def delete_section(course_id, section_label):
    # Get all tasks under this section (including the section header itself)
    tasks_to_delete = Task.query.filter(
        Task.course_id == course_id,
        Task.label.startswith(section_label)
    ).all()

    for task in tasks_to_delete:
        Submission.query.filter_by(task_id=task.id).delete()
        db.session.delete(task)

    db.session.commit()
    flash("Section and all associated tasks deleted.", "success")
    return redirect(url_for("admin.edit_course", course_id=course_id))

@admin.route("/delete_module/<int:course_id>/<string:module_label>", methods=["POST"])
@login_required
def delete_module(course_id, module_label):
    # Get all tasks under this module (including section headers and tasks)
    tasks_to_delete = Task.query.filter(
        Task.course_id == course_id,
        Task.label.startswith(module_label)
    ).all()

    for task in tasks_to_delete:
        Submission.query.filter_by(task_id=task.id).delete()
        db.session.delete(task)

    db.session.commit()
    flash("Module and all associated sections and tasks deleted.", "success")
    return redirect(url_for("admin.edit_course", course_id=course_id))

@admin.route('/trainer/user_tasks', methods=['GET', 'POST'])
@login_required
def trainer_user_tasks():
    if not (current_user.is_trainer or current_user.is_admin or current_user.is_training_manager):
        abort(403)

    #users = User.query.order_by(User.last_name).all()
    users = sorted(
        User.query.all(),
        key=lambda u: (str(u.name).split()[1] if len(str(u.name).split()) > 1 else "")
    )
    
    return render_template("admin/trainer_user_selector.html", users=users)

@admin.route("/trainer/user_tasks/<int:user_id>")
@login_required
def trainer_user_task_view(user_id):
    if not (current_user.is_admin or current_user.is_training_manager or current_user.is_trainer):
        abort(403)

    user = User.query.get_or_404(user_id)

    # 🚨 NEW — Apply scoping if Training Manager
    if current_user.is_training_manager and not current_user.is_admin:
        if current_user.platoon_id and user.platoon_id != current_user.platoon_id:
            abort(403)
        if current_user.mission_element_id and user.mission_element_id != current_user.mission_element_id:
            abort(403)
        if current_user.team_id and user.team_id != current_user.team_id:
            abort(403)

    # Existing logic → no changes needed below this
    enrollments = CourseEnrollment.query.filter_by(user_id=user.id).all()
    tasks = Task.query.all()
    completed_assignments = TaskAssignment.query.filter_by(user_id=user.id, status="completed").all()
    completed_task_ids = [a.task_id for a in completed_assignments]

    submissions = Submission.query.filter_by(user_id=user.id).all()

    # Build grouped_tasks for template (existing logic unchanged)
    grouped_tasks = build_grouped_tasks(tasks, enrollments)

    return render_template(
        "admin/user_task_overview.html",
        user=user,
        grouped_tasks=grouped_tasks,
        completed_task_ids=completed_task_ids,
        submissions=submissions
    )

@admin.route("/admin/trainer/mark_task_toggle/<int:user_id>/<int:task_id>", methods=["POST"])
@login_required
def toggle_task_completion(user_id, task_id):
    if not (current_user.is_admin or current_user.is_trainer or current_user.is_training_manager):
        abort(403)

    action = request.form.get("action")
    submission = Submission.query.filter_by(user_id=user_id, task_id=task_id).first()

    if action == "complete":
        if not submission:
            submission = Submission(user_id=user_id, task_id=task_id, status="completed")
            db.session.add(submission)
            assignment = TaskAssignment.query.filter_by(user_id=user_id, task_id=task_id).first()
            if not assignment:
                assignment = TaskAssignment(user_id=user_id, task_id=task_id, status="completed")
                db.session.add(assignment)
            else:
                assignment.status = "completed"
    elif action == "incomplete":
        if submission:
            db.session.delete(submission)

    db.session.commit()
    flash("Task updated successfully.", "success")
    return redirect(url_for("admin.trainer_user_task_view", user_id=user_id))

@admin.route("/trainer/delete_submission/<int:submission_id>", methods=["POST"])
@login_required
def trainer_delete_submission(submission_id):
    UPLOAD_FOLDER = "/mnt/data/uploads"  # local dev only

    if not current_user.is_trainer and not current_user.is_admin:
        flash("⚠️ You do not have permission to delete submissions.", "danger")
        return redirect(url_for("main.dashboard"))

    submission = Submission.query.get_or_404(submission_id)

    # 🔄 Delete uploaded file if it exists
    if submission.uploaded_file:
        folder_path = os.path.join(UPLOAD_FOLDER, str(submission.user_id), str(submission.task_id))
        file_path = os.path.join(folder_path, submission.uploaded_file)
        if os.path.exists(file_path):
            os.remove(file_path)

    # 🔄 Delete associated trainer review if it exists
    review = TrainerReview.query.filter_by(submission_id=submission.id).first()
    if review:
        db.session.delete(review)

    # Remove any task completion assignment
    assignment = TaskAssignment.query.filter_by(user_id=submission.user_id, task_id=submission.task_id).first()
    if assignment:
        db.session.delete(assignment)

    db.session.delete(submission)
    db.session.commit()

    flash("✅ Submission, file, and review deleted successfully.", "success")
    return redirect(request.referrer or url_for("admin.trainer_dashboard"))

@admin.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        flash("❌ You do not have permission to delete users.", "danger")
        return redirect(url_for('admin.dashboard'))

    user = User.query.get_or_404(user_id)

    # Optional: Prevent deleting self
    if user.id == current_user.id:
        flash("⚠️ You cannot delete your own account from this panel.", "warning")
        return redirect(url_for('admin.manage_users'))

    db.session.delete(user)
    db.session.commit()
    flash(f"🗑️ User {user.name} deleted.", "success")
    return redirect(url_for('admin.manage_users'))

@admin.route("/admin/edit_user/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit_user_assignments(user_id):
    if not current_user.is_admin:
        abort(403)

    user = User.query.get_or_404(user_id)
    platoons = Platoon.query.all()
    mission_elements = MissionElement.query.all()
    teams = Team.query.all()

    if request.method == "POST":
        # Update hierarchy
        user.platoon_id = request.form.get("platoon_id") or None
        user.mission_element_id = request.form.get("mission_element_id") or None
        user.team_id = request.form.get("team_id") or None

        # ✅ Update roles!
        user.is_trainer = "is_trainer" in request.form
        user.is_admin = "is_admin" in request.form
        user.is_training_manager = "is_training_manager" in request.form

        db.session.commit()
        flash("✅ User assignment and roles updated.", "success")
        return redirect(url_for("admin.manage_users"))

    return render_template(
        "admin/edit_user.html",
        user=user,
        platoons=platoons,
        mission_elements=mission_elements,
        teams=teams
    )

# ----------------------------
# MANAGE PLATOONS
# ----------------------------
@admin.route("/admin/manage_platoons")
@login_required
def manage_platoons():
    if not current_user.is_admin:
        abort(403)
    platoons = Platoon.query.all()
    return render_template("admin/manage_platoons.html", platoons=platoons)

@admin.route("/admin/create_platoon", methods=["POST"])
@login_required
def create_platoon():
    if not current_user.is_admin:
        abort(403)
    name = request.form.get("name")
    if name:
        db.session.add(Platoon(name=name))
        db.session.commit()
        flash("✅ Platoon created!", "success")
    return redirect(url_for("admin.manage_platoons"))

@admin.route("/admin/delete_platoon/<int:platoon_id>", methods=["POST"])
@login_required
def delete_platoon(platoon_id):
    if not current_user.is_admin:
        abort(403)
    platoon = Platoon.query.get_or_404(platoon_id)
    db.session.delete(platoon)
    db.session.commit()
    flash("✅ Platoon deleted!", "success")
    return redirect(url_for("admin.manage_platoons"))

# ----------------------------
# MANAGE MISSION ELEMENTS
# ----------------------------
@admin.route("/admin/manage_mission_elements")
@login_required
def manage_mission_elements():
    if not current_user.is_admin:
        abort(403)
    mission_elements = MissionElement.query.all()
    return render_template("admin/manage_mission_elements.html", mission_elements=mission_elements)

@admin.route("/admin/create_mission_element", methods=["POST"])
@login_required
def create_mission_element():
    if not current_user.is_admin:
        abort(403)
    name = request.form.get("name")
    if name:
        db.session.add(MissionElement(name=name))
        db.session.commit()
        flash("✅ Mission Element created!", "success")
    return redirect(url_for("admin.manage_mission_elements"))

@admin.route("/admin/delete_mission_element/<int:mission_element_id>", methods=["POST"])
@login_required
def delete_mission_element(mission_element_id):
    if not current_user.is_admin:
        abort(403)
    mission_element = MissionElement.query.get_or_404(mission_element_id)
    db.session.delete(mission_element)
    db.session.commit()
    flash("✅ Mission Element deleted!", "success")
    return redirect(url_for("admin.manage_mission_elements"))

# ----------------------------
# MANAGE TEAMS
# ----------------------------
@admin.route("/admin/manage_teams")
@login_required
def manage_teams():
    if not current_user.is_admin:
        abort(403)
    teams = Team.query.all()
    return render_template("admin/manage_teams.html", teams=teams)

@admin.route("/admin/create_team", methods=["POST"])
@login_required
def create_team():
    if not current_user.is_admin:
        abort(403)
    name = request.form.get("name")
    if name:
        db.session.add(Team(name=name))
        db.session.commit()
        flash("✅ Team created!", "success")
    return redirect(url_for("admin.manage_teams"))

@admin.route("/admin/delete_team/<int:team_id>", methods=["POST"])
@login_required
def delete_team(team_id):
    if not current_user.is_admin:
        abort(403)
    team = Team.query.get_or_404(team_id)
    db.session.delete(team)
    db.session.commit()
    flash("✅ Team deleted!", "success")
    return redirect(url_for("admin.manage_teams"))

@admin.route("/admin/manage_units", methods=["GET", "POST"])
@login_required
def manage_units():
    if not current_user.is_admin:
        abort(403)

    platoons = Platoon.query.order_by(Platoon.name).all()
    mission_elements = MissionElement.query.order_by(MissionElement.name).all()
    teams = Team.query.order_by(Team.name).all()

    if request.method == "POST":
        entity_type = request.form.get("entity_type")
        name = request.form.get("name").strip()

        if entity_type == "platoon":
            db.session.add(Platoon(name=name))
            db.session.commit()
            flash("✅ Platoon created.", "success")

        elif entity_type == "mission_element":
            platoon_id = request.form.get("platoon_id")
            if not platoon_id:
                flash("❌ Please select a Platoon for the Mission Element.", "danger")
                return redirect(url_for("admin.manage_units"))

            db.session.add(MissionElement(name=name, platoon_id=int(platoon_id)))
            db.session.commit()
            flash("✅ Mission Element created.", "success")

        elif entity_type == "team":
            mission_element_id = request.form.get("mission_element_id")
            if not mission_element_id:
                flash("❌ Please select a Mission Element for the Team.", "danger")
                return redirect(url_for("admin.manage_units"))

            db.session.add(Team(name=name, mission_element_id=int(mission_element_id)))
            db.session.commit()
            flash("✅ Team created.", "success")

        return redirect(url_for("admin.manage_units"))

    return render_template(
        "admin/manage_units.html",
        platoons=platoons,
        mission_elements=mission_elements,
        teams=teams
    )

@admin.route("/admin/delete_unit/<entity_type>/<int:entity_id>", methods=["POST"])
@login_required
def delete_unit(entity_type, entity_id):
    if not current_user.is_admin:
        abort(403)

    if entity_type == "platoon":
        unit = Platoon.query.get_or_404(entity_id)
    elif entity_type == "mission_element":
        unit = MissionElement.query.get_or_404(entity_id)
    elif entity_type == "team":
        unit = Team.query.get_or_404(entity_id)
    else:
        flash("❌ Invalid entity type.", "danger")
        return redirect(url_for("admin.manage_units"))

    db.session.delete(unit)
    db.session.commit()
    flash(f"✅ {entity_type.replace('_', ' ').title()} deleted.", "success")
    return redirect(url_for("admin.manage_units"))


