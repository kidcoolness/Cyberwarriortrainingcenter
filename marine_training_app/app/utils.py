# utils.py
import re
from .models import TaskAssignment, CourseTask
import os, json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))


def calculate_progress(user_id, course_id):
    course_tasks = CourseTask.query.filter_by(course_id=course_id).all()
    task_ids = [ct.task_id for ct in course_tasks if not ct.task.is_section_header]

    total_tasks = len(task_ids)
    completed_tasks = TaskAssignment.query.filter_by(user_id=user_id, status="completed") \
                                          .filter(TaskAssignment.task_id.in_(task_ids)).count()

    progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    return round(progress, 2), total_tasks, completed_tasks

def natural_key(string_):
    return [int(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', string_)]

def natural_sort_key(label):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', label)]

from flask_mail import Message
  # update the import to your actual app structure

def send_reset_email(user, token):
    from marine_training_app.app import mail
    reset_url = url_for('main.reset_token', token=token, _external=True)
    msg = Message(
                subject="Password Reset Request",
                recipients=[user.email],
                body=f'''Hi {user.name},

                To reset your password, click the link below:

                {reset_url}

                If you did not request a password reset, please ignore this email.

                Semper Fi,
                Your Marine Training Portal Team
                '''
            )
    mail.send(msg)

def grade_with_ai(question, expected_answer, student_answer):
    prompt = f"""
    Question: {question}
    Expected concepts: {expected_answer}
    Student answer: {student_answer}

    Determine if the student's answer demonstrates the expected concepts.
    Respond ONLY in JSON like this:
    {{ "correct": true/false, "feedback": "short explanation" }}
    """
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",  # or "gpt-4-turbo"
        messages=[
            {"role": "system", "content": "You are an automated grading assistant. Reply only in JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0)
        raw = response.choices[0].message.content.strip()
        return json.loads(raw)
    except Exception as e:
        print(f"[AI Grading Error]: {e}")
        return {"correct": False, "feedback": "⚠️ AI grading failed. Please review manually."}