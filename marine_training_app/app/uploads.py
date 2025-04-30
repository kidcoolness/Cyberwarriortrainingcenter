from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Upload, Task, db
import os

uploads = Blueprint('uploads', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # adjust if needed

# USER view: My Uploads
@uploads.route('/my_uploads')
@login_required
def my_uploads():
    uploads = Upload.query.filter_by(user_id=current_user.id).all()
    return render_template('uploads/my_uploads.html', uploads=uploads)

# ADMIN/TRAINER view: All uploads
@uploads.route('/admin/uploads')
@login_required
def admin_uploads():
    if not current_user.is_trainer and not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for('main.dashboard'))

    uploads = Upload.query.all()
    return render_template('uploads/admin_uploads.html', uploads=uploads)

# Delete an upload
@uploads.route('/delete_upload/<int:upload_id>', methods=['POST'])
@login_required
def delete_upload(upload_id):
    upload = Upload.query.get_or_404(upload_id)

    if upload.user_id != current_user.id and not (current_user.is_trainer or current_user.is_admin):
        flash("Access denied.", "danger")
        return redirect(url_for('main.dashboard'))

    file_path = os.path.join(UPLOAD_FOLDER, str(upload.user_id), str(upload.task_id), upload.filename)
    if os.path.exists(file_path):
        os.remove(file_path)

    db.session.delete(upload)
    db.session.commit()

    flash("✅ Upload deleted successfully.", "success")
    return redirect(request.referrer or url_for('uploads.my_uploads'))
