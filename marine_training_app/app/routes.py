from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .admin import admin
from .forms import EditProfileForm, AnswerForm, MCQForm, TrainerAnswerForm
from .models import db, User, CourseEnrollment, CourseTask, TaskAssignment, Course, Task
from collections import defaultdict
import json
from sqlalchemy.orm import joinedload
from .utils import calculate_progress, natural_key, grade_with_ai
import csv
from io import StringIO
from flask import make_response
from .models import Submission, TrainerReview
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os
from flask import current_app
from datetime import datetime
from flask import send_from_directory
# Define a Blueprint

main = Blueprint("main", __name__)
if os.environ.get("RENDER"):
    UPLOAD_FOLDER = "/mnt/data/uploads"
else:
    UPLOAD_FOLDER = "/mnt/data/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'log', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    trainer_form = TrainerAnswerForm()

    existing_submission = Submission.query.filter_by(user_id=current_user.id, task_id=task.id).first()
    if task.grading_type == "trainer" and existing_submission:
        trainer_form.answer.data = existing_submission.submission_text

    if task.grading_type == "mcq" and task.choices:
        try:
            mcq_form.answer.choices = [(c, c) for c in json.loads(task.choices)]
        except Exception:
            mcq_form.answer.choices = []

    if request.method == "POST":
        # -----------------------------
        # AUTO GRADED
        # -----------------------------
        if task.grading_type == "auto" and form.validate_on_submit():
            user_answer = form.answer.data.strip()
            if task.correct_answer and user_answer.lower() == task.correct_answer.strip().lower():
                result = "correct"
                if not assignment:
                    db.session.add(TaskAssignment(user_id=current_user.id, task_id=task.id, status="completed"))
                else:
                    assignment.status = "completed"
                db.session.commit()
            else:
                result = "incorrect"

        # -----------------------------
        # MCQ
        # -----------------------------
        elif task.grading_type == "mcq" and mcq_form.validate_on_submit():
            user_answer = mcq_form.answer.data.strip()
            if user_answer == task.correct_answer:
                result = "correct"
                if not assignment:
                    db.session.add(TaskAssignment(user_id=current_user.id, task_id=task.id, status="completed"))
                else:
                    assignment.status = "completed"
                db.session.commit()
            else:
                result = "incorrect"

        # -----------------------------
        # TRAINER-GRADED
        # -----------------------------
        elif task.grading_type == "trainer":
            answer_text = request.form.get("answer", "").strip()
            uploaded_file = request.files.get("file")
            filename = None

            if uploaded_file and uploaded_file.filename != "":
                from werkzeug.utils import secure_filename
                import os
                UPLOAD_FOLDER = os.path.join("/mnt/data/uploads", str(current_user.id), str(task.id))
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                filename = secure_filename(uploaded_file.filename)
                uploaded_file.save(os.path.join(UPLOAD_FOLDER, filename))

            if answer_text or filename:
                if existing_submission:
                    existing_submission.submission_text = answer_text
                    existing_submission.status = 'pending'
                    if filename:
                        existing_submission.uploaded_file = filename
                else:
                    submission = Submission(
                        user_id=current_user.id,
                        task_id=task.id,
                        submission_text=answer_text,
                        uploaded_file=filename,
                        status='pending'
                    )
                    db.session.add(submission)
                db.session.commit()
                flash("✅ Submission sent for trainer review.", "success")

        # -----------------------------
        # AI-GRADED
        # -----------------------------
        elif task.grading_type == "ai" and form.validate_on_submit():
            user_answer = form.answer.data.strip()
            ai_result = grade_with_ai(task.title, task.correct_answer or "", user_answer)

            if existing_submission:
                existing_submission.submission_text = user_answer
                existing_submission.status = 'completed' if ai_result.get("correct") else 'incomplete'
                existing_submission.feedback = ai_result.get("feedback", "")
                existing_submission.is_correct = ai_result.get("correct", False)
            else:
                submission = Submission(
                    user_id=current_user.id,
                    task_id=task.id,
                    submission_text=user_answer,
                    status='completed' if ai_result.get("correct") else 'incomplete',
                    feedback=ai_result.get("feedback", ""),
                    is_correct=ai_result.get("correct", False)
                )
                db.session.add(submission)

            if ai_result.get("correct"):
                if not assignment:
                    db.session.add(TaskAssignment(user_id=current_user.id, task_id=task.id, status="completed"))
                else:
                    assignment.status = "completed"

            db.session.commit()
            flash(
                f"🤖 AI Graded: {'✅ Correct' if ai_result.get('correct') else '❌ Incorrect'} – {ai_result.get('feedback','')}",
                "info"
            )
            return redirect(url_for('main.dashboard'))

    # Refresh submission after processing
    existing_submission = Submission.query.filter_by(user_id=current_user.id, task_id=task.id).first()
    # Pre-fill answer form for auto/AI
    if existing_submission and task.grading_type in ["auto", "ai"]:
        form.answer.data = existing_submission.submission_text
        
    # Handle AJAX partial requests
    if request.headers.get("X-Requested-With") == "XMLHttpRequest" or request.args.get("partial") == "1":
        return render_template(
            "partials/task_content.html",
            task=task,
            form=form,
            mcq_form=mcq_form,
            trainer_form=trainer_form,
            assignment=assignment,
            result=result,
            user_submission=existing_submission,
            inside_course=True
        )
    else:
        return render_template(
            "task_wrapper.html",
            task=task,
            form=form,
            mcq_form=mcq_form,
            trainer_form=trainer_form,
            assignment=assignment,
            result=result,
            user_submission=existing_submission
        )

# Submit a task
@main.route("/submit/<int:task_id>", methods=["POST"])
@login_required
def submit_task(task_id):
    #submission_text = request.form.get("submission_text")
    submission_text = request.form.get("answer")
    uploaded_file = request.files.get("file")

    # Check if the user already has a submission for this task
    submission = Submission.query.filter_by(user_id=current_user.id, task_id=task_id).first()

    filename = None
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        user_folder = os.path.join(UPLOAD_FOLDER, str(current_user.id), str(task_id))
        os.makedirs(user_folder, exist_ok=True)
        file_path = os.path.join(user_folder, filename)

        # Delete old uploaded file if it exists
        if submission and submission.uploaded_file:
            old_file_path = os.path.join(user_folder, submission.uploaded_file)
            if os.path.exists(old_file_path):
                os.remove(old_file_path)

        uploaded_file.save(file_path)
    elif uploaded_file:
        flash("❌ Invalid file type.", "danger")
        return redirect(url_for("main.task_detail", task_id=task_id))

    if submission:
        # Update existing submission
        submission.submission_text = submission_text
        submission.uploaded_file = filename or submission.uploaded_file  # Only update if a new file uploaded
        submission.status = "pending"
    else:
        # Create new submission
        submission = Submission(
            user_id=current_user.id,
            task_id=task_id,
            submission_text=submission_text,
            status="pending",
            uploaded_file=filename
        )
        db.session.add(submission)

    db.session.commit()

    flash("✅ Task submitted successfully!", "success")
    return redirect(url_for("main.task_detail", task_id=task_id))

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

    all_tasks = sorted(Task.query.filter_by(course_id=course_id).all(), key=lambda t: natural_key(t.label))

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
    enrollment.completed = total_tasks > 0 and completed_count == total_tasks
    db.session.commit()

    task_hierarchy = build_task_hierarchy(all_tasks)

    selected_task_id = request.args.get("task")
    selected_task_html = None
    if selected_task_id:
        try:
            selected_task_id = int(selected_task_id)
            task = Task.query.get(selected_task_id)
            if task and task.course_id == course.id:
                from flask import render_template_string
                selected_task_html = render_template(
                    "partials/task_content.html",
                    task=task,
                    form=AnswerForm(),
                    mcq_form=MCQForm(),
                    trainer_form=TrainerAnswerForm(),
                    assignment=TaskAssignment.query.filter_by(user_id=current_user.id, task_id=task.id).first(),
                    result=None,
                    user_submission=Submission.query.filter_by(user_id=current_user.id, task_id=task.id).first()
                )
        except ValueError:
            pass  # Invalid task_id format

    return render_template(
        "course.html",
        course=course,
        task_hierarchy=task_hierarchy,
        completed_tasks=completed_tasks,
        progress=enrollment.progress,
        selected_task_html=selected_task_html  # 👈 Send it to the template
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
    if not (current_user.is_admin or current_user.is_training_manager or current_user.is_trainer):
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))

    # Fetch marines to display in dropdown
    if current_user.is_admin:
        marines = User.query.filter_by(is_student=True).order_by(User.name).all()
    else:
        if not current_user.platoon_id:
            flash("⚠️ You must be assigned to a Platoon.", "danger")
            return redirect(url_for("main.dashboard"))
        marines = User.query.filter_by(
            is_student=True,
            platoon_id=current_user.platoon_id
        ).order_by(User.name).all()

    # Fetch courses
    courses = Course.query.order_by(Course.name).all()

    # Fetch enrollments for display
    if current_user.is_admin:
        enrollments = (
            db.session.query(CourseEnrollment, User, Course)
            .join(User, CourseEnrollment.user_id == User.id)
            .join(Course, CourseEnrollment.course_id == Course.id)
            .order_by(User.name)
            .all()
        )
    else:
        enrollments = (
            db.session.query(CourseEnrollment, User, Course)
            .join(User, CourseEnrollment.user_id == User.id)
            .join(Course, CourseEnrollment.course_id == Course.id)
            .filter(User.platoon_id == current_user.platoon_id)
            .order_by(User.name)
            .all()
        )

    return render_template(
        "training_panel.html",
        marines=marines,
        courses=courses,
        enrollments=enrollments
    )

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
    form = EditProfileForm(obj=user)
    return render_template("profile.html", user=user, completed_courses=completed_courses, form=form)

import os
from werkzeug.utils import secure_filename
from .forms import EditProfileForm

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(obj=current_user)

    if form.validate_on_submit():
        # Update email if changed
        if form.email.data and form.email.data != current_user.email:
            current_user.email = form.email.data

        # Handle password update
        if form.current_password.data and form.new_password.data:
            if check_password_hash(current_user.password_hash, form.current_password.data):
                current_user.password_hash = generate_password_hash(form.new_password.data)
            else:
                flash("❌ Incorrect current password.", "danger")
                return redirect(url_for('main.edit_profile'))

        # Update name and other fields
        current_user.name = form.name.data
        current_user.position = form.position.data
        current_user.accolades = form.accolades.data

        # Handle profile picture upload if provided
        if form.profile_picture.data and hasattr(form.profile_picture.data, 'read'):
            pic_data = form.profile_picture.data.read()
            filename = secure_filename(form.profile_picture.data.filename)
            filepath = os.path.join("marine_training_app", "app","static", "profile_pics", filename)

            with open(filepath, "wb") as f:
                f.write(pic_data)

            current_user.profile_picture = f"profile_pics/{filename}"

        db.session.commit()
        flash('✅ Profile updated successfully!', 'success')
        return redirect(url_for('main.edit_profile'))

    return render_template('edit_profile.html', form=form)

@main.route("/leaderboard")
@login_required
def leaderboard():
    from .models import User, CourseEnrollment  # ✅ Import here to break circular loop

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
    feedback = request.form.get("feedback", "")
    action = request.form.get("action")

    submission.feedback = feedback  # Always update feedback

    if action == "approve":
        submission.status = "approved"
        # Mark task complete
        assignment = TaskAssignment.query.filter_by(user_id=submission.user_id, task_id=submission.task_id).first()
        if not assignment:
            assignment = TaskAssignment(user_id=submission.user_id, task_id=submission.task_id, status="completed")
            db.session.add(assignment)
        else:
            assignment.status = "completed"

    elif action == "reject":
        submission.status = "rejected"

    # "update" means feedback only, so status stays the same

    db.session.commit()
    flash("✅ Submission review updated.", "success")
    return redirect(url_for("main.review_submissions"))

@main.route("/review_submissions")
@login_required
def review_submissions():
    if not (current_user.is_trainer or current_user.is_admin or current_user.is_training_manager):
        flash("Access denied.", "danger")
        return redirect(url_for("main.dashboard"))

    # Default: no platoon restriction for admin
    if current_user.is_admin:
        pending_submissions = Submission.query.filter_by(status='pending').order_by(Submission.timestamp.desc()).all()
        approved_submissions = Submission.query.filter_by(status='approved').order_by(Submission.timestamp.desc()).all()
        rejected_submissions = Submission.query.filter_by(status='rejected').order_by(Submission.timestamp.desc()).all()

    else:
        # Trainers & Training Managers - filter by platoon
        platoon_id = current_user.platoon_id
        if platoon_id is None:
            flash("⚠️ You must be assigned to a Platoon to review submissions.", "danger")
            return redirect(url_for("main.dashboard"))

        pending_submissions = (
            Submission.query
            .join(User, Submission.user_id == User.id)
            .filter(User.platoon_id == platoon_id, Submission.status == 'pending')
            .order_by(Submission.timestamp.desc())
            .all()
        )
        approved_submissions = (
            Submission.query
            .join(User, Submission.user_id == User.id)
            .filter(User.platoon_id == platoon_id, Submission.status == 'approved')
            .order_by(Submission.timestamp.desc())
            .all()
        )
        rejected_submissions = (
            Submission.query
            .join(User, Submission.user_id == User.id)
            .filter(User.platoon_id == platoon_id, Submission.status == 'rejected')
            .order_by(Submission.timestamp.desc())
            .all()
        )

    return render_template(
        "trainer/review_submissions.html",
        pending_submissions=pending_submissions,
        approved_submissions=approved_submissions,
        rejected_submissions=rejected_submissions
    )

UPLOAD_FOLDER = "/mnt/data/uploads"  # for local dev
@main.route('/uploads/<int:user_id>/<int:task_id>/<filename>')
@login_required
def download_submission(user_id, task_id, filename):
    folder_path = os.path.join(UPLOAD_FOLDER, str(user_id), str(task_id))
    file_path = os.path.join(folder_path, filename)

    if not os.path.exists(file_path):
        return f"❌ File not found: {file_path}", 404

    return send_from_directory(folder_path, filename, as_attachment=True)

@main.route("/delete_submission/<int:task_id>", methods=["POST"])
@login_required
def delete_submission(task_id):
    submission = Submission.query.filter_by(user_id=current_user.id, task_id=task_id).first()

    if submission:
        # Delete associated file if it exists
        if submission.uploaded_file:
            folder_path = os.path.join(UPLOAD_FOLDER, str(current_user.id), str(task_id))
            file_path = os.path.join(folder_path, submission.uploaded_file)
            if os.path.exists(file_path):
                os.remove(file_path)

        # Delete the submission itself
        db.session.delete(submission)
        db.session.commit()
        flash("✅ Submission and upload deleted.", "success")
    else:
        flash("⚠️ No submission found to delete.", "warning")

    return redirect(url_for("main.task_detail", task_id=task_id))

@main.route("/delete_upload/<int:task_id>", methods=["POST"])
@login_required
def delete_uploaded_file(task_id):
    submission = Submission.query.filter_by(user_id=current_user.id, task_id=task_id).first()

    if submission and submission.uploaded_file:
        # Remove the uploaded file
        folder_path = os.path.join(UPLOAD_FOLDER, str(current_user.id), str(task_id))
        file_path = os.path.join(folder_path, submission.uploaded_file)
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Clear the uploaded file field in the database
        submission.uploaded_file = None
        db.session.commit()

        flash("✅ Uploaded file deleted.", "success")
    else:
        flash("⚠️ No uploaded file found.", "warning")

    return redirect(url_for("main.task_detail", task_id=task_id))

@main.route("/export_performance")
@login_required
def export_performance():
    flash("🚧 Export Performance feature not implemented yet.", "warning")
    return redirect(url_for("main.dashboard"))

@main.route("/test_email")
@login_required
def test_email():
    from marine_training_app.app import mail  # adjust to your actual app structure
    from flask_mail import Message
    print("We made it Mom!")
    msg = Message(
        subject="🚨 Test Email from Marine Training Portal",
        recipients=[current_user.email],
        body="This is a test email. If you received it, your SMTP setup is working! – Semper Fi."
    )
    print(current_user.email)
    try:
        mail.send(msg)
        flash("✅ Test email sent successfully!", "success")
    except Exception as e:
        flash(f"❌ Failed to send test email: {e}", "danger")
    
    return redirect(url_for("main.dashboard"))