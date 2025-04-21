from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, User, Task, Course, CourseTask, CourseEnrollment
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional
from .forms import TaskForm, OrgAssignmentForm
import json
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
@admin.route("admin/manage_users")
@login_required
def manage_users():
    if not current_user.is_admin:  # ✅ Use is_admin instead of role
        flash("Access denied: Admins only.", "danger")
        return redirect(url_for("main.dashboard"))

    users = User.query.all()
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

    tasks = Task.query.filter_by(course_id=course_id).order_by(Task.label).all()

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

from .forms import TaskForm

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

@admin.route("/delete_task/<int:task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    if not current_user.is_admin:
        flash("Access denied: Admins only.", "danger")
        return redirect(url_for("main.dashboard"))

    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "success")
    return redirect(url_for("admin.edit_course", course_id=task.course.id))

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
