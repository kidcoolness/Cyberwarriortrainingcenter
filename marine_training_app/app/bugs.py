from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import BugReport, db

bugs = Blueprint('bugs', __name__)

# USER: Submit a Bug
@bugs.route('/submit_bug', methods=['GET', 'POST'])
@login_required
def submit_bug():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if not title or not description:
            flash("❌ Title and Description are required.", "danger")
            return redirect(url_for('bugs.submit_bug'))

        new_bug = BugReport(
            user_id=current_user.id,
            title=title,
            description=description
        )
        db.session.add(new_bug)
        db.session.commit()

        flash("✅ Bug report submitted successfully.", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('bugs/submit_bug.html')

# ADMIN: View All Bugs
@bugs.route('/admin/bugs')
@login_required
def admin_bugs():
    if not current_user.is_admin and not current_user.is_trainer:
        flash("⚠️ Access denied.", "danger")
        return redirect(url_for('main.dashboard'))

    bugs = BugReport.query.order_by(BugReport.timestamp.desc()).all()
    return render_template('bugs/admin_bugs.html', bugs=bugs)

# ADMIN: Mark Bug Resolved
@bugs.route('/admin/resolve_bug/<int:bug_id>', methods=['POST'])
@login_required
def resolve_bug(bug_id):
    if not current_user.is_admin and not current_user.is_trainer:
        flash("⚠️ Access denied.", "danger")
        return redirect(url_for('main.dashboard'))

    bug = BugReport.query.get_or_404(bug_id)
    bug.status = 'resolved'
    db.session.commit()

    flash("✅ Bug marked as resolved.", "success")
    return redirect(url_for('bugs.admin_bugs'))

# PUBLIC: View Bug List (Open + Resolved)
@bugs.route('/bugs')
def public_bug_list():
    open_bugs = BugReport.query.filter_by(status='open').order_by(BugReport.timestamp.desc()).all()
    unresolved_bugs = BugReport.query.filter_by(status='unresolved').order_by(BugReport.timestamp.desc()).all()
    resolved_bugs = BugReport.query.filter_by(status='resolved').order_by(BugReport.timestamp.desc()).all()
    return render_template('bugs/public_bug_list.html', open_bugs=open_bugs, unresolved_bugs=unresolved_bugs, resolved_bugs=resolved_bugs)

@bugs.route('/admin/mark_unresolved/<int:bug_id>', methods=['POST'])
@login_required
def mark_unresolved(bug_id):
    if not current_user.is_admin and not current_user.is_trainer:
        flash("⚠️ Access denied.", "danger")
        return redirect(url_for('main.dashboard'))

    bug = BugReport.query.get_or_404(bug_id)
    bug.status = 'unresolved'
    db.session.commit()

    flash("⚠️ Bug marked as Unresolved.", "info")
    return redirect(url_for('bugs.admin_bugs'))

# ADMIN: Delete a Bug
@bugs.route('/admin/delete_bug/<int:bug_id>', methods=['POST'])
@login_required
def delete_bug(bug_id):
    if not current_user.is_admin:
        flash("⚠️ Only Admins can delete bugs.", "danger")
        return redirect(url_for('main.dashboard'))

    bug = BugReport.query.get_or_404(bug_id)
    db.session.delete(bug)
    db.session.commit()

    flash("🗑️ Bug deleted successfully.", "success")
    return redirect(url_for('bugs.admin_bugs'))
