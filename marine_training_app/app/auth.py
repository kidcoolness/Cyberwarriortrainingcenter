from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import db, User
from .forms import LoginForm, RegistrationForm


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if not user or not check_password_hash(user.password_hash, form.password.data):
            flash("Invalid email or password.", "danger")
            return redirect(url_for("auth.login"))
        login_user(user)
        flash("Login successful!", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("auth/login.html", form=form)

@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("An account with this email already exists.", "danger")
            return redirect(url_for("auth.register"))

        # ✅ Create a new user as a Student by default
        new_user = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(password),
            is_student=True  # ✅ All users start as students
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! You can now log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))

@auth.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    if request.method == "POST":
        email = request.form.get("email").strip()
        user = User.query.filter_by(email=email).first()
        if user:
            token = serializer.dumps(user.email, salt='reset-password')
            if user:
                token = s.dumps(user.email, salt='password-reset')
                send_reset_email(user, token)
            reset_link = url_for('auth.reset_password', token=token, _external=True)
            # TODO: Replace this print with actual email sending
            print(f"[DEBUG] Password reset link: {reset_link}")
            flash("A password reset link has been sent to your email.", "info")
        else:
            flash("No user found with that email.", "danger")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password_request.html")

@auth.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    try:
        email = serializer.loads(token, salt='reset-password', max_age=3600)
    except Exception:
        flash("The password reset link is invalid or has expired.", "danger")
        return redirect(url_for("auth.reset_password_request"))

    user = User.query.filter_by(email=email).first_or_404()

    if request.method == "POST":
        new_password = request.form.get("password").strip()
        user.password_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')
        db.session.commit()
        flash("✅ Your password has been updated! You can now log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password.html", token=token)
