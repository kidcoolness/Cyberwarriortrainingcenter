from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .admin import admin
from .forms import ProfileUpdateForm, AnswerForm, MCQForm, TrainerAnswerForm
from .models import db, User, CourseEnrollment, CourseTask, TaskAssignment, Course, Task
from collections import defaultdict
import json
from sqlalchemy.orm import joinedload
from .utils import calculate_progress
import csv
from io import StringIO
from flask import make_response
from .models import Submission, TrainerReview

# Define a Blueprint
main = Blueprint("main", __name__)

def build_task_hierarchy(tasks):
    hierarchy = {}

    task_map = {task.label: task for task in tasks}

    for task in tasks:
        if task.label.endswith(".0"):
            # This is a module
            hierarchy[task.label] = {
                "title": task.title,
                "sections": {}
            }

    for task in tasks:
        if task.label.count(".") == 1:
            # This is a section
            module_label = task.parent_label
            if module_label in hierarchy:
                hierarchy[module_label]["sections"][task.label] = {
                    "title": task.title,
                    "tasks": []
                }

    for task in tasks:
        if task.label.count(".") == 2:
            # This is a task
            section_label = task.parent_label
            for module in hierarchy.values():
                if section_label in module["sections"]:
                    module["sections"][section_label]["tasks"].append(task)

    return hierarchy

@main.route("/")
@login_required
def index():
    if current_user.is_admin:
        return redirect(url_for("admin.dashboard"))  # ✅ Admins go to Admin Dashboard
    elif current_user.is_trainer:
        return redirect(url_for("main.trainer_dashboard"))  # ✅ Trainers go to Trainer Dashboard
    else:
        return redirect(url_for("main.dashboard"))  # ✅ Students go to Student Dashboard

@main.route("/tasks")
@login_required
def task_list():
    tasks = Task.query.all()
    return render_template("task.html", tasks=tasks)  

@main.route("/task/<int:task_id>", methods=["GET", "POST"])
@login_required
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    assignment = TaskAssignment.query.filter_by(user_id=current_user.id, task_id=task.id).first()
    result = None

    form = AnswerForm()
    mcq_form = MCQForm()

    # Load existing submission for trainer-graded tasks
    trainer_form = TrainerAnswerForm()
    existing_submission = None

    if task.grading_type == "trainer":
        existing_submission = Submission.query.filter_by(user_id=current_user.id, task_id=task.id).first()
        if existing_submission:
            trainer_form.answer.data = existing_submission.submission_text


    # MCQ: Set choices dynamically
    if task.grading_type == "mcq" and task.choices:
        try:
            mcq_form.answer.choices = [(c, c) for c in json.loads(task.choices)]
            print("✅ MCQ Choices Set:", mcq_form.answer.choices)
        except Exception as e:
            print("⚠️ Failed to load MCQ choices:", e)
            mcq_form.answer.choices = []

    # Trainer-graded: Check for existing submission
    existing_submission = None
    if task.grading_type == "trainer":
        existing_submission = Submission.query.filter_by(user_id=current_user.id, task_id=task.id).first()
        if existing_submission:
            trainer_form.answer.data = existing_submission.submission_text  # prefill

    # Form Handling
    if request.method == "POST":
        if task.grading_type == "auto" and form.validate_on_submit():
            user_answer = form.answer.data.strip()
            if task.correct_answer and user_answer.lower() == task.correct_answer.strip().lower():
                result = "correct"
                if not assignment:
                    assignment = TaskAssignment(user_id=current_user.id, task_id=task.id, status="completed")
                    db.session.add(assignment)
                else:
                    assignment.status = "completed"
                db.session.commit()
            else:
                result = "incorrect"

        elif task.grading_type == "mcq" and mcq_form.validate_on_submit():
            user_answer = mcq_form.answer.data.strip()
            if user_answer == task.correct_answer:
                result = "correct"
                if not assignment:
                    assignment = TaskAssignment(user_id=current_user.id, task_id=task.id, status="completed")
                    db.session.add(assignment)
                else:
                    assignment.status = "completed"
                db.session.commit()
            else:
                result = "incorrect"

        elif task.grading_type == "trainer" and trainer_form.validate_on_submit():
            if existing_submission:
                existing_submission.submission_text = trainer_form.answer.data
                existing_submission.status = 'pending'
            else:
                submission = Submission(
                    user_id=current_user.id,
                    task_id=task.id,
                    submission_text=trainer_form.answer.data,
                    status='pending'
                )
                db.session.add(submission)
            db.session.commit()
            flash("✅ Submission sent for trainer review.", "success")
            return redirect(url_for("main.course_page", course_id=task.course_id, _anchor=f"task-{task.id}"))

    return render_template(
        "partials/task_content.html",
        task=task,
        form=form,
        mcq_form=mcq_form,
        trainer_form=trainer_form,
        assignment=assignment,
        result=result
    )

# Submit a task
@main.route("/submit/<int:task_id>", methods=["POST"])
@login_required
def submit_task(task_id):
    submission_text = request.form.get("submission_text")
    new_submission = Submission(
        user_id=current_user.id,
        task_id=task_id,
        submission_text=submission_text,
        status="pending"
    )
    db.session.add(new_submission)
    db.session.commit()
    return redirect(url_for("main.dashboard"))

@main.route("/assign_task/<int:task_id>", methods=["POST"])
@login_required
def assign_task(task_id):
    if not (current_user.is_trainer or current_user.is_admin):  # Only trainers can assign tasks
        flash("Access denied: Trainers only.", "danger")
        return redirect(url_for("main.dashboard"))

    user_id = request.form["user_id"]
    existing_assignment = TaskAssignment.query.filter_by(user_id=user_id, task_id=task_id).first()

    if existing_assignment:
        flash("This Marine is already assigned to this task.", "warning")
    else:
        new_assignment = TaskAssignment(user_id=user_id, task_id=task_id)
        db.session.add(new_assignment)
        db.session.commit()
        flash("Task assigned successfully!", "success")

    return redirect(url_for("main.dashboard"))

@main.route("/complete_task/<int:task_id>", methods=["POST"])
@login_required
def complete_task(task_id):
    task_assignment = TaskAssignment.query.filter_by(user_id=current_user.id, task_id=task_id).first()

    if not task_assignment:
        flash("You have not been assigned this task.", "danger")
        return redirect(url_for("main.dashboard"))

    # ✅ Mark the task as completed
    task_assignment.status = "completed"
    db.session.commit()
    
    flash("Task marked as completed!", "success")
    return redirect(url_for("main.dashboard"))

@main.route("/dashboard")
@login_required
def dashboard():
    if current_user.is_admin:
        return redirect(url_for("admin.dashboard"))
    elif current_user.is_trainer:
        return redirect(url_for("main.trainer_dashboard"))

    enrollments = CourseEnrollment.query.filter_by(user_id=current_user.id).all()
    completed_courses = [e.course for e in enrollments if e.completed]
    active_courses = [e.course for e in enrollments if not e.completed]

    return render_template("dashboard.html", active_courses=active_courses, completed_courses=completed_courses)

@main.route("/enroll_marine/<int:user_id>/<int:course_id>", methods=["POST"])
@login_required
def enroll_marine(user_id, course_id):
    if not (current_user.is_trainer or current_user.is_admin):
        flash("Access denied: Trainers only.", "danger")
        return redirect(url_for("main.dashboard"))

    existing_enrollment = CourseEnrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    if existing_enrollment:
        flash("Marine is already enrolled in this course.", "warning")
    else:
        new_enrollment = CourseEnrollment(user_id=user_id, course_id=course_id)
        db.session.add(new_enrollment)
        db.session.commit()
        flash("Marine enrolled successfully!", "success")

    return redirect(url_for("main.dashboard"))

@main.route("/course/<int:course_id>")
@login_required
def course_page(course_id):
    course = Course.query.get_or_404(course_id)

    enrollment = CourseEnrollment.query.filter_by(user_id=current_user.id, course_id=course_id).first()
    if not enrollment:
        flash("You are not enrolled in this course.", "danger")
        return redirect(url_for("main.dashboard"))

    all_tasks = Task.query.filter_by(course_id=course_id).order_by(Task.label).all()

    completed_tasks = [
        t.task_id for t in TaskAssignment.query.filter_by(
            user_id=current_user.id, status="completed"
        ).join(Task, TaskAssignment.task_id == Task.id)
        .filter(Task.course_id == course_id).all()
    ]

    total_tasks = len([t for t in all_tasks if not t.is_section_header])
    completed_count = len(completed_tasks)
    progress = (completed_count / total_tasks * 100) if total_tasks > 0 else 0

    enrollment.progress = round(progress, 1)
    if total_tasks > 0 and completed_count == total_tasks:
        enrollment.completed = True
    db.session.commit()

    task_hierarchy = build_task_hierarchy(all_tasks)

    # 👇 Handle partial reloads (AJAX)
    if request.args.get("partial") == "1":
        return render_template("partials/task_sidebar.html", task_hierarchy=task_hierarchy, completed_tasks=completed_tasks)

    return render_template(
        "course.html",
        course=course,
        task_hierarchy=task_hierarchy,
        completed_tasks=completed_tasks,
        progress=enrollment.progress
    )

@main.route("/trainer")
@login_required
def trainer_dashboard():
    if not (current_user.is_trainer or current_user.is_admin):
        flash("Access denied: Trainers only.", "danger")
        return redirect(url_for("main.dashboard"))
    return render_template("trainer_dashboard.html")

@main.route("/training_panel")
@login_required
def training_panel():
    if not (current_user.is_trainer or current_user.is_admin):  # ✅ Allow Admins and Trainers
        flash("Access denied: Trainers and Admins only.", "danger")
        return redirect(url_for("main.dashboard"))

    marines = User.query.filter((User.is_student == True) | (User.is_trainer == True)).all()  # ✅ Include Trainers
    courses = Course.query.all()
    enrollments = db.session.query(CourseEnrollment, User, Course).join(User, CourseEnrollment.user_id == User.id).join(Course, CourseEnrollment.course_id == Course.id).all()

    return render_template("training_panel.html", marines=marines, courses=courses, enrollments=enrollments)

@main.route("/enroll_marines", methods=["POST"])
@login_required
def enroll_marines():
    if not (current_user.is_trainer or current_user.is_admin):
        flash("Access denied: Trainers only.", "danger")
        return redirect(url_for("main.dashboard"))

    user_ids = request.form.getlist("user_id")  # ✅ list of user IDs to enroll
    course_id = request.form.get("course_id")   # ✅ ID of course to enroll in

    course_tasks = CourseTask.query.filter_by(course_id=course_id).all()

    enrolled_marine_names = []
    completed_marine_names = []

    for user_id in user_ids:
        existing_enrollment = CourseEnrollment.query.filter_by(user_id=user_id, course_id=course_id).first()

        if existing_enrollment:
            user = User.query.get(user_id)
            if existing_enrollment.completed:
                completed_marine_names.append(user.name)
            else:
                enrolled_marine_names.append(user.name)
            continue

        # ✅ Create enrollment
        new_enrollment = CourseEnrollment(user_id=user_id, course_id=course_id)
        db.session.add(new_enrollment)

        # ✅ Assign tasks
        for course_task in course_tasks:
            task_assignment = TaskAssignment(user_id=user_id, task_id=course_task.task_id, status="incomplete")
            db.session.add(task_assignment)

    db.session.commit()

    if enrolled_marine_names:
        flash(f"Already enrolled: {', '.join(enrolled_marine_names)}", "warning")
    if completed_marine_names:
        flash(f"Already completed: {', '.join(completed_marine_names)}", "danger")
    if not enrolled_marine_names and not completed_marine_names:
        flash("✅ Marines enrolled and tasks assigned successfully!", "success")

    return redirect(url_for("main.training_panel"))

@main.route("/mycourses")
@login_required
def my_courses():
    # Get all course enrollments for this Marine
    enrollments = CourseEnrollment.query.options(joinedload(CourseEnrollment.course)).filter_by(user_id=current_user.id).all()
    
    # Get all enrolled courses
    course_ids = [e.course_id for e in enrollments]
    courses = Course.query.filter(Course.id.in_(course_ids)).all()

    # 🔍 DEBUG
    print("Current user:", current_user.id)
    print("Enrollments:", enrollments)

    # ✅ Get real tasks for each course (exclude section headers)
    course_tasks = {
        course.id: Task.query.filter_by(course_id=course.id, is_section_header=False)
                             .order_by(Task.label).all()
        for course in courses
    }

    return render_template("my_courses.html", enrollments=enrollments)

@main.route("/disenroll_marine/<int:user_id>/<int:course_id>", methods=["POST"])
@login_required
def disenroll_marine(user_id, course_id):
    if not (current_user.is_trainer or current_user.is_admin):
        flash("Access denied: Trainers only.", "danger")
        return redirect(url_for("main.dashboard"))

    enrollment = CourseEnrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    if enrollment:
        # ✅ Delete related task assignments
        course_tasks = CourseTask.query.filter_by(course_id=course_id).all()
        for course_task in course_tasks:
            task_assignment = TaskAssignment.query.filter_by(user_id=user_id, task_id=course_task.task_id).first()
            if task_assignment:
                db.session.delete(task_assignment)

        db.session.delete(enrollment)
        db.session.commit()
        flash("Marine has been disenrolled from the course.", "success")
    else:
        flash("Marine is not enrolled in this course.", "warning")

    return redirect(url_for("main.training_panel"))

@main.route("/submit_answer/<int:task_id>", methods=["POST"])
@login_required
def submit_answer(task_id):
    task = Task.query.get_or_404(task_id)

    # ✅ Ensure the task is auto-graded
    if task.grading_type != "auto":
        flash("This task is not auto-graded.", "danger")
        return redirect(url_for("main.task_detail", task_id=task_id))

    submitted_answer = request.form["submitted_answer"].strip().lower()
    correct_answer = task.correct_answer.strip().lower() if task.correct_answer else ""

    task_assignment = TaskAssignment.query.filter_by(user_id=current_user.id, task_id=task_id).first()
    if not task_assignment:
        flash("You have not been assigned this task.", "danger")
        return redirect(url_for("main.dashboard"))

    # ✅ Auto-Grading Logic
    if submitted_answer == correct_answer:
        task_assignment.status = "completed"
        db.session.commit()
        flash("✅ Correct! Task marked as completed.", "success")
    else:
        flash("❌ Incorrect answer. Try again.", "danger")

    return redirect(url_for("main.task_detail", task_id=task_id))

@main.route("/profile/<int:user_id>")
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    completed_courses = CourseEnrollment.query.filter_by(user_id=user.id, completed=True).all()
    return render_template("profile.html", user=user, completed_courses=completed_courses)

import os
from werkzeug.utils import secure_filename

@main.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = ProfileUpdateForm(obj=current_user)

    if form.validate_on_submit():
        current_user.position = form.position.data
        current_user.accolades = form.accolades.data

        if form.profile_picture.data:
            filename = secure_filename(form.profile_picture.data.filename)
            path = os.path.join("app/static/profile_pics", filename)
            form.profile_picture.data.save(path)
            current_user.profile_picture = filename

        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for("main.profile", user_id=current_user.id))

    return render_template("edit_profile.html", form=form)

@main.route("/leaderboard")
@login_required
def leaderboard():
    from app.models import User, CourseEnrollment  # ✅ Import here to break circular loop

    users = User.query.all()
    leaderboard_data = []
    for user in users:
        completed = CourseEnrollment.query.filter_by(user_id=user.id, completed=True).count()
        leaderboard_data.append((user, completed))
    leaderboard_data.sort(key=lambda item: item[1], reverse=True)
    return render_template("leaderboard.html", leaderboard=leaderboard_data)

@main.route("/review/<int:submission_id>", methods=["POST"])
@login_required
def review_submission(submission_id):
    if not (current_user.is_trainer or current_user.is_admin or current_user.is_training_manager):
        return "Unauthorized", 403

    submission = Submission.query.get_or_404(submission_id)
    approved = request.form.get("approved") == "true"
    feedback = request.form.get("feedback", "")

    submission.status = "approved" if approved else "rejected"
    submission.feedback = feedback

    # ✅ Mark task as complete if approved
    if approved:
        assignment = TaskAssignment.query.filter_by(user_id=submission.user_id, task_id=submission.task_id).first()
        if not assignment:
            assignment = TaskAssignment(user_id=submission.user_id, task_id=submission.task_id, status="completed")
            db.session.add(assignment)
        else:
            assignment.status = "completed"

    db.session.commit()
    flash("✅ Submission reviewed successfully.", "success")
    return redirect(url_for("main.review_submissions"))

@main.route("/export/performance")
@login_required
def export_performance():
    if not (current_user.is_admin or current_user.is_training_manager):
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))

    users = User.query.all()

    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(["Name", "Platoon", "Mission Element", "Team", "Completed Tasks", "Total Tasks", "Percent Complete"])

    for user in users:
        assignments = TaskAssignment.query.filter_by(user_id=user.id).all()
        total_tasks = len(assignments)
        completed_tasks = len([a for a in assignments if a.status == "completed"])
        percent = f"{(completed_tasks / total_tasks * 100):.1f}%" if total_tasks > 0 else "0%"

        writer.writerow([
            user.name,
            user.platoon or "Unassigned",
            user.mission_element or "Unassigned",
            user.team or "Unassigned",
            completed_tasks,
            total_tasks,
            percent
        ])

    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=performance_by_unit.csv"
    response.headers["Content-type"] = "text/csv"
    return response

@main.route("/review_submissions")
@login_required
def review_submissions():
    if not (current_user.is_trainer or current_user.is_admin or current_user.is_training_manager):
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))

    submissions = Submission.query.order_by(Submission.timestamp.desc()).all()
    return render_template("trainer/review_submissions.html", submissions=submissions)
