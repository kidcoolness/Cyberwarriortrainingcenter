# utils.py
import re
from .models import TaskAssignment, CourseTask

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
