
Marine Training Portal – Continuation Handoff Document

Project Overview
----------------
The Marine Training Portal is a Flask-based web application that serves as a structured training platform for Marines. It allows Trainers and Admins to enroll users in modular cyber training courses and track individual and unit progress.

Current Functionality
---------------------
Roles
- All users start as basic students by default.
- Admins or Training Managers can assign additional roles:
  - Admin — full access to manage users, roles, courses, and the backend.
  - Trainer — can enroll users in courses and track progress.
  - Marine — standard user who completes assigned tasks.

Authentication & Access
- Uses Flask-Login for user sessions.
- Flask-WTF for form handling.
- All roles are checked before rendering pages or submitting data.

Course & Task Structure
- Courses are made from hierarchically organized tasks, pulled from USMC JQR documents.
- Tasks are structured as:
  - Modules (e.g., 1.0)
  - Sections (e.g., 1.1)
  - Tasks (e.g., 1.1.1) — only these are interactable.

Courses Implemented
- Host Basic
- Network Basic
- Host Senior
- Network Senior

Course Pages
- Rendered with:
  - Bold section headers
  - Clickable tasks
  - ✅/🔲 based on completion
- Each course displays percentage progress and auto-updates when tasks are completed.

Admin Panel
- Create, edit, and delete:
  - Courses
  - Modules (headers)
  - Sections (sub-headers)
  - Tasks
- Tasks can be:
  - Auto-Graded (with answer)
  - Trainer-Graded (with submission + feedback)
  - API-Graded (e.g., TryHackMe integration coming soon)

Trainer Panel
- Can:
  - Enroll Marines into courses
  - View active enrollments and progress
  - Disenroll users
- UI displays real-time course status.

Marine Dashboard
- Displays:
  - Assigned courses
  - Progress per course
  - Completed courses

User Profiles
- Profile includes:
  - Name, email, and role(s)
  - Completed courses
  - Uploadable profile picture
  - Placeholder for ranks, accolades, and leaderboard integration

In-Progress / Recently Completed
--------------------------------
- Hierarchical task structure built into courses
- Course and Task page refactor
- Tasks now organized under headers, with clean display
- Functional training panel and dashboards for each role
- Forms to create Modules, Sections, and Tasks added to edit_course.html
- Profiles created
- Admin course builder interface online

TODO List
---------
High Priority
1. Fix/Edit Hierarchy Nesting Logic
2. Edit & Reorder Hierarchy
3. Unit-Level Tracking System

Medium Priority
4. Add error handling if course or task ID does not exist
5. Refactor flash messages for all CRUD events
6. Add download/upload logging support to tasks
7. Add CyberDefender integration (API-graded tasks)
8. Add TryHackMe integration (task linking and score checking)
9. Leaderboard feature – rank by task/course completions

Low Priority / Future
10. Add streak tracking (days with activity)
11. Add challenge/task search system
12. Gamification (XP, medals, flags)
13. Unit-level reports exportable as CSV or printable PDF

File Structure
--------------
marine-training-app/
|
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── admin.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── course.html
│   │   ├── task.html
│   │   ├── admin/
│   │       ├── dashboard.html
│   │       ├── create_course.html
│   │       ├── edit_course.html
│   │       ├── create_task.html
│   │       ├── edit_task.html
│   └── static/
|
├── scripts/
│   ├── import_tasks_to_db.py
|
├── instance/
│   └── marine_training.db
|
├── migrations/
├── run.py
└── README.txt

Tips for Continuation
---------------------
- All forms use Flask-WTF. If a form error occurs, update both forms.py and the route.
- User roles are stored as booleans: is_admin, is_trainer.
- Task hierarchy uses label (e.g., 1.1.1) and is_section_header.
- Course progress is recalculated each time a task is marked complete.
