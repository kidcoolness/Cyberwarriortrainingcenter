from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Meme, db
import os
from werkzeug.utils import secure_filename
from datetime import datetime

memes = Blueprint('memes', __name__)

MEME_UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads', 'memes')  # Adjust if needed

# Meme Upload
@memes.route('/upload_meme', methods=['GET', 'POST'])
@login_required
def upload_meme():
    if request.method == 'POST':
        meme_file = request.files.get('meme')

        if not meme_file:
            flash("❌ No file uploaded.", "danger")
            return redirect(url_for('memes.upload_meme'))

        if meme_file.filename.split('.')[-1].lower() not in ['jpg', 'jpeg', 'png', 'gif']:
            flash("❌ Invalid file type. Only images allowed.", "danger")
            return redirect(url_for('memes.upload_meme'))

        filename = secure_filename(meme_file.filename)
        os.makedirs(MEME_UPLOAD_FOLDER, exist_ok=True)
        filepath = os.path.join(MEME_UPLOAD_FOLDER, filename)
        meme_file.save(filepath)

        new_meme = Meme(
            user_id=current_user.id,
            image_filename=filename,
            timestamp=datetime.utcnow()
        )
        db.session.add(new_meme)
        db.session.commit()

        flash("✅ Meme uploaded successfully!", "success")
        return redirect(url_for('memes.meme_list'))

    return render_template('memes/upload_meme.html')

# Meme Voting
@memes.route('/memes', methods=['GET', 'POST'])
@login_required
def meme_list():
    memes = Meme.query.order_by(Meme.timestamp.desc()).all()

    if request.method == 'POST':
        meme_id = request.form.get('meme_id')
        meme = Meme.query.get(meme_id)
        if meme:
            meme.votes += 1
            db.session.commit()
            flash("✅ Vote recorded!", "success")
        return redirect(url_for('memes.meme_list'))

    return render_template('memes/meme_list.html', memes=memes)

# ADMIN: Pick Meme Winner
@memes.route('/admin/meme_winner/<int:meme_id>', methods=['POST'])
@login_required
def award_meme_winner(meme_id):
    if not current_user.is_admin and not current_user.is_trainer:
        flash("⚠️ Access denied.", "danger")
        return redirect(url_for('main.dashboard'))

    meme = Meme.query.get_or_404(meme_id)
    user = meme.user

    if user:
        # Add "Meme Master" badge
        current_badges = user.badges.split(",") if user.badges else []
        if "Meme Master" not in current_badges:
            current_badges.append("Meme Master")
            user.badges = ",".join(current_badges)
            db.session.commit()
            flash(f"🏅 Meme Master badge awarded to {user.name}!", "success")
        else:
            flash(f"⚠️ {user.name} already has Meme Master badge.", "warning")
    else:
        flash("⚠️ No user associated with this meme.", "danger")

    return redirect(url_for('memes.meme_list'))
