import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Course, Task, CourseTask

app = create_app()
app.app_context().push()

# === Host Basic Tasks ===
course = Course.query.filter_by(name="Host Basic").first()
if course:
    task = Task(
        title="Task # | Task # | (U) Basic Host Analyst Knowledge | T&R ID | Trainee Initials | Trainer Initials | Date Qualified",
        description="Task # | Task # | (U) Basic Host Analyst Knowledge | T&R ID | Trainee Initials | Trainer Initials | Date Qualified",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be",
        description="Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability | Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability | Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability | Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability | Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability | Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability | Module 1.0. (U) This module covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="1.1 | 1.1 | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM &",
        description="1.1 | 1.1 | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="1.1.1 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM",
        description="1.1.1 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM) Company.  Training Resources & Technical References: CWP 3-33.4 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM) Company.  Training Resources & Technical References: CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="1.1.2 | Describe the roles and responsibilities for 3d Network Battalion.  Training Resources & Technical References: Jo",
        description="1.1.2 | Describe the roles and responsibilities for 3d Network Battalion.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the roles and responsibilities for 3d Network Battalion.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="1.1.3 | Describe the following mission types: DCO-IDM DODIN Operations Assess Harden Clear Hunt  Training Resources & Te",
        description="1.1.3 | Describe the following mission types: DCO-IDM DODIN Operations Assess Harden Clear Hunt  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the following mission types: DCO-IDM DODIN Operations Assess Harden Clear Hunt  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="1.1.4 | Explain the structure of a Mission Element and their roles. Team Lead Network Analyst Host Analyst Network Techn",
        description="1.1.4 | Explain the structure of a Mission Element and their roles. Team Lead Network Analyst Host Analyst Network Technician Intelligence Analyst  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain the structure of a Mission Element and their roles. Team Lead Network Analyst Host Analyst Network Technician Intelligence Analyst  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="1.1.5 | Describe relevant policies and procedures governing the DCO-IDM Company.  Training Resources & Technical Referen",
        description="1.1.5 | Describe relevant policies and procedures governing the DCO-IDM Company.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information | Describe relevant policies and procedures governing the DCO-IDM Company.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="1.1.6 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.  Training Resources & Te",
        description="1.1.6 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="1.1.7 | (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to",
        description="1.1.7 | (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to the mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information | (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to the mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="1.1.8 | Describe the Mission Element Lead responsibilities toward network owner interaction.  Training Resources & Techn",
        description="1.1.8 | Describe the Mission Element Lead responsibilities toward network owner interaction.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the Mission Element Lead responsibilities toward network owner interaction.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="1.1.9 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakehold",
        description="1.1.9 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeholders.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeholders.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="1.1.10 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrat",
        description="1.1.10 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrate data collection.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrate data collection.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="1.1.11 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.  Trainin",
        description="1.1.11 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="1.1.12 | Define Battle Rhythm and discuss why it is useful in preparing for a mission.  Training Resources & Technical R",
        description="1.1.12 | Define Battle Rhythm and discuss why it is useful in preparing for a mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 Joint Publication (JP) 2-01.3: Joint Intelligence Preparation of the Operational Environment (21 May 2014) | Define Battle Rhythm and discuss why it is useful in preparing for a mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 Joint Publication (JP) 2-01.3: Joint Intelligence Preparation of the Operational Environment (21 May 2014) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="1.1.13 | Identify and describe information resources at the company to use during mission planning.  Training Resources",
        description="1.1.13 | Identify and describe information resources at the company to use during mission planning.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Identify and describe information resources at the company to use during mission planning.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="1.1.14 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.  Training Resources & Technical R",
        description="1.1.14 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.  Training Resources & Technical References: NIST SP 800-30 r1 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.  Training Resources & Technical References: NIST SP 800-30 r1 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="1.1.15 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.  Tr",
        description="1.1.15 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="1.1.16 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.",
        description="1.1.16 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="1.1.17 | Briefing. Explain the importance of an in-brief and what should be included Explain the importance of an out-br",
        description="1.1.17 | Briefing. Explain the importance of an in-brief and what should be included Explain the importance of an out-brief and what should be included  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Briefing. Explain the importance of an in-brief and what should be included Explain the importance of an out-brief and what should be included  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="1.1.18 | Explain the timeline for creating and completing the final report.  Training Resources & Technical References:",
        description="1.1.18 | Explain the timeline for creating and completing the final report.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain the timeline for creating and completing the final report.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="1.1.19 | Describe incident response.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace",
        description="1.1.19 | Describe incident response.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe incident response.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="1.1.20 | (U) Describe the purpose of an Equipment Density List (EDL).  Training Resources & Technical References: Local",
        description="1.1.20 | (U) Describe the purpose of an Equipment Density List (EDL).  Training Resources & Technical References: Local SOP | (U) Describe the purpose of an Equipment Density List (EDL).  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="1.1.21 | Explain the purpose and components of a Risk Mitigation Plan.  Training Resources & Technical References: Joint",
        description="1.1.21 | Explain the purpose and components of a Risk Mitigation Plan.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain the purpose and components of a Risk Mitigation Plan.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="1.1.22 | Describe priority items or artifacts that may be found in an investigation.  Training Resources & Technical Ref",
        description="1.1.22 | Describe priority items or artifacts that may be found in an investigation.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe priority items or artifacts that may be found in an investigation.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="1.1.23 | Describe the process in determining the proper mitigations and courses of action for a mission owner.  Training",
        description="1.1.23 | Describe the process in determining the proper mitigations and courses of action for a mission owner.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the process in determining the proper mitigations and courses of action for a mission owner.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="1.1.24 | Discuss the scope and audience of a hot-wash.  Training Resources & Technical References: Joint Publication (JP",
        description="1.1.24 | Discuss the scope and audience of a hot-wash.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) | Discuss the scope and audience of a hot-wash.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="1.1.25 | Explain the importance of the after action review and what should be included.  Training Resources & Technical",
        description="1.1.25 | Explain the importance of the after action review and what should be included.  Training Resources & Technical References: Local SOP | Explain the importance of the after action review and what should be included.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="1.1.26 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.  Traini",
        description="1.1.26 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.  Training Resources & Technical References: CWP 3-33.4 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.  Training Resources & Technical References: CWP 3-33.4 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="1.1.27 | Explain the procedures and required documentation for transporting classified material and what procedure to fo",
        description="1.1.27 | Explain the procedures and required documentation for transporting classified material and what procedure to follow when passing through airport security.  Training Resources & Technical References: Local SOP | Explain the procedures and required documentation for transporting classified material and what procedure to follow when passing through airport security.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="1.1.28 | (U) Give an example of PKI and the known vulnerabilities in a customer network. | (U) Give an example of PKI an",
        description="1.1.28 | (U) Give an example of PKI and the known vulnerabilities in a customer network. | (U) Give an example of PKI and the known vulnerabilities in a customer network. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="1.1.29 | Explain network security implications if the following concepts are poorly implemented: Confidentiality Integri",
        description="1.1.29 | Explain network security implications if the following concepts are poorly implemented: Confidentiality Integrity Availability | Explain network security implications if the following concepts are poorly implemented: Confidentiality Integrity Availability |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="1.1.30 | (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain the differe",
        description="1.1.30 | (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain the difference between risk and threat as they relate to vulnerabilities. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="1.1.31 | Explain network security implications if the following concepts are poorly implemented: Non-repudiation Authent",
        description="1.1.31 | Explain network security implications if the following concepts are poorly implemented: Non-repudiation Authentication Access Control | Explain network security implications if the following concepts are poorly implemented: Non-repudiation Authentication Access Control |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="1.1.32 | Explain network security implications associated with implementing Security Technical Implementation Guides (ST",
        description="1.1.32 | Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) | Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="1.1.33 | (U) Explain the difference between attributable and non-attributable IP space. | (U) Explain the difference bet",
        description="1.1.33 | (U) Explain the difference between attributable and non-attributable IP space. | (U) Explain the difference between attributable and non-attributable IP space. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="1.1.34 | (U) Describe what constitutes a US Person.  Training Resources & Technical References: USSID SP0018 | (U) Descr",
        description="1.1.34 | (U) Describe what constitutes a US Person.  Training Resources & Technical References: USSID SP0018 | (U) Describe what constitutes a US Person.  Training Resources & Technical References: USSID SP0018 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="1.1.35 | Explain the following in regards to reports. Delivery Mission owner vulnerabilities Mitigation techniques  Trai",
        description="1.1.35 | Explain the following in regards to reports. Delivery Mission owner vulnerabilities Mitigation techniques  Training Resources & Technical References: Local SOP | Explain the following in regards to reports. Delivery Mission owner vulnerabilities Mitigation techniques  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="1.1.36 | Describe what each of the following DCO-IDM capabilities provide to supported commanders: Discovery and Counter",
        description="1.1.36 | Describe what each of the following DCO-IDM capabilities provide to supported commanders: Discovery and Counter Infiltration (D&CI) Threat Mitigation  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” | Describe what each of the following DCO-IDM capabilities provide to supported commanders: Discovery and Counter Infiltration (D&CI) Threat Mitigation  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="1.1.37 | As part of a mission, describe the systems that should be evaluated to gain situational awareness of the missio",
        description="1.1.37 | As part of a mission, describe the systems that should be evaluated to gain situational awareness of the mission partner’s network.  Training Resources & Technical References: Local SOP | As part of a mission, describe the systems that should be evaluated to gain situational awareness of the mission partner’s network.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="1.1.38 | Explain the following initial steps that are completed before an evaluation is started: Validate Scope Review N",
        description="1.1.38 | Explain the following initial steps that are completed before an evaluation is started: Validate Scope Review Network Design Identify Critical Systems Obtain IP address Scheme Build Exclusion List  Training Resources & Technical References: Local SOP | Explain the following initial steps that are completed before an evaluation is started: Validate Scope Review Network Design Identify Critical Systems Obtain IP address Scheme Build Exclusion List  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="1.1.39 | Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What i",
        description="1.1.39 | Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What is the ultimate goal of a collection plan?  Training Resources & Technical References: Local SOP | Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What is the ultimate goal of a collection plan?  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="1.1.40 | Explain how the below guidelines can be useful to the Network Analyst. Vendor Security guidance General best pr",
        description="1.1.40 | Explain how the below guidelines can be useful to the Network Analyst. Vendor Security guidance General best practices DISA Security Technical Implementation Common vulnerabilities and exposures. | Explain how the below guidelines can be useful to the Network Analyst. Vendor Security guidance General best practices DISA Security Technical Implementation Common vulnerabilities and exposures. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="1.1.41 | Explain what a SITREP is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions,",
        description="1.1.41 | Explain what a SITREP is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” | Explain what a SITREP is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="1.1.42 | Explain the following types of orders: FRAGORD OPORD WARNORD EXORD TASKORD  Training Resources & Technical Refe",
        description="1.1.42 | Explain the following types of orders: FRAGORD OPORD WARNORD EXORD TASKORD  Training Resources & Technical References: Joint Publication 3-12, “Cyberspace Operations” | Explain the following types of orders: FRAGORD OPORD WARNORD EXORD TASKORD  Training Resources & Technical References: Joint Publication 3-12, “Cyberspace Operations” |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="1.1.43 | Explain what “Mission Relevant Key Terrain” (MRT-C) is.  Training Resources & Technical References: CWP 3-33.4,",
        description="1.1.43 | Explain what “Mission Relevant Key Terrain” (MRT-C) is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” | Explain what “Mission Relevant Key Terrain” (MRT-C) is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="1.1.44 | (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |",
        description="1.1.44 | (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="1.1.45 | (U) Walkthrough the layout of MCEN in the INDOPACOM region.  Training Resources & Technical References: Introdu",
        description="1.1.45 | (U) Walkthrough the layout of MCEN in the INDOPACOM region.  Training Resources & Technical References: Introduction to MCEN Course | (U) Walkthrough the layout of MCEN in the INDOPACOM region.  Training Resources & Technical References: Introduction to MCEN Course |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="1.1.46 | 1.1.46 | (U) Explain the difference phases of the operational cycle.  Training Resources & Technical References",
        description="1.1.46 | 1.1.46 | (U) Explain the difference phases of the operational cycle.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="1.2 | 1.2 | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fun",
        description="1.2 | 1.2 | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="1.2.1 | 1.2.1 | Define dead disk.  Training Resources & Technical References: International Journal of Computer Science",
        description="1.2.1 | 1.2.1 | Define dead disk.  Training Resources & Technical References: International Journal of Computer Science and Information Technologies, Vol.8 (3), 2017 “Live Vs Dead Computer Forensic Image Acquistion” |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="1.2.2 | 1.2.2 | (U) Describe the types of volatile network information that can be obtained from a host for analysis.  T",
        description="1.2.2 | 1.2.2 | (U) Describe the types of volatile network information that can be obtained from a host for analysis.  Training Resources & Technical References: ScienceDirect, “Volatile Memory”, https://science/volatile-memory |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="1.2.3 | 1.2.3 | Memory Acquisition. Define Memory Acquisition Define how collected data is utilized Define risks and lim",
        description="1.2.3 | 1.2.3 | Memory Acquisition. Define Memory Acquisition Define how collected data is utilized Define risks and limitations associated with the live memory capture  Training Resources & Technical References: Sans Institute, White Papers “Techniques and Tools for Recovering and Analyzing Data from Volatile Memory” https:// white- papers/33049 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="1.2.4 | 1.2.4 | Memory Allocation. Define Memory allocation Identify how a legitimate program could use memory allocatio",
        description="1.2.4 | 1.2.4 | Memory Allocation. Define Memory allocation Identify how a legitimate program could use memory allocation for malicious activity Define Stack Define Heap  Training Resources & Technical References: Techopedia, “Memory Allocation – What Does Memory Allocation Mean?”  https:// oryAlloc.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="1.2.5 | 1.2.5 | Set User ID and Set Group ID. Explain how an adversary can take advantage of SETUID Explain how an adver",
        description="1.2.5 | 1.2.5 | Set User ID and Set Group ID. Explain how an adversary can take advantage of SETUID Explain how an adversary can take advantage of SETGID Define Bitmasking  Training Resources & Technical References: MITRE “Abuse Elevation Control Mechanism:Setuid and Setgid” https://attack.mitre.org/techniques/T1548/001/ Linuxconfig.org “How to use special permissions: the setgid and sticky bits” https://linuxconfig.org/how-to-use-special- permissions-the-setuid-setgid-and-sticky-bits |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="1.2.6 | 1.2.6 | Logging Describe where logging is stored on UNIX Describe where logging is stored on Windows  Training R",
        description="1.2.6 | 1.2.6 | Logging Describe where logging is stored on UNIX Describe where logging is stored on Windows  Training Resources & Technical References: Sun Java System Web Server 6.1 SP8 Administrator's Guide, Chapter 10 Using Log Files, Logging on the UNIX and WindowsPlatform,https://docs.oracle.com/cd/E19857- 01/8201639/bhale/index.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="1.2.7 | 1.2.7 | Describe the default logs that are kept on a Windows System.  Training Resources & Technical References:",
        description="1.2.7 | 1.2.7 | Describe the default logs that are kept on a Windows System.  Training Resources & Technical References: Solarwinds “Windows Logging Basics” https:// basics/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="1.2.8 | 1.2.8 | Describe Event Logs content and indicators within the logs that must be analyzed during a vulnerability",
        description="1.2.8 | 1.2.8 | Describe Event Logs content and indicators within the logs that must be analyzed during a vulnerability assessment.  Training Resources & Technical References: Microsoft.com “Event Logging” https://docs.microsoft.com/en- us/windows/win32/eventlog/event-logging |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="1.2.9 | 1.2.9 | Unix Profiles. Identify users log in times Identify where users are logging from Define how to identify",
        description="1.2.9 | 1.2.9 | Unix Profiles. Identify users log in times Identify where users are logging from Define how to identify user activities as normal or malicious  Training Resources & Technical References: NIXCraft Forum, Linux Display Date And Time Of Login by Mr. Vivek Gite,   How to Investigate User Logins – Intro to Incident Response Triage (Part 4) in 2019 by Dr. Brian Carter, https:// triage-part-4-user-logins-in-2019/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="1.2.10 | 1.2.10 | Active Directory Structures Explain the purpose of Active Directory Explain what type of services it p",
        description="1.2.10 | 1.2.10 | Active Directory Structures Explain the purpose of Active Directory Explain what type of services it provides for a network Explain the logical structure of Active directory  Training Resources & Technical References: Wikipedia, Active Directory by multiple authors, https://en.wikipedia.org/wiki/Active_Directory |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="1.2.11 | 1.2.11 | Registry Keys. Explain how registry values are used to maintain persistence Identify common registry v",
        description="1.2.11 | 1.2.11 | Registry Keys. Explain how registry values are used to maintain persistence Identify common registry values that are used to maintain persistence  Training Resources & Technical References: MITRE“Modify Registry”, https://attack.mitre.org/techniques/T1112/ InfosecInstitute.com “Common malware persistence mechanisms” by Security Ninja, https://resources.infosecinstitute.com/topic/common-malware- persistence-mechanisms/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="1.2.12 | 1.2.12 | DLL search order. Describe windows DLL search order Describe DLL search order hijacking  Training Reso",
        description="1.2.12 | 1.2.12 | DLL search order. Describe windows DLL search order Describe DLL search order hijacking  Training Resources & Technical References: Microsoft.com, “Dynamic-Link Library SearchOrder”,  MITRE “Hijack Execution Flow: DLL Search Order Hijacking”https://attack.mitre.org/techniques/T1574/001/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="1.2.13 | 1.2.13 | Rootkits. Describe indications of a rootkit for Windows Describe indications of a rootkit for UNIX  Tr",
        description="1.2.13 | 1.2.13 | Rootkits. Describe indications of a rootkit for Windows Describe indications of a rootkit for UNIX  Training Resources & Technical References: SANS Institute “Security Consensus Operational Readiness Evaluation (SCORE) Security Checklist”, https:// investigation-procedures.pdf |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="1.2.14 | 1.2.14 | Portable Executable. Define Portable Executable Identify how a malicious actor could obfuscate an exec",
        description="1.2.14 | 1.2.14 | Portable Executable. Define Portable Executable Identify how a malicious actor could obfuscate an executable  Training Resources & Technical References: Microsoft.com “PE Format”,   MITRE “Obfuscated Files or Information”, https://attack.mitre.org/techniques/T1027/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="1.2.15 | 1.2.15 | Describe the following encoding types. Base32 Base64 XOR Hex PunyCode ROT13  Training Resources & Tech",
        description="1.2.15 | 1.2.15 | Describe the following encoding types. Base32 Base64 XOR Hex PunyCode ROT13  Training Resources & Technical References: Wikipedia “Base32, Base64, XOR Cipher, Hexadecimal, Punycode, ROT13” by multiple authors,  https://en.wikipedia.org/wiki/Base64httphttps://en.wikipedia.or g/wiki/XOR_cipher, https://en.wikipedia.org/wiki/Hexadecimal https://en.wikipedia.org/wiki/Punycode https://en.wikipedia.org/wiki/ROT13 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="1.2.16 | 1.2.16 | Define exfiltration staging.  Training Resources & Technical References: MITRE “Data Staged: Local Dat",
        description="1.2.16 | 1.2.16 | Define exfiltration staging.  Training Resources & Technical References: MITRE “Data Staged: Local DataStaging,”https://attack.mitre.org/techniques/T1074/001/ MITRE “Data Staged: Remote Data Staging” ,https://attack.mitre.org/techniques/T1074/002/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="1.2.17 | 1.2.17 | Describe three methods to obfuscate or hide programs on compromised systems.  Training Resources & Tec",
        description="1.2.17 | 1.2.17 | Describe three methods to obfuscate or hide programs on compromised systems.  Training Resources & Technical References: MITRE “Defense Evasion”, https://attack.mitre.org/tactics/TA0005/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="1.2.18 | 1.2.18 | Describe common data and file obfuscation techniques based on file attributes and naming conventions.",
        description="1.2.18 | 1.2.18 | Describe common data and file obfuscation techniques based on file attributes and naming conventions.  Training Resources & Technical References: MITRE “Hide Artifacts”, https://attack.mitre.org/techniques/T1564/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="1.2.19 | 1.2.19 | (U) Describe the purpose of Handles on a Windows operating system.  Training Resources & Technical Ref",
        description="1.2.19 | 1.2.19 | (U) Describe the purpose of Handles on a Windows operating system.  Training Resources & Technical References: Microsoft.com “Windows System Information”, https://docs.microsoft.com/en- us/windows/win32/sysinfo/windows-system-information |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="1.2.20 | 1.2.20 | Discuss how process handles may indicate anomalous or malicious activity.  Training Resources & Techni",
        description="1.2.20 | 1.2.20 | Discuss how process handles may indicate anomalous or malicious activity.  Training Resources & Technical References: Blackberry Threat Vector Blog “Uncommon Handle Analysis in Incident Response and Forensics”, https://blogs.blackberry.com/en/2013/05/Uncommon-Handle- Analysis-in-Incident-Response-and-Forensics |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="1.2.21 | 1.2.21 | Explain how analyzing the number of handles associated with a process across a given network could be",
        description="1.2.21 | 1.2.21 | Explain how analyzing the number of handles associated with a process across a given network could be used to find anomalous or malicious activity.  Training Resources & Technical References: Blackberry Threat Vector Blog “Uncommon Handle Analysis in Incident Response and Forensics”, https://blogs.blackberry.com/en/2013/05/Uncommon-Handle- Analysis-in-Incident-Response-and-Forensics |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="1.2.22 | 1.2.22 | Services. Define what Windows Services do. Explain how an adversary would use services to maintain per",
        description="1.2.22 | 1.2.22 | Services. Define what Windows Services do. Explain how an adversary would use services to maintain persistence. Creating Malicious Services Modifying Existing Services Hijacking Service Binaries DLL Hijacking and Search Order Abuse Registry-Based Service Configuration Tampering List the associated services used with the following ports: 20/21 22 25 53 80 123 135 139 179 443 445 3389  Training Resources & Technical References: MITRE “Systems Services”, https://attack.mitre.org/techniques/T1569/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="1.2.23 | 1.2.23 | Passwords. Identify the location of passwords on a Windows operating system and on a Linux operating s",
        description="1.2.23 | 1.2.23 | Passwords. Identify the location of passwords on a Windows operating system and on a Linux operating system Discuss how password reuse can be considered a vulnerability Discuss at least three methods that can be used to obtain account passwords  Training Resources & Technical References: Wikipedia “Security Account Manager”, https://en.wikipedia.org/wiki/Security_Account_Manager UltimateWindowsSecurity.com “Security, et al Randy's Blog on Infosec and Other Stuff”, https:// =10/2017 Compasscyber.com “PASSWORD REUSE ATTACKS” Blog By John Lewis, 2017, https:// Sentinelone.com “7 Ways Hackers Steal Your Passwords” Blog By Sentinel One, 24 July 2019, https:// passwords/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="1.2.24 | 1.2.24 | Permission levels. Define the use of permission levels in Windows (Domain, System, Share, and File) De",
        description="1.2.24 | 1.2.24 | Permission levels. Define the use of permission levels in Windows (Domain, System, Share, and File) Define the use of permission levels in Linux  Training Resources & Technical References: Online-Tech-Tips.com “How to Set File and Folder Permissions in Windows” By Asseem Kishore, 13 November 2015, https:// folder-permissions-windows/ Wikipedia “File-System Permissions”, https://en.wikipedia.org/wiki/File-system_permissions |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="1.2.25 | 1.2.25 | Evidence of Program execution. Describe the following artifacts.  UserAssist BAM/DAM Recent Apps ShimC",
        description="1.2.25 | 1.2.25 | Evidence of Program execution. Describe the following artifacts.  UserAssist BAM/DAM Recent Apps ShimCache Jumplists Prefetch Amache.hve Superfetch  Training Resources & Technical References: Wikipedia “Prefetcher”, https://en.wikipedia.org/wiki/Prefetcher |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="1.2.26 | 1.2.26 | Explain the significance of at least two Common Vulnerabilities and Exposures (CVE) reports retrieved",
        description="1.2.26 | 1.2.26 | Explain the significance of at least two Common Vulnerabilities and Exposures (CVE) reports retrieved from the National Vulnerability Database that are relevant to III MEF and the INDOPACOM region.  Training Resources & Technical References: CVE.MITRE.ORG “CVE and NVD Relationship”, https://cve.mitre.org/about/cve_and_nvd_relationship.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="1.2.27 | 1.2.27 | (U) Identify two vulnerability scanner benefits and limitations.  Training Resources & Technical Refer",
        description="1.2.27 | 1.2.27 | (U) Identify two vulnerability scanner benefits and limitations.  Training Resources & Technical References: Computest “The Pros and Cons of Vulnerability Scanning Tools.” Computest, 4 Jan. 2021, Product owner, Marco van den Oever |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="1.2.28 | 1.2.28 | Explain the process of identifying anomalous or potentially malicious files using a known good baselin",
        description="1.2.28 | 1.2.28 | Explain the process of identifying anomalous or potentially malicious files using a known good baseline and full file system directory listing.  Training Resources & Technical References: SANS Whitepaper “Creating a Baseline of Process Activity for Memory Forensics” by Gordon Fraser, 27 August 2014, https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="1.2.29 | 1.2.29 | Demonstrate how to compare file hashes against known lists which include: National Institute of Standa",
        description="1.2.29 | 1.2.29 | Demonstrate how to compare file hashes against known lists which include: National Institute of Standards and Technology (NIST) National Software Reference Library (NSRL). Bit9  Training Resources & Technical References: Wikipedia “File Verification” , https://en.wikipedia.org/wiki/File_verification |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="1.2.30 | 1.2.30 | Explain how and when to use Virus Total.  Training Resources & Technical References: Wikipedia “File V",
        description="1.2.30 | 1.2.30 | Explain how and when to use Virus Total.  Training Resources & Technical References: Wikipedia “File Verification” , https://en.wikipedia.org/wiki/File_verification |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="1.2.31 | 1.2.31 | Describe the significance of the following privilege levels:  SYSTEM Local Administrator Domain Admini",
        description="1.2.31 | 1.2.31 | Describe the significance of the following privilege levels:  SYSTEM Local Administrator Domain Administrator Root Sudoer  Training Resources & Technical References: Microsoft.com “Localsystem Account”, https://docs.microsoft.com/en- us/windows/win32/services/localsystem-account ServerFault.com “Domain Admins vs. Administrators in Windows AD DC” , https://serverfault.com/questions/174200/domain-admins-vs- administrators-in-windows-ad-dc |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="1.2.32 | 1.2.32 | Provide an example command in Windows to recursively list all files, including hidden and system files",
        description="1.2.32 | 1.2.32 | Provide an example command in Windows to recursively list all files, including hidden and system files, of the C: drive.  Training Resources & Technical References: Microsoft.com “dir”, https://docs.microsoft.com/en- us/windows-server/administration/windows-commands/dir |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="1.2.33 | 1.2.33 | Explain how to check for outdated patches.  Training Resources & Technical References: “How to Keep Wi",
        description="1.2.33 | 1.2.33 | Explain how to check for outdated patches.  Training Resources & Technical References: “How to Keep Windows up to Date - Windows Client”, by Deland-Han |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="1.2.34 | 1.2.34 | Explain how to identify multiple installed versions of an application.  Training Resources & Technical",
        description="1.2.34 | 1.2.34 | Explain how to identify multiple installed versions of an application.  Training Resources & Technical References: Microsoft.com “Control Panels”, https://docs.microsoft.com/en- us/windows/win32/uxguide/winenv-ctrl-panels |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="1.2.35 | 1.2.35 | Explain the purpose and significance of the following:  Microsoft Knowledge Base (KB) Microsoft Servic",
        description="1.2.35 | 1.2.35 | Explain the purpose and significance of the following:  Microsoft Knowledge Base (KB) Microsoft Service Packs Password Policy Requirements Auditing Policy User Rights Assignments Event log Settings Registry Permissions File System Auditing File and Folder Permissions Share Permissions Application White-Listing Windows Error Reporting (WER) Cross-Domain Solutions Hardware and Software Baselines Least Privileges  Training Resources & Technical References: Wikipedia, “Microsoft Knowledge Base”, https://en.wikipedia.org/w/Microsoft_Kledge_Base Wikipedia, “Service pa”, https://en.wikipedia.org/w/Service_pac Wikipedia, “Password icy”, https://en.wikipedia.org/w/Passw Ultimate IT Security, “The Ws Secy og Revealed”, https://www.ultimatewindowecuriy.com/securitobook/pe.aspx?spid=chapter2 Microsoft, “User Rights Assien”, https://docs.microsoft.com/enus/prious-veionswndow pro/windows-server-2012-r2and-/dn221963(s.11) Solarwinds Loggly, “Wins Logging c https://e-gde/wis-lgging- basics/ Wikipedia, “Windows Rery” https://en.wikipedia.org/wikiis_Regiry Varonis, “Complete Guide  Ws e System Auditing”, https://www.vas.c/blog/wdowe-syst- auditing/ Online Tech Tips, “How to  File and Folr Permsions i Windows”, https://www.onlitech-tips.com-tips/se file-folder-permissions-wins/ Online Tech Tips, “How to  File and Folr Permsions i Windows”, https://www.onlitech-tips.comcomput-tips/se file-folder-permissions-windows/ Microsoft, “Application Control for Windows”, https://docs.microsoft.com/en-us/windows/security/threat- protection/windows-defender-application-control/windows- defender-application-control Microsoft, “About WER”  Wikipedia, “Cross-domain solution”, https://en.wikipedia.org/wiki/Cross-domain-solution Wikipedia, “Baseline (configuration management)”, https://en.wikipedia.org/wiki/Baseline_(configuration_manage ment) Wikipedia, “Principle of least privilege”, https://en.wikipedia.org/wiki/Principle_of_least_privilege |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="1.2.36 | 1.2.36 | (U) Describe each of the following key Windows processes and their functions: Smss.exe Services.exe Ls",
        description="1.2.36 | 1.2.36 | (U) Describe each of the following key Windows processes and their functions: Smss.exe Services.exe Lsass.exe Csrss.exe Svchost.exe Winlogon.exe Explorer.exe  Training Resources & Technical References: “Windows System Processes - an Overview for Blue Teams.” Medium, Medium, 24 Oct. 2020, by Bencherchali, Nasreddine. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="1.2.37 | 1.2.37 | (U) Discuss Windows default shares. Include the following points in the discussion: What are the defau",
        description="1.2.37 | 1.2.37 | (U) Discuss Windows default shares. Include the following points in the discussion: What are the default shares on a Windows host? What location do they each point to? How can they be used in a cyber-operation? What are the default shares on domain controllers and exchange servers? What does a dollar sign ($) at the end of a share name signify?  Training Resources & Technical References: Computer Hope, “Hidden share”,  MITRE, “Network Share Discovery”, https://attack.mitre.org/techniques/T1135/ Microsoft.com “Remove Administrative Shares - Windows Server” by Deland-Han Cloudwars, “The Ultimate Guide to Windows Shared Drives in 2022”, https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="1.2.38 | 1.2.38 | Describe the function, output, and significance of the following native Windows commands: Ipconfig nbt",
        description="1.2.38 | 1.2.38 | Describe the function, output, and significance of the following native Windows commands: Ipconfig nbtstat netstat at arp route cacls attrib nslookup  Training Resources & Technical References: Microsoft, “ipconfig”,   Microsoft, “nbtstat”,   Microsoft, “netstat”,   Microsoft, “at”,   Microsoft, “arp”,   Microsoft, “route”,    Microsoft, “cacls”,   Microsoft, “attrib”, https://docs.microsoft.com/en- us/windows-server/administration/windows-commands/attrib Microsoft, “nslookup”, https://docs.microsoft.com/en-us/windows-server/administration/windows- commands/nslookup |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="1.2.39 | 1.2.39 | (U) Describe the function, output, and significance of the following Windows NET service commands: a.",
        description="1.2.39 | 1.2.39 | (U) Describe the function, output, and significance of the following Windows NET service commands: a.	net help b.  net group c.	net localgroup administrators d.  net session e.	net share net start net stop net time net use net user net view net statistics  Training esou & Technical References: Mros, “Net Commands On Oating Systems”, hts://ocs.microsoft.com/en-us/tleshoot/windows- seer/rking/net-commands--operating-systems |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="1.2.40 | 1.2.40 | Descrbe t ftion, output, and sigicance of the following Windows Reso Kit tools: k netdom sc srnfo tas",
        description="1.2.40 | 1.2.40 | Descrbe t ftion, output, and sigicance of the following Windows Reso Kit tools: k netdom sc srnfo tas y  Training ourc  Technical Reference M “ill”, https://do.mcrosoft.com/en- us/wndowseer/administrationidows-commands/taskkill M “tdom”, https://do.mcrosoft.com/en- us/iousveions/windows/it-pndows-server-2012-r2- -2/17(v=ws.11) M “.exe create”, httpss.microsoft.com/en- us/wndowseer/administrationidows-commands/sc- cr M “steminfo”, https:/.microsoft.com/en- us/windows-server/administration/windows- commands/systeminfo Microsoft, “tasklist”, https://docs.microsoft.com/en- us/windows-server/administration/windows-commands/tasklist Microsoft, “Dsquery”, https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2- and-2012/cc732952 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="1.2.41 | 1.2.41 | Discuss the significance of the \"at\" command and its relationship with the NT AUTHORITY\SYSTEM account",
        description="1.2.41 | 1.2.41 | Discuss the significance of the \"at\" command and its relationship with the NT AUTHORITY\SYSTEM account.  Training Resources & Technical References: Microsoft, “at”, https://docs.microsoft.com/en-us/windows- server/administration/windows-commands/at |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="1.2.42 | 1.2.42 | Compare differences in the function and purpose of NetBIOS names and a Fully Qualified Domain Names (F",
        description="1.2.42 | 1.2.42 | Compare differences in the function and purpose of NetBIOS names and a Fully Qualified Domain Names (FQDN).  Training Resources & Technical References: Wikipedia, “Fully qualified domain name”, https://en.wikipedia.org/wiki/Fully_qualified_domain_name Network Network Encyclopedia, “Netbios Name”, https://networkencyclopedia.com/netbios-name/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="1.2.43 | 1.2.43 | Explain the following Dynamic Host Configuration Protocol (DHCP) topics: How it works How it works wit",
        description="1.2.43 | 1.2.43 | Explain the following Dynamic Host Configuration Protocol (DHCP) topics: How it works How it works with DNS Describe DHCP scope The purpose of reservations and reserved clients  Training Resources & Technical References: Wikipedia, “Dynamic Host Configuration Protocol”, https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Pro tocol Network World, “DHCP defined and how it works”, https:// and-how-it-works.html IDC Online, “DHCP Scope”, http://www.idc- online.com/technical_references/pdfs/information_technology/D HCP_Scope.pdf Digitally Accurate Inc., “Static IP vs DHCP Reservation”, https:// reservation/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    task = Task(
        title="1.2.44 | 1.2.44 | Explain the following Domain Name System (DNS) topics:  How it works How it works with Active Director",
        description="1.2.44 | 1.2.44 | Explain the following Domain Name System (DNS) topics:  How it works How it works with Active Directory Purpose of DNS zones, forward and reverse Difference between recursive and iterative DNS queries DNS debug log, what can be found, and why it is useful Zone transfers  Training Resources & Technical References: Wikipedia, “Domain Name System”, https://en.wikipedia.org/wiki/Domain_Name_System Microsoft, “DNS and AD DS”, https://docs.microsoft.com/en- us/windows-server/identity/ad-ds/plan/dns-and-ad-ds NS1, “What is a DNS Zone? DNS Zones Explained”, https://ns1.com/resources/dns-zones-explained OmniSecu, “Recursive and Iterative DNS Queries”,   Microsoft.com ,    ClouDNS, “DNS zone transfer and zone file”, |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=94)
    db.session.add(course_task)

    task = Task(
        title="1.2.45 | 1.2.45 | Discuss how an insecurely configured DNS server that allows external, untrusted zone transfers could p",
        description="1.2.45 | 1.2.45 | Discuss how an insecurely configured DNS server that allows external, untrusted zone transfers could provide information to an attacker.  Training Resources & Technical References: Null-Byte, “Zone Transfer Attack to DNS”, https://null- byte.wonderhowto.com/forum/zone-transfer-attack-dns- 0179845/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=95)
    db.session.add(course_task)

    task = Task(
        title="1.2.46 | 1.2.46 | (U) Describe the following Windows Security Features and how they are leveraged during an assessment:",
        description="1.2.46 | 1.2.46 | (U) Describe the following Windows Security Features and how they are leveraged during an assessment: Security Identifiers (SIDs) Access Control Lists (ACLs) Security Accounts Manager (SAM) Tokens Tickets  Training Resources & Technical References: Wikipedia, “Security Identifier”, https://en.wikipedia.org/wiki/Security_Identifier Microsoft, \"Access Control Lists” https://docs.microsoft.com/en- us/windows/win32/secauthz/access-control-lists Wikipedia, “Security Account Manager”,  Microsoft, \"Security tokens” https://docs.microsoft.com/en- us/azure/active-directory/develop/security-tokens |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=96)
    db.session.add(course_task)

    task = Task(
        title="1.2.47 | 1.2.47 | Describe alternate data streaming and hiding in plain sight techniques.  Training Resources & Technica",
        description="1.2.47 | 1.2.47 | Describe alternate data streaming and hiding in plain sight techniques.  Training Resources & Technical References: Malware Bytes, “Introduction to Alternate Data Streams”, https://blog.malwarebytes.com/101/2015/07/introduction  Huntress Labs, “Hiding in Plain Sight”, https://blog.huntresslabs.com/hiding-in-plain-sight- 556469e0a4e |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=97)
    db.session.add(course_task)

    task = Task(
        title="1.2.48 | 1.2.48 | Discuss the significance of the following windows directories:  %SystemRoot%\system32 %SystemRoot%\Sys",
        description="1.2.48 | 1.2.48 | Discuss the significance of the following windows directories:  %SystemRoot%\system32 %SystemRoot%\SysWOW64 %SystemRoot%\temp %System Root%\repair %ProgramFiles(x86)% %SystemRoot%\system32\drivers\etc  Training Resources & Technical References: Make Use Of, “The Windows System32 Directory: What It Is and Why You Can’t Delete It”, https:// Intelligent Systems Monitoring “ Why malware installers use TMP files and the temp folder when infecting windows”, 2017, May 31 Microsoft, “Voulme Shadow Copy Service”, https://docs.microsoft.com/en-us/windows-server/storage/file- server/volume-shadow-copy-service Wikipedia, “Program Files”, https://en.wikipedia.org/wiki/Program_Files Wikipedia, “hosts (file)”, https://en.wikipedia.org/wiki/Hosts_(file) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=98)
    db.session.add(course_task)

    task = Task(
        title="1.2.49 | 1.2.49 | Discuss the significance of the following unix directories:  /opt /bin /dev /var /usr  Training Resour",
        description="1.2.49 | 1.2.49 | Discuss the significance of the following unix directories:  /opt /bin /dev /var /usr  Training Resources & Technical References: EDUCBA, “Unix File System”, https://educba.com/unix-file- system |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=99)
    db.session.add(course_task)

    task = Task(
        title="1.2.50 | 1.2.50 | Compare the differences and similarities between “Trusted Installer” and system accounts.  Training Re",
        description="1.2.50 | 1.2.50 | Compare the differences and similarities between “Trusted Installer” and system accounts.  Training Resources & Technical References: Microsoft, “Supported Resource Replacement Mechanisms”, https://docs.microsoft.com/en- us/windows/win32/wfp/supported-file-replacement-mechanisms |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=100)
    db.session.add(course_task)

    task = Task(
        title="1.2.51 | 1.2.51 | Describe the following terms and indicate how it is relevant to cyber operations: Cryptography types a",
        description="1.2.51 | 1.2.51 | Describe the following terms and indicate how it is relevant to cyber operations: Cryptography types and examples OOB (Out-of-Band) Network SSO (Single Sign-On) MFA (Multi-Factor Authentication) Forensic Artifact Salted Hash NIPS (Network Intrusion Prevention System) VPN Concentrator HIPS(Host Intrusion Prevention System)  Training Resources & Technical References: Geeks for Geeks, “Cryptography and its Types”, https:// Wikipedia, “Out-of-band management”, https://en.wikipedia.org/wiki/Out-of-band_management Auth0 docs, “Single Sign-On”, https://auth0.com/docs/sso Wikipedia, “Multi-factor authentication”, https://en.wikipedia.org/wiki/Multi-factor_authentication Vestige “ Digital artifacts: Digital Forensics vs Cyber Security”, by Hacker Wikipedia, “Salt (cryptography)”, https://en.wikipedia.org/wiki/Salt_(cryptography) ITProToday, “NIPS and HIPS”, https:// Professor Messer, “VPN Concentrators – CompTIA Security+ SY0-501 – 2.1”,   ITProToday, “NIPS and HIPS”, https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=101)
    db.session.add(course_task)

    task = Task(
        title="1.2.52 | 1.2.52 | Describe how 32-bit applications run on a 64-bit Windows platform and what restrictions apply.  Traini",
        description="1.2.52 | 1.2.52 | Describe how 32-bit applications run on a 64-bit Windows platform and what restrictions apply.  Training Resources & Technical References: Microsoft, “Running 32-bit Applications”, https://docs.microsoft.com/en- us/windows/win32/winprog64/running-32-bit-applications |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=102)
    db.session.add(course_task)

    task = Task(
        title="1.2.53 | 1.2.53 | Describe the different types of virtualization, including application, operating system, hardware, and",
        description="1.2.53 | 1.2.53 | Describe the different types of virtualization, including application, operating system, hardware, and presentation.  Training Resources & Technical References: Kelser, “The Seven Types of Virtualization”, https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=103)
    db.session.add(course_task)

    task = Task(
        title="1.2.54 | 1.2.54 | Describe the different types of hypervisors, containers, and virtual machines.  Training Resources & T",
        description="1.2.54 | 1.2.54 | Describe the different types of hypervisors, containers, and virtual machines.  Training Resources & Technical References: Kelser, “The Seven Types of Virtualization”, https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=104)
    db.session.add(course_task)

    task = Task(
        title="1.2.55 | 1.2.55 | List common techniques used to anonymize network traffic from an attack perspective.  Training Resourc",
        description="1.2.55 | 1.2.55 | List common techniques used to anonymize network traffic from an attack perspective.  Training Resources & Technical References: Wired, “Famed Hacker Kevin Mitnick Shows You How to Go Invisible Online”, https:// hacker-kevin-mitnick-shows-go-invisible-online/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=105)
    db.session.add(course_task)

    task = Task(
        title="1.2.56 | 1.2.56 | Research an open source vulnerability assessment to answer mission requirements.  Training Resources &",
        description="1.2.56 | 1.2.56 | Research an open source vulnerability assessment to answer mission requirements.  Training Resources & Technical References: MITRE, “CVE”, https://cve.mitre.org/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=106)
    db.session.add(course_task)

    task = Task(
        title="1.2.57 | 1.2.57 | Describe best practices to collect, assess, and identify improperly configured host-based firewall set",
        description="1.2.57 | 1.2.57 | Describe best practices to collect, assess, and identify improperly configured host-based firewall settings.  Training Resources & Technical References: Ryadel, “Common Firewall Configuration errors and how to avoid them”, https:// configuration-errors-how-avoid/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=107)
    db.session.add(course_task)

    task = Task(
        title="1.2.58 | 1.2.58 | (U) Analyze a Microsoft Security Bulletin and/or open source zero day reporting to identify software a",
        description="1.2.58 | 1.2.58 | (U) Analyze a Microsoft Security Bulletin and/or open source zero day reporting to identify software and operating system vulnerabilities that are exploitable through available capabilities.  Training Resources & Technical References: Microsoft, “Security Advisories and Bulletins”, https://docs.microsoft.com/en-us/security-updates/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=108)
    db.session.add(course_task)

    task = Task(
        title="1.2.59 | 1.2.59 | Describe the purpose, access requirements, classification levels, and sensitivities of data repositori",
        description="1.2.59 | 1.2.59 | Describe the purpose, access requirements, classification levels, and sensitivities of data repositories used to perform mission-essential analytics.  Training Resources & Technical References: Local SOP Joint Chiefs of Staff, “Joint Publication 3-12”, https://fas.org/irp/doddir/dod/jp3_12.pdf |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=109)
    db.session.add(course_task)

    task = Task(
        title="1.2.60 | 1.2.60 | Describe how to collect terminal history for users of a Linux host.  Training Resources & Technical Re",
        description="1.2.60 | 1.2.60 | Describe how to collect terminal history for users of a Linux host.  Training Resources & Technical References: Linux, “Disk/Memory/Forensics”, Linux Forensics by Philip Polstra: ISBN 1515037630 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=110)
    db.session.add(course_task)

    task = Task(
        title="1.2.61 | 1.2.61 | Describe the information that can be found in /etc/passwd, /etc/shadow, and /etc/group  Training Resou",
        description="1.2.61 | 1.2.61 | Describe the information that can be found in /etc/passwd, /etc/shadow, and /etc/group  Training Resources & Technical References: Linux, “Disk/Memory/Forensics”, Linux Forensics by Philip Polstra: ISBN 1515037630 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=111)
    db.session.add(course_task)

    task = Task(
        title="1.2.62 | 1.2.62 | Describe intrusion artifacts that can be found in /proc.  Training Resources & Technical References: L",
        description="1.2.62 | 1.2.62 | Describe intrusion artifacts that can be found in /proc.  Training Resources & Technical References: Linux, “Disk/Memory/Forensics”, Linux Forensics by Philip Polstra: ISBN 1515037630 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=112)
    db.session.add(course_task)

    task = Task(
        title="1.2.63 | 1.2.63 | Describe how jumps in index node number can indicate a malicious file.  Training Resources & Technical",
        description="1.2.63 | 1.2.63 | Describe how jumps in index node number can indicate a malicious file.  Training Resources & Technical References: Linux, “Disk/Memory/Forensics”, Linux Forensics by Philip Polstra: ISBN 1515037630 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=113)
    db.session.add(course_task)

    task = Task(
        title="1.2.64 | 1.2.64 | Define Web Proxy.  Training Resources & Technical References: Forcepoint, “What is a Web Proxy Server?",
        description="1.2.64 | 1.2.64 | Define Web Proxy.  Training Resources & Technical References: Forcepoint, “What is a Web Proxy Server?, https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=114)
    db.session.add(course_task)

    task = Task(
        title="1.3 | 1.3 | (U) Discuss the MITRE ATT&CK Framework and identify potential host artifacts. |  |  |  |",
        description="1.3 | 1.3 | (U) Discuss the MITRE ATT&CK Framework and identify potential host artifacts. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=115)
    db.session.add(course_task)

    task = Task(
        title="1.3.1 | 1.3.1 | Reconnaissance  Training Resources & Technical References: MITRE, “Reconnaissance”, |  |  |  |",
        description="1.3.1 | 1.3.1 | Reconnaissance  Training Resources & Technical References: MITRE, “Reconnaissance”, |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=116)
    db.session.add(course_task)

    task = Task(
        title="1.3.2 | 1.3.2 | Resource Development  Training Resources & Technical References: MITRE, “Resource Development”, https://",
        description="1.3.2 | 1.3.2 | Resource Development  Training Resources & Technical References: MITRE, “Resource Development”, https://attack.mitre.org/tactics/TA00432 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=117)
    db.session.add(course_task)

    task = Task(
        title="1.3.3 | 1.3.3 | Initial Access  Training Resources & Technical References: MITRE, “ATT&CK Framework”, https://attack.mit",
        description="1.3.3 | 1.3.3 | Initial Access  Training Resources & Technical References: MITRE, “ATT&CK Framework”, https://attack.mitre.org/tactics/TA0001 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=118)
    db.session.add(course_task)

    task = Task(
        title="1.3.4 | 1.3.4 | Execution  Training Resources & Technical References: MITRE, “Execution”, https://attack.mitre.org/tacti",
        description="1.3.4 | 1.3.4 | Execution  Training Resources & Technical References: MITRE, “Execution”, https://attack.mitre.org/tactics/TA0002 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=119)
    db.session.add(course_task)

    task = Task(
        title="1.3.5 | 1.3.5 | Privilege Escalation  Training Resources & Technical References: MITRE, “Privilege Escalation”, https://",
        description="1.3.5 | 1.3.5 | Privilege Escalation  Training Resources & Technical References: MITRE, “Privilege Escalation”, https://attack.mitre.org/tactics/TA0004 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=120)
    db.session.add(course_task)

    task = Task(
        title="1.3.6 | 1.3.6 | Defense Evasion  Training Resources & Technical References: MITRE, “Defense Evasion”, https://attack.mit",
        description="1.3.6 | 1.3.6 | Defense Evasion  Training Resources & Technical References: MITRE, “Defense Evasion”, https://attack.mitre.org/tactics/TA0005 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=121)
    db.session.add(course_task)

    task = Task(
        title="1.3.7 | 1.3.7 | Credential Access  Training Resources & Technical References: MITRE, “Credential Access”, https://attack",
        description="1.3.7 | 1.3.7 | Credential Access  Training Resources & Technical References: MITRE, “Credential Access”, https://attack.mitre.org/tactics/TA0006 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=122)
    db.session.add(course_task)

    task = Task(
        title="1.3.8 | 1.3.8 | Discovery  Training Resources & Technical References: MITRE, “Discovery”, https://attack.mitre.org/tacti",
        description="1.3.8 | 1.3.8 | Discovery  Training Resources & Technical References: MITRE, “Discovery”, https://attack.mitre.org/tactics/TA0007 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=123)
    db.session.add(course_task)

    task = Task(
        title="1.3.9 | 1.3.9 | Lateral movement  Training Resources & Technical References: MITRE, “Lateral Movement”, https://attack.m",
        description="1.3.9 | 1.3.9 | Lateral movement  Training Resources & Technical References: MITRE, “Lateral Movement”, https://attack.mitre.org/tactics/TA0008 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=124)
    db.session.add(course_task)

    task = Task(
        title="1.3.10 | 1.3.10 | (U) Collection  Training Resources & Technical References: MITRE, “Collection”, https://attack.mitre.o",
        description="1.3.10 | 1.3.10 | (U) Collection  Training Resources & Technical References: MITRE, “Collection”, https://attack.mitre.org/tactics/TA0009 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=125)
    db.session.add(course_task)

    task = Task(
        title="1.3.11 | 1.3.11 | Command and Control  Training Resources & Technical References: MITRE, “Command and Control”, https://",
        description="1.3.11 | 1.3.11 | Command and Control  Training Resources & Technical References: MITRE, “Command and Control”, https://attack.mitre.org/tactics/TA0011 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=126)
    db.session.add(course_task)

    task = Task(
        title="1.3.12 | 1.3.12 | Exfiltration  Training Resources & Technical References: MITRE, “Exfiltration”, https://attack.mitre.o",
        description="1.3.12 | 1.3.12 | Exfiltration  Training Resources & Technical References: MITRE, “Exfiltration”, https://attack.mitre.org/tactics/TA0010 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=127)
    db.session.add(course_task)

    task = Task(
        title="1.3.13 | 1.3.13 | Impact  Training Resources & Technical References: MITRE, “Impact”, https://attack.mitre.org/tactics/T",
        description="1.3.13 | 1.3.13 | Impact  Training Resources & Technical References: MITRE, “Impact”, https://attack.mitre.org/tactics/TA0040 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=128)
    db.session.add(course_task)

    task = Task(
        title="Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and ex",
        description="Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=129)
    db.session.add(course_task)

    task = Task(
        title="2.1 | 2.1 | (U) Host Analysis |  |  |  |",
        description="2.1 | 2.1 | (U) Host Analysis |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=130)
    db.session.add(course_task)

    task = Task(
        title="2.1.1 | 2.1.1 | Describe the following capabilities of Splunk.  Custom Searches Alerts Dashboards and Reports Incident I",
        description="2.1.1 | 2.1.1 | Describe the following capabilities of Splunk.  Custom Searches Alerts Dashboards and Reports Incident Investigations  Training Resources & Technical References: Splunk PECL |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=131)
    db.session.add(course_task)

    task = Task(
        title="2.1.2 | 2.1.2 | (U)  Describe the following capabilities of Security Onion.  Network Traffic Configuration Elastic Stack",
        description="2.1.2 | 2.1.2 | (U)  Describe the following capabilities of Security Onion.  Network Traffic Configuration Elastic Stack Alerts Suricata  Training Resources & Technical References: Security Onion PECL |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=132)
    db.session.add(course_task)

    task = Task(
        title="2.1.3 | 2.1.3 | (U) Describe the following capabilities of Red Seal.  Network Mapping and Topology Visualization Vulnera",
        description="2.1.3 | 2.1.3 | (U) Describe the following capabilities of Red Seal.  Network Mapping and Topology Visualization Vulnerability and Risk Analysis Attack Pathway Simulation  Training Resources & Technical References: Red Seal PECL |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=133)
    db.session.add(course_task)

    task = Task(
        title="2.1.4 | 2.1.4 | (U) Describe the following capabilities of Palo Alto.  Firewall Rules Traffic and Threat Log Monitoring",
        description="2.1.4 | 2.1.4 | (U) Describe the following capabilities of Palo Alto.  Firewall Rules Traffic and Threat Log Monitoring Remote Access Tunnels  Training Resources & Technical References: Palo Alto PECL |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=134)
    db.session.add(course_task)

    task = Task(
        title="2.1.5 | 2.1.5 | Describe the following capabilities of Tanium.  Endpoint Visibility Vulnerability and Patch Management T",
        description="2.1.5 | 2.1.5 | Describe the following capabilities of Tanium.  Endpoint Visibility Vulnerability and Patch Management Threat Hunting and Incident Investigation Compliance and Security Policy Remediation   Training Resources & Technical References: Tanium, “TANIUM USER DOCUMENTATION”, |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=135)
    db.session.add(course_task)

    task = Task(
        title="2.1.6 | 2.1.6 | (U)  Describe the following capabilities of MDE.  Security Alert and Incident Investigation Threat Respo",
        description="2.1.6 | 2.1.6 | (U)  Describe the following capabilities of MDE.  Security Alert and Incident Investigation Threat Response Advanced Queries Data Analysis  Training Resources & Technical References: X |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=136)
    db.session.add(course_task)

    task = Task(
        title="2.1.7 | 2.1.7 | Describe the following capabilities of HX.  Endpoint Monitoring Endpoint Threat Detection and Investigat",
        description="2.1.7 | 2.1.7 | Describe the following capabilities of HX.  Endpoint Monitoring Endpoint Threat Detection and Investigation Root Cause Analysis Endpoint Isolation  Training Resources & Technical References: HX Class |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=137)
    db.session.add(course_task)

    task = Task(
        title="2.2 | 2.2 | (U) Software |  |  |  |",
        description="2.2 | 2.2 | (U) Software |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=138)
    db.session.add(course_task)

    task = Task(
        title="2.2.3 | 2.2.3 | Describe the primary functions PowerShell.  Training Resources & Technical References: Microsoft, “Power",
        description="2.2.3 | 2.2.3 | Describe the primary functions PowerShell.  Training Resources & Technical References: Microsoft, “Powershell Documentation”, https://docs.microsoft.com/en-us/powershell/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=139)
    db.session.add(course_task)

    task = Task(
        title="2.2.4 | 2.2.4 | Describe the primary functions Sysinternals.  Training Resources & Technical References: Microsoft, “PsE",
        description="2.2.4 | 2.2.4 | Describe the primary functions Sysinternals.  Training Resources & Technical References: Microsoft, “PsExec v2.34”, https://docs.microsoft.com/en  Microsoft, “Autoruns fo4r Windows v14.09”, |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=140)
    db.session.add(course_task)

    task = Task(
        title="2.2.5 | 2.2.5 | (U) Describe the primary functions of windows native tools.  Regedit Certutil Windows Event Viewer Task",
        description="2.2.5 | 2.2.5 | (U) Describe the primary functions of windows native tools.  Regedit Certutil Windows Event Viewer Task Scheduler Netsh Service Control manager  Training Resources & Technical References: Microsoft, “Registry”, https://docs.microsoft.com/en  Microsoft, “certutil”, https://docs.microsoft.com/en- us/windows-server/administration/windows-commands/certutil Microsoft, “Windows Event log”, https://docs.microsoft.com/en-us/windows/win32/wes/windows- event-log Microsoft, “Task Scheduler for developers:, https://docs.microsoft.com/en-us/windows/win32/taskschd/task- scheduler-start-page Microsoft, “Netsh Command Syntax, Contents, and Formatting”, https://docs.microsoft.com/en-us/windows- server/networking/technologies/netsh/netsh-contexts Microsoft, “sc.exe create”, |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=141)
    db.session.add(course_task)

    task = Task(
        title="Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the",
        description="Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=142)
    db.session.add(course_task)

    task = Task(
        title="3.1 | 3.1 | (U) Demonstration |  |  |  |",
        description="3.1 | 3.1 | (U) Demonstration |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=143)
    db.session.add(course_task)

    task = Task(
        title="3.1.1 | 3.1.1 | Demonstrate at least two ways to access the following native OS tools locally and remotely:  WINDOWS: Wi",
        description="3.1.1 | 3.1.1 | Demonstrate at least two ways to access the following native OS tools locally and remotely:  WINDOWS: Windows Event Viewer Task scheduler Regedit Windows Management Instrumentation Powershell  LINUX: SSH Bash  Training Resources & Technical References: Microsoft, “Windows Event Log” https://docs.microsoft.com/en  Microsoft, “Task Scheduler for developers”,   Microsoft, “Registry”,   “Abusing windows management instrumentation (WMI) to build a persistent ... Abusing Windows Management Instrumentation (WMI) to Build a Persistent, Asynchronous, and Fileless Backdoor”, 2015, by Matt Graeber |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=144)
    db.session.add(course_task)

    task = Task(
        title="3.1.2 | 3.1.2 | Analyze and refine vulnerability tools in a test environment to optimize performance in accordance with",
        description="3.1.2 | 3.1.2 | Analyze and refine vulnerability tools in a test environment to optimize performance in accordance with mission objectives.  Training Resources & Technical References: Microsoft,“Registry,” https://docs.microsoft.com/en- us/windows/win32/sysinfo/registry |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=145)
    db.session.add(course_task)

    task = Task(
        title="3.1.3 | 3.1.3 | (U) Create a script or program that employs multiple inputs, command line arguments, and environmental v",
        description="3.1.3 | 3.1.3 | (U) Create a script or program that employs multiple inputs, command line arguments, and environmental variables to solve a mission requirement. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=146)
    db.session.add(course_task)

    task = Task(
        title="3.1.5 | 3.1.5 | Identify the appropriate security control measures to implement based on a given threat actor TTP.  Trai",
        description="3.1.5 | 3.1.5 | Identify the appropriate security control measures to implement based on a given threat actor TTP.  Training Resources & Technical References: SANS Institute, “SIFT Workstation”, https://digital- forensics.sans.org/community/downloads |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=147)
    db.session.add(course_task)

    task = Task(
        title="3.1.7 | 3.1.7 | Explain how to use software debugging tools to identify potential vulnerabilities, illegitimate function",
        description="3.1.7 | 3.1.7 | Explain how to use software debugging tools to identify potential vulnerabilities, illegitimate functionality, and hidden content.  Training Resources & Technical References: SANS Institute, “Hunting and Gathering with PowerShell”, https://powershell/121279 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=148)
    db.session.add(course_task)

    task = Task(
        title="3.1.8 | 3.1.8 | (U) Identify appropriate security controls that align with detecting and inhibiting known adversarial ca",
        description="3.1.8 | 3.1.8 | (U) Identify appropriate security controls that align with detecting and inhibiting known adversarial capabilities, tactics, techniques, and procedures. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=149)
    db.session.add(course_task)

    task = Task(
        title="3.1.9 | 3.1.9 | (U) Detect a rogue or unauthorized system within a specified domain on the network using available tools",
        description="3.1.9 | 3.1.9 | (U) Detect a rogue or unauthorized system within a specified domain on the network using available tools, techniques, and information. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=150)
    db.session.add(course_task)

    task = Task(
        title="3.1.10 | 3.1.10 | Analyze a software baseline to identify systemic issues that could lead to vulnerability exploitation.",
        description="3.1.10 | 3.1.10 | Analyze a software baseline to identify systemic issues that could lead to vulnerability exploitation.  Training Resources & Technical References: Geeksforgeeks.org, “Software Engineering | Debugging”, https:// debugging/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=151)
    db.session.add(course_task)

    task = Task(
        title="3.1.11 | 3.1.11 | (U) Assess domain-joined and stand-alone systems for improper configurations. |  |  |  |",
        description="3.1.11 | 3.1.11 | (U) Assess domain-joined and stand-alone systems for improper configurations. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=152)
    db.session.add(course_task)

    task = Task(
        title="3.1.12 | 3.1.12 | Assess domain-joined and stand-alone systems for anomalous or malicious behavior.  Training Resources",
        description="3.1.12 | 3.1.12 | Assess domain-joined and stand-alone systems for anomalous or malicious behavior.  Training Resources & Technical References: Geeksforgeeks.org, “Software Engineering | Debugging”, https:// debugging/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=153)
    db.session.add(course_task)

    task = Task(
        title="3.1.13 | 3.1.13 | (U) Assess a system and/or host group management, group memberships, users, and privileges to identify",
        description="3.1.13 | 3.1.13 | (U) Assess a system and/or host group management, group memberships, users, and privileges to identify system issues, improper access to network resources, and malicious behavior. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=154)
    db.session.add(course_task)

    task = Task(
        title="Module 4.0 – (U) Deployable Mission Support System Fundamentals | Module 4.0 – (U) Deployable Mission Support System Fun",
        description="Module 4.0 – (U) Deployable Mission Support System Fundamentals | Module 4.0 – (U) Deployable Mission Support System Fundamentals | Module 4.0 – (U) Deployable Mission Support System Fundamentals | Module 4.0 – (U) Deployable Mission Support System Fundamentals | Module 4.0 – (U) Deployable Mission Support System Fundamentals | Module 4.0 – (U) Deployable Mission Support System Fundamentals | Module 4.0 – (U) Deployable Mission Support System Fundamentals",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=155)
    db.session.add(course_task)

    task = Task(
        title="4.1 | 4.1 | (U) Hardware |  |  |  |",
        description="4.1 | 4.1 | (U) Hardware |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=156)
    db.session.add(course_task)

    task = Task(
        title="4.1.1 | 4.1.1 | Explain the function of the following appliances: Hub Switches (non-managed/managed) Wireless access poi",
        description="4.1.1 | 4.1.1 | Explain the function of the following appliances: Hub Switches (non-managed/managed) Wireless access point Routers Firewall Wireless Router  Training Resources & Technical References: Wikipedia, “Ethernet hub”, https://en.wikipedia.org/wiki/Ethernet_hub Wikipedia, “Network Switch”, https://en.wikipedia.org/wiki/Network_switch Wikipedia, “Wireless access point”, https://en.wikipedia.org/wiki/Wireless_access_point Wikipedia, “Router (computing)”, https://en.wikipedia.org/wiki/Router_(computing) Wikipedia, “Firewall (computing)”, https://en.wikipedia.org/wiki/Firewall_(computing) Wikipedia, “Wireless router”, https://en.wikipedia.org/wiki/Wireless_router |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=157)
    db.session.add(course_task)

    task = Task(
        title="4.1.2 | 4.1.2 | Explain the following storage concepts and devices: Redundant storage Non-redundant storage Non-RAID con",
        description="4.1.2 | 4.1.2 | Explain the following storage concepts and devices: Redundant storage Non-redundant storage Non-RAID controller RAID controller Disk Network attached storage appliance SAN and VSAN  Training Resources & Technical References: Wikipedia, “Data Redundancy”, https://en.wikipedia.org/wiki/Data_redundan Wikipedia, “Non-RAID drive architectures, https://en.wikipedia.org/wiki/Non-RAID_dre_architectures Wikipedia, “Disk array controller”, https://en.wikipedia.org/wiki/Disk_array_contoller Wikipedia, “Disk storage”, https://en.wikipedia.org/wiki/Disk_storage Wikipedia, “Network-attached storage”, https://en.wikipedia.org/wiki/Network-attacd_storage |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=158)
    db.session.add(course_task)

    task = Task(
        title="4.1.3 | 4.1.3 | For each of the following hardware pieces of the kit, identify and explain the utility for host or netwo",
        description="4.1.3 | 4.1.3 | For each of the following hardware pieces of the kit, identify and explain the utility for host or network analysis: CyberPAC MiniRax GigaVue Tap Cisco ASA NAS Cisco Switch  Training Resources & Technical References: Wikipedia, “Bare-Metal Server, https://en.wikipedia.org/wiki/Bare-metal_server Wikipedia, “Virtual Sensing”, https://en.wikipedia.org/wiki/Virtual_sensing Profitap, “All You Need to Know About Network Packet Brokers” Vmware, “What is a Kubernetes cluster?”, https:// cluser.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=159)
    db.session.add(course_task)

    task = Task(
        title="4.2 | 4.2 | (U) Virtual Machines |  |  |  |",
        description="4.2 | 4.2 | (U) Virtual Machines |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=160)
    db.session.add(course_task)

    task = Task(
        title="4.2.1 | 4.2.1 | (U) For each of the following virtual machines on the kit, identify and explain the utility for host or",
        description="4.2.1 | 4.2.1 | (U) For each of the following virtual machines on the kit, identify and explain the utility for host or network analysis: ESXi Palo Alto Splunk Security Onion RedSeal  Training Resources & Technical References: ESXi User Guide Palo Alto PECL Splunk PECL Security Onion PECL RedSeal PECL |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=161)
    db.session.add(course_task)

    db.session.commit()

# === Host Senior Tasks ===
course = Course.query.filter_by(name="Host Senior").first()
if course:
    task = Task(
        title="Task # | (U) Senior Host Analyst | JCT&CS ID# | Trainee Initials | Trainer Initials | Trainer Initials | Date Qualified",
        description="Task # | (U) Senior Host Analyst | JCT&CS ID# | Trainee Initials | Trainer Initials | Trainer Initials | Date Qualified",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studi",
        description="Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the training references (TR) listed will aid you in a self or guided study program. All references cited for study are selected according to their credibility and availability.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="1.1 | (U) DCO-IDM & Mission Knowledge |  |  |  |  |",
        description="1.1 | (U) DCO-IDM & Mission Knowledge |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="1.1.1 | Given intelligence reporting describe how to integrate it into tactical planning.  Training Resources & Technica",
        description="1.1.1 | Given intelligence reporting describe how to integrate it into tactical planning.  Training Resources & Technical References: JP 2-01.3 JP 3-0 JP 5-0 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="1.1.2 | Describe the process of developing analytics to support mission requirements and reporting.  Training Resources",
        description="1.1.2 | Describe the process of developing analytics to support mission requirements and reporting.  Training Resources & Technical References: Local SOP |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="1.1.3 | Describe the process for surveilling Named Areas of Interest (NAIs).  Training Resources & Technical References:",
        description="1.1.3 | Describe the process for surveilling Named Areas of Interest (NAIs).  Training Resources & Technical References: JP 5-0 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="1.1.4 | Describe under what circumstances you would need to engage with the local Counter Intelligence or law enforcemen",
        description="1.1.4 | Describe under what circumstances you would need to engage with the local Counter Intelligence or law enforcement agencies.  Training Resources & Technical References: EO12333, “Raw SIGINT availability procedures”, https://fas.org/sgp/othergov/intel/sigint-raw.pdf |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="1.1.5 | Given a critical asset list/key terrain cyber prioritize vulnerabilities for the mission owner.  Training Resour",
        description="1.1.5 | Given a critical asset list/key terrain cyber prioritize vulnerabilities for the mission owner.  Training Resources & Technical References: CIS Critical Security Controls |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="1.1.6 | Describe the chain of custody and your role in maintaining it and relationship with CI/LE.  Training Resources &",
        description="1.1.6 | Describe the chain of custody and your role in maintaining it and relationship with CI/LE.  Training Resources & Technical References: NIST SP 800-86 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="1.1.7 | Demonstrate understanding of the following policies and documents: Executive Order 12333 (as amended) DOD Direct",
        description="1.1.7 | Demonstrate understanding of the following policies and documents: Executive Order 12333 (as amended) DOD Directive 5240.1 (change 2) DODM 5240.01 DOD Directive 5148.13  Training Resources & Technical References: USCC Intelligence Oversight Plan |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="1.1.8 | Explain the difference between Cyberspace authorities and SIGINT authorities.  Training Resources & Technical Re",
        description="1.1.8 | Explain the difference between Cyberspace authorities and SIGINT authorities.  Training Resources & Technical References: EO12333, “Raw SIGINT vailability procedures” https://fas.org/sgp/othergov/intel/sigint-raw.pdf USSID1231 USSID1610 ISS-268-11 ISS-166-11 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="1.1.9 | Describe the ME Lead’s responsibilities toward mission owner interaction.  Training Resources & Technical Refere",
        description="1.1.9 | Describe the ME Lead’s responsibilities toward mission owner interaction.  Training Resources & Technical References: EO12333, “Raw SIGINT availability procedures”, https://fas.org/sgp/othergov/intel/sigint-raw.pdf |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="1.1.10 | Describe how the ME Lead will synchronize efforts with local defenders, customer and key stakeholders.  Trainin",
        description="1.1.10 | Describe how the ME Lead will synchronize efforts with local defenders, customer and key stakeholders.  Training Resources & Technical References: Joint Chiefs of Staff, “CHAIRMAN OF THE JOINT CHIEFS OF STAFF MANUAL”, https:// m651001.pdf?ver=2016-0205-175710-897 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="1.1.11 | Describe how, by working with the mission owner, the ME Lead can determine where to concentrate data collection",
        description="1.1.11 | Describe how, by working with the mission owner, the ME Lead can determine where to concentrate data collection.  Training Resources & Technical References: Local SOP |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="1.1.12 | Explain the importance of an out-brief and what should be included.  Training Resources & Technical References:",
        description="1.1.12 | Explain the importance of an out-brief and what should be included.  Training Resources & Technical References: National Institute of Standards and Technology . (2013, September 13). 4th Cybersecurity Framework Workshop Outbrief and Discussion of Next Steps. Dallas Texas |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="1.1.13 | Explain the importance of the final report and what it should include.  Training Resources & Technical Referenc",
        description="1.1.13 | Explain the importance of the final report and what it should include.  Training Resources & Technical References: SANS, “Tips for Creating a Strong Cybersecurity Assessment Report”, https:// cybersecurity-assessment-report/ Local SOP |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="1.1.14 | Explain how to prioritize Host Analyst findings and mitigation recommendations in the final report.  Training R",
        description="1.1.14 | Explain how to prioritize Host Analyst findings and mitigation recommendations in the final report.  Training Resources & Technical References:  National Infrastructure Advisory Council, Vulnerability Disclosure Framework \"Final Report and Recommendations by the Council\", Chamber J.T., Thompson J.W. 13 January 2004 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="1.1.15 | Describe the ME Leads responsibilities for reporting.  Training Resources & Technical References: National Infr",
        description="1.1.15 | Describe the ME Leads responsibilities for reporting.  Training Resources & Technical References: National Infrastructure Advisory Council, Vulnerability Disclosure Framework \"Final Report and Recommendations by the Council\", Chamber J.T., Thompson J.W. 13 January 2004. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="1.1.16 | Describe how to utilize “phase line” when executing the mission and the importance of it.  Training Resources &",
        description="1.1.16 | Describe how to utilize “phase line” when executing the mission and the importance of it.  Training Resources & Technical References: Local SOP |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="1.2 | (U) Collection Planning |  |  |  |  |",
        description="1.2 | (U) Collection Planning |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="1.2.1 | Discuss what a collection plan is and how pertinent it is to accomplish a successful mission.  Training Resource",
        description="1.2.1 | Discuss what a collection plan is and how pertinent it is to accomplish a successful mission.  Training Resources & Technical References: TarLogic, “Data Collection Plan: A key Component of the Intelligence Cycle”, https:// collection-plan-a-key-component-of-the-intelligence-cycle/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="1.2.2 | Given a list of resources define what is relevant in building a collection plan.  Training Resources & Technical",
        description="1.2.2 | Given a list of resources define what is relevant in building a collection plan.  Training Resources & Technical References: TarLogic, “Data Collection Plan: A key Component of the Intelligence Cycle”, https:// collection-plan-a-key-component-of-the-intelligence-cycle/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="1.2.3 | (U) Identify the steps on building a collection plan.  Training Resources & Technical References: TarLogic, “Dat",
        description="1.2.3 | (U) Identify the steps on building a collection plan.  Training Resources & Technical References: TarLogic, “Data Collection Plan: A key Component of the Intelligence Cycle”, https://collection-plan-a-key-component-of-the-intelligence-cycle/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="1.2.4 | Explain why it is important to understand the customer’s organizational policies for users and computers.  Train",
        description="1.2.4 | Explain why it is important to understand the customer’s organizational policies for users and computers.  Training Resources & Technical References: PowerDMS, “Following Policies and procedures, and why it’s important”, https:// policies-and-procedures-why-its-important/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="1.2.5 | Identify the importance of a Pre-Deployment Site Survey.  Training Resources & Technical References: Cisco, “Tak",
        description="1.2.5 | Identify the importance of a Pre-Deployment Site Survey.  Training Resources & Technical References: Cisco, “Take your network as seriously as your business”, |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="1.2.6 | Define the term “Rules of Engagement” and how it applies to a mission.  Training Resources & Technical Reference",
        description="1.2.6 | Define the term “Rules of Engagement” and how it applies to a mission.  Training Resources & Technical References: Military.com, “Cyber Attacks and Warfare – Rules of Engagement”, https:// attacks-warfare-rules-of-engagement |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="1.3 | (U) Host Knowledge |  |  |  |  |",
        description="1.3 | (U) Host Knowledge |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="1.3.1 | Given organization system policy identify invalid active directory objects.  Training Resources & Technical Refe",
        description="1.3.1 | Given organization system policy identify invalid active directory objects.  Training Resources & Technical References: Microsoft, “MCSA Windows server 2016 complete study guide 2nd edition by William Panek”, March 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="| Dishan Francis, “Mastering Active Directory: understanding the core functionalities of active director services using",
        description="| Dishan Francis, “Mastering Active Directory: understanding the core functionalities of active director services using Microsoft server 2016 and PowerShell”, June 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="1.3.2 | Given an Active Directory domain audit policy and threat actor tactics, techniques and procedures identify audit",
        description="1.3.2 | Given an Active Directory domain audit policy and threat actor tactics, techniques and procedures identify auditing gaps that would prevent logging.  Training Resources & Technical References: Microsoft, “MCSA Windows server 2016 complete study guide 2nd edition by William Panek”, 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="1.3.3 | Demonstrate using PowerShell to manage Active Directory applicable to cyber operations.  Training Resources & Te",
        description="1.3.3 | Demonstrate using PowerShell to manage Active Directory applicable to cyber operations.  Training Resources & Technical References: Dishan Francis, “Mastering Active Directory: understanding the core functionalities of active director services using Microsoft server 2016 and PowerShell”, June 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="1.3.4 | Interpret and configure host-based firewalls and Host Intrusion Prevention Systems through group policy.  Traini",
        description="1.3.4 | Interpret and configure host-based firewalls and Host Intrusion Prevention Systems through group policy.  Training Resources & Technical References: Microsoft, “MCSA Windows server 2016 complete study guide 2nd edition by William Panek”, March 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="1.3.5 | Explain how to ensure patches are up to date for all domain workstations and determine effectiveness of current",
        description="1.3.5 | Explain how to ensure patches are up to date for all domain workstations and determine effectiveness of current process for updating.  Training Resources & Technical References: Microsoft, “MCSA Windows server 2016 complete study guide 2nd edition by William Panek”, March 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="1.3.6 | Given a list of IOCs identify key log entries/Event IDs ,use a Security information and event management (SIEM)",
        description="1.3.6 | Given a list of IOCs identify key log entries/Event IDs ,use a Security information and event management (SIEM) platform to correlate indicators of compromise, and develop dashboards to better visualize data.  Training Resources & Technical References: Jason T. Luttgens, Matthew Pepe and Kevin Mandia, “Incident Response & Computer Forensics, Third Edition” Betsy Sigman & Erickson Delgado, “Splunk essentials 2nd Edition Sep. 2016.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="1.3.7 | Using a SIEM create alerts to detect the creation of unauthorized accounts.  Training Resources & Technical Refe",
        description="1.3.7 | Using a SIEM create alerts to detect the creation of unauthorized accounts.  Training Resources & Technical References: Microsoft, “MCSA Windows server 2016 complete study guide 2nd edition by William Panek”, March 2016. Dishan Francis, “Mastering Active Directory: understanding the core functionalities of active director services using Microsoft server 2016 and PowerShell”, June 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="1.3.8 | Configure, forward, and statically analyze logs from all workstations in an enterprise environment.  Training Re",
        description="1.3.8 | Configure, forward, and statically analyze logs from all workstations in an enterprise environment.  Training Resources & Technical References: Andrei Miroshnikov, “Windows Security Monitoring, 2018.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="1.3.9 | Describe the relationship between the pyramid of pain and the development of signatures and detection methods.",
        description="1.3.9 | Describe the relationship between the pyramid of pain and the development of signatures and detection methods.  Training Resources & Technical References: William Panek, M”CSA Windows 10 Study guide 2016.” Andrei Miroshnikov, “Windows Security Monitoring 2018. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="1.3.10 | (U) Explain how to oversee the tuning of host-based IDS/IPS alerts in order to evaluate their severity while el",
        description="1.3.10 | (U) Explain how to oversee the tuning of host-based IDS/IPS alerts in order to evaluate their severity while eliminating false positives.  Training Resources & Technical References: MCSA Windows 10 Study guide by William Panek 2016 Windows Security Monitoring by Andrei Miroshnikov 2018. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="1.3.11 | Given a list of active processes identify libraries, modules, executables, and binaries against databases of kn",
        description="1.3.11 | Given a list of active processes identify libraries, modules, executables, and binaries against databases of known advanced malware.  Training Resources & Technical References: Dmitry Vostokov, “Windows memory dump analysis advanced V2.0 2017.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="1.3.12 | Given and IOC, explain how to utilize tools and analysis techniques to identify processes, libraries, modules,",
        description="1.3.12 | Given and IOC, explain how to utilize tools and analysis techniques to identify processes, libraries, modules, and other activity that have been obfuscated and might indicate the presence of a more advanced rootkit on endpoint.  Training Resources & Technical References: Christopher c. Elisan, Michael A. Davis; Sean M. Bodmer and Aaron LeMasters, “Hacking exposed Malware & Rootkits: security secrets and solutions 2nd Edition June 2016.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="1.3.13 | Given a Prioritized Defended Asset list, identify which dependent systems are key terrain.  Training Resources",
        description="1.3.13 | Given a Prioritized Defended Asset list, identify which dependent systems are key terrain.  Training Resources & Technical References: Conrad, Misenar, and Feldman, “CISSP Study Guide Third Edition 2016. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="1.3.14 | Evaluate patch levels on host machines across a complex Windows domain to determine the current patch level con",
        description="1.3.14 | Evaluate patch levels on host machines across a complex Windows domain to determine the current patch level consistency.  Training Resources & Technical References: Herb Scribner, “Nessus March 2017.” DISA Guidance |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="1.3.15 | Given a host baseline of configuration/state, for host machines on a network conduct a scan for anomalous confi",
        description="1.3.15 | Given a host baseline of configuration/state, for host machines on a network conduct a scan for anomalous configurations.  Training Resources & Technical References: DISA Guidance |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="1.3.16 | Given a Windows Domain Controller, evaluate information (e.g. users, groups, trust relationships, and security",
        description="1.3.16 | Given a Windows Domain Controller, evaluate information (e.g. users, groups, trust relationships, and security policies) from a complex Domain to identify vulnerabilities/misconfiguration, and how to export this information.  Training Resources & Technical References: Dishan Francis, “Mastering Active Directory: understanding the core functionalities of active director services using Microsoft server 2016 and Powershell, June 2016.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="1.3.17 | Given a script determine what is occurring.  Training Resources & Technical References: Christopher c. Elisan,",
        description="1.3.17 | Given a script determine what is occurring.  Training Resources & Technical References: Christopher c. Elisan, Michael A. Davis; Sean M. Bodmer and Aaron LeMasters, “Hacking exposed Malware & Rootkits: security secrets and solutions 2nd Edition, June 2016.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="1.3.18 | Perform device discovery in order to conduct enumeration of a complex network while limiting the amount of netw",
        description="1.3.18 | Perform device discovery in order to conduct enumeration of a complex network while limiting the amount of network traffic generated.  Training Resources & Technical References: Mohammad Junaid, “Analyzing Network traffic with wireshark 2.6, Sept. 2018.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="1.3.19 | Analyze host discovery tool output to generate accurate maps of endpoint systems.  Training Resources & Technic",
        description="1.3.19 | Analyze host discovery tool output to generate accurate maps of endpoint systems.  Training Resources & Technical References: Mohammad Junaid, “Analyzing Network traffic with wireshark 2.6, Sept. 2018.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="1.4 | (U) Enterprise Domain Knowledge |  |  |  |  |",
        description="1.4 | (U) Enterprise Domain Knowledge |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="1.4.1 | (U) Given an enterprise domain, explain how to identify potentially malicious processes, connections, libraries,",
        description="1.4.1 | (U) Given an enterprise domain, explain how to identify potentially malicious processes, connections, libraries, and other malicious code/activity from a memory image and perform trend and outlier analysis.  Training Resources & Technical References: EC-Council, “Computer Forensics: Investigation Procedures and Response (CHFI) Second Edition.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="1.4.2 | Automate advanced and repetitive tasks on remote workstations within a domain.  Training Resources & Technical R",
        description="1.4.2 | Automate advanced and repetitive tasks on remote workstations within a domain.  Training Resources & Technical References: A. Sweigart, “Automate the Boring Stuff with Python, 2015.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="1.4.3 | Assess customer security posture across a complex enterprise network to Identify security posture shortcomings.",
        description="1.4.3 | Assess customer security posture across a complex enterprise network to Identify security posture shortcomings.  Training Resources & Technical References: Conrad, Misenar, and Feldman, “CISSP Study Guide Third Edition, 2016.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="1.4.4 | Given a vulnerability scan and mission owner network information prioritize vulnerabilities for action.  Trainin",
        description="1.4.4 | Given a vulnerability scan and mission owner network information prioritize vulnerabilities for action.  Training Resources & Technical References: J.M. Couretas, “An Introduction to Cyber Mondeling and Simulation, 2019.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="1.5 | (U) Risk Mitigation & After Action |  |  |  |  |",
        description="1.5 | (U) Risk Mitigation & After Action |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="1.5.1 | Describe and display knowledge of the “After Action Report” and all areas needed to complete one.  Training Reso",
        description="1.5.1 | Describe and display knowledge of the “After Action Report” and all areas needed to complete one.  Training Resources & Technical References: PHF, “After Action Report Tool”,  t_Tool.aspx |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="1.5.2 | Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events relat",
        description="1.5.2 | Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events related to a compromise and recommend mitigations.  Training Resources & Technical References: MITRE, “Risk Mitigation Planning, Implementation, and Progress Monitoring” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="1.5.3 | Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events relat",
        description="1.5.3 | Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events related to a compromise and recommend mitigations  Training Resources & Technical References: Dmitry Vostokov, “Windows memory dump analysis advanced V2.0, 2017.” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="1.5.4 | Demonstrate familiarity with STIGs on host machines by using any software platform to generate a report for a co",
        description="1.5.4 | Demonstrate familiarity with STIGs on host machines by using any software platform to generate a report for a complex network and follow-up with recommendations.  Training Resources & Technical References: DISA, “Security Readiness Review (SRR).” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="1.5.5 | Discuss the term “Lessons Learned” and how it applies to the CPT life cycle.  Training Resources & Technical Ref",
        description="1.5.5 | Discuss the term “Lessons Learned” and how it applies to the CPT life cycle.  Training Resources & Technical References: Joint Publication 3_12, https:// 12.pdf |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="1.5.6 | Given a scenario, identify steps to recover from a full- network compromise.  Training Resources & Technical Ref",
        description="1.5.6 | Given a scenario, identify steps to recover from a full- network compromise.  Training Resources & Technical References: “Certified Information Systems Security Professional (CISSP).” |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and ex",
        description="Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification. | Module 2.0. (U) In this module, personnel demonstrate the capabilities and skillsets required for proper function and execution of a tool. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final watch-station qualification.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="2.1 | (U) Tools |  |  |  |  |",
        description="2.1 | (U) Tools |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="2.1.1 | Identify PS modules that are helpful for local analysis.  Training Resources & Technical References: ATA Learnii",
        description="2.1.1 | Identify PS modules that are helpful for local analysis.  Training Resources & Technical References: ATA Learniing, “Understanding and Building Powershell Modules”, https://adamtheautomator.com/powershell- modules/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="2.1.2 | Identify PS module that are helpful for remote analysis.  Training Resources & Technical References: ATA Learnii",
        description="2.1.2 | Identify PS module that are helpful for remote analysis.  Training Resources & Technical References: ATA Learniing, “Understanding and Building Powershell Modules”, https://adamtheautomator.com/powershell- modules/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="2.1.3 | Define what an Agent Based Security System is and how it could be advantageous during a mission.  Training Resou",
        description="2.1.3 | Define what an Agent Based Security System is and how it could be advantageous during a mission.  Training Resources & Technical References: EasyTechJunkie, “What is a Host-Based Security System?”, https:// system.htm |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="2.1.4 | Deploy an agent based security system to an enterprise network.  Training Resources & Technical References: Easy",
        description="2.1.4 | Deploy an agent based security system to an enterprise network.  Training Resources & Technical References: EasyTechJunkie, “What is a Host-Based Security System?”, https:// system.htm |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="2.1.5 | Configure and develop rules for CPT host-based agents.  Training Resources & Technical References: Tech Target,",
        description="2.1.5 | Configure and develop rules for CPT host-based agents.  Training Resources & Technical References: Tech Target, “Intrusion Detection System (IDS)”, https://searchsecurity.techtarget.com/definition/intrusion- detection-system |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="2.1.6 | Given the Sysinternals suite identify what the specific capabilities the tools can provide.  Training Resources",
        description="2.1.6 | Given the Sysinternals suite identify what the specific capabilities the tools can provide.  Training Resources & Technical References: Microsoft, “Sysinternals Suite”, https://docs.microsoft.com/en- us/sysinternals/downloads/sysinternals-suite |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="2.1.7 | Given a set of sysmon logs identify malicious process creation.  Training Resources & Technical References: JPCE",
        description="2.1.7 | Given a set of sysmon logs identify malicious process creation.  Training Resources & Technical References: JPCERT, “Sysmon search”, |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the",
        description="Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification. | Module 3.0. (U) In this module, personnel demonstrate gained knowledge. It allows practice of the tasks required for the watch-station and to handle abnormal conditions. Before starting the assigned tasks, the prerequisites that pertain to the performance of that particular task must be completed. Satisfactory completion of all prerequisites is required prior to achievement of final qualification.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="3.1 | (U) Demonstration |  |  |  |  |",
        description="3.1 | (U) Demonstration |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="3.1.1 | Detect adversary modification of the following:  bash_profile bashrc  Training Resources & Technical References:",
        description="3.1.1 | Detect adversary modification of the following:  bash_profile bashrc  Training Resources & Technical References: MITRE, “Event Triggered Execution: Unix Shell Configuration Modification”, https://attack.mitre.org/techniques/T1546/004/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="3.1.2 | Detect adversary addition of user to local administrator group:  Account manipulation Account creation  Training",
        description="3.1.2 | Detect adversary addition of user to local administrator group:  Account manipulation Account creation  Training Resources & Technical References: MITRE, “Account Manipulation”, https://attack.mitre.org/techniques/T1098/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="3.1.3 | Detect adversary addition of root user and sudoer. Root sudoer  Training Resources & Technical References: MITRE",
        description="3.1.3 | Detect adversary addition of root user and sudoer. Root sudoer  Training Resources & Technical References: MITRE, “Privilege Escalation”,  MITRE, “Account Manipulation”, |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="3.1.4 | Detect adversary presence in windows logon and startup scripts.  Training Resources & Technical References: MITR",
        description="3.1.4 | Detect adversary presence in windows logon and startup scripts.  Training Resources & Technical References: MITRE, “Boot or Login Initialization Scripts”, https://attack.mitre.org/techniques/T1037/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="3.1.5 | Detect adversary presence in linux logon and startup scripts.  Training Resources & Technical References: MITRE,",
        description="3.1.5 | Detect adversary presence in linux logon and startup scripts.  Training Resources & Technical References: MITRE, “Boot or Login Initialization Scripts”, https://attack.mitre.org/techniques/T1037/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="3.1.6 | Detect adversary addition to BITS jobs.  Training Resources & Technical References: MITRE, “BITS Jobs”, https://",
        description="3.1.6 | Detect adversary addition to BITS jobs.  Training Resources & Technical References: MITRE, “BITS Jobs”, https://attack.mitre.org/techniques/T1197/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="3.1.7 | Detect DLL Search Order Hijacking.  Training Resources & Technical References: MITRE, “Hijack Execution Flow: DL",
        description="3.1.7 | Detect DLL Search Order Hijacking.  Training Resources & Technical References: MITRE, “Hijack Execution Flow: DLL Search Order Hijacking”, https://attack.mitre.org/techniques/T1574/001/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="3.1.8 | Detect malicious hidden files and/or directories.  Training Resources & Technical References: MITRE, “Hide Artif",
        description="3.1.8 | Detect malicious hidden files and/or directories.  Training Resources & Technical References: MITRE, “Hide Artifacts: Files and Directories”, https://attack.mitre.org/techniques/T1564/001/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="3.1.9 | Detect the presence of a rootkit.  Training Resources & Technical References: MITRE, “Rootkit”, https://attack.m",
        description="3.1.9 | Detect the presence of a rootkit.  Training Resources & Technical References: MITRE, “Rootkit”, https://attack.mitre.org/techniques/T1014/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="3.1.10 | Detect the presence of a malicious cronjob.  Training Resources & Technical References: MITRE, “Scheduled Task/",
        description="3.1.10 | Detect the presence of a malicious cronjob.  Training Resources & Technical References: MITRE, “Scheduled Task/Job: Cron”, https://attack.mitre.org/techniques/T1053/003/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="3.1.11 | Detect the presence of a malware maintaining persistence through scheduled tasks. Training Resources & Technica",
        description="3.1.11 | Detect the presence of a malware maintaining persistence through scheduled tasks. Training Resources & Technical References: MITRE, “Scheduled Task/Job: Scheduled Task”, ttps://attack.mitre.org/techniques/T1053/005/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="3.1.12 | Detect the presence of malware maintaining persistence through modified services. Training Resources & Technica",
        description="3.1.12 | Detect the presence of malware maintaining persistence through modified services. Training Resources & Technical References: MITRE, “Create or Modify System Processes”, https://attack.mitre.org/techniques/T1543 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="3.1.13 | Detect the adversary changes to PATH variables.  Training Resources & Technical References: MITRE, “Hijack Exec",
        description="3.1.13 | Detect the adversary changes to PATH variables.  Training Resources & Technical References: MITRE, “Hijack Execution Flow: Path Interception by PATH Environment Variable”, https://attack.mitre.org/techniques/T1574/007/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="3.1.14 | Detect the presence of malicious activity using elevated execution permissions from the following methods: Setu",
        description="3.1.14 | Detect the presence of malicious activity using elevated execution permissions from the following methods: Setuid Setgid  Training Resources & Technical References: MITRE, “Abuse Elevation Control Mechanism: Setuid and Setgid”, https://attack.mitre.org/techniques/T1548/001/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="3.1.15 | Detect the use of shortcut modification.  Training Resources & Technical References: MITRE, “Boot or Login Auto",
        description="3.1.15 | Detect the use of shortcut modification.  Training Resources & Technical References: MITRE, “Boot or Login Autostart Execution: Registry Run Keys / Startup Folder”, https://attack.mitre.org/techniques/T1547/009/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="3.1.16 | Detect malicious use of WMI event subscription.  Training Resources & Technical References: MITRE, “Event Trigg",
        description="3.1.16 | Detect malicious use of WMI event subscription.  Training Resources & Technical References: MITRE, “Event Triggered Execution: Windows Management Instrumentation Event Subscription”, https://attack.mitre.org/techniques/T1546/003/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="3.1.17 | Detect the use of data staging and encoding used prior to exfiltration.  Training Resources & Technical Referen",
        description="3.1.17 | Detect the use of data staging and encoding used prior to exfiltration.  Training Resources & Technical References: MITRE, “Data Staged: Local Data Staging”, https://attack.mitre.org/techniques/T1074/001/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="3.1.18 | Detect the exfiltration of data over removable devices.  Training Resources & Technical References: MITRE, “Exf",
        description="3.1.18 | Detect the exfiltration of data over removable devices.  Training Resources & Technical References: MITRE, “Exfiltration Over Physical Medium”, https://attack.mitre.org/techniques/T1052/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="3.1.19 | Demonstrate the ability to search for Indicators of Compromise on a dead disk.  Training Resources & Technical",
        description="3.1.19 | Demonstrate the ability to search for Indicators of Compromise on a dead disk.  Training Resources & Technical References: CISCO, “Indicators of Compromise and Where to Find Them”, https://blogs.cisco.com/security/indicators-of- compromise-and-where-to-find-them |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="3.1.20 | Triage malware from dead disk and identify the process to get assistance with reverse engineering. Training Res",
        description="3.1.20 | Triage malware from dead disk and identify the process to get assistance with reverse engineering. Training Resources & Technical References: MDPI, “Methods and Tools of Digital Triage in Forensic Context: Survey and Future Directions”, https:// |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="3.1.21 | (U) Detect malware in Memory.  Training Resources & Technical References: Oreilly, “Hunting Malware in Process",
        description="3.1.21 | (U) Detect malware in Memory.  Training Resources & Technical References: Oreilly, “Hunting Malware in Process Memory”, https:// of/9781118824993/c08.xhtml |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="3.1.22 | Discover Files using Alternate Data streams.  Training Resources & Technical References: Malwarebytes, “Introdu",
        description="3.1.22 | Discover Files using Alternate Data streams.  Training Resources & Technical References: Malwarebytes, “Introduction to Alternate Data Streams”, https://blog.malwarebytes.com/101/2015/07/introduction-to- alternate-data-streams/ |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="3.1.23 | Submit tool and capability requirements to resolve mission gaps in accordance with established policies, regula",
        description="3.1.23 | Submit tool and capability requirements to resolve mission gaps in accordance with established policies, regulations, and procedures. Training Resources & Technical References: Microsoft, “Windows Event Log”,   Microsoft, “Task Scheduler for Developers”,   Microsoft, “Registry”, https://docs.microsoft.com/en- us/windows/win32/sysinfo/registry |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    task = Task(
        title="3.1.24 | Evaluate a comprehensive assessment strategy that leverages available information sources, personnel, and syste",
        description="3.1.24 | Evaluate a comprehensive assessment strategy that leverages available information sources, personnel, and systems to address potential vulnerabilities and risk-related practices. Training Resources & Technical References: Microsoft, “Windows Event Log”, https://docs.microsoft.com/en- us/windows/win32/wes/windows-event-log |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=94)
    db.session.add(course_task)

    task = Task(
        title="3.1.25 | Incorporate open source vulnerability assessment tools into a virtual machine for use in a test environment. Tr",
        description="3.1.25 | Incorporate open source vulnerability assessment tools into a virtual machine for use in a test environment. Training Resources & Technical References: Microsoft, “Task Scheduler for Developers”, https://docs.microsoft.com/en-us/windows/win32/taskschd/task- scheduler-start-page |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=95)
    db.session.add(course_task)

    task = Task(
        title="3.2 | (U) Capstones |  |  |  |  |",
        description="3.2 | (U) Capstones |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=96)
    db.session.add(course_task)

    task = Task(
        title="3.2.1 | Given current intelligence and a network map, create a host collection plan.  Training Resources & Technical Ref",
        description="3.2.1 | Given current intelligence and a network map, create a host collection plan.  Training Resources & Technical References: Dragos, “Collection Management Frameworks – Looking Beyond Asset Inventories in Preparation for and Response to Cyber Threats”, https:// content/uploads/CMF_For_ICS.pdf?hsCtaTracking=1b2b0c29 2196-4ebd-a68c-5099dea41ff6%7C27c19e1c-0374-490d-92f9- b9dcf071f9b5 |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=97)
    db.session.add(course_task)

    task = Task(
        title="3.2.2 | Given a scenario and required data, draft or provide input to the host section of a risk mitigation plan.  Train",
        description="3.2.2 | Given a scenario and required data, draft or provide input to the host section of a risk mitigation plan.  Training Resources & Technical References: MITRE, “Risk Mitigation Planning, Implementation, and Progress Monitoring”, https:// guide/acquisition-system-sengineering/risk-management/risk- mitigation-planning-implementation-and-progress-monitoring |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=98)
    db.session.add(course_task)

    db.session.commit()

# === Network Basic Tasks ===
course = Course.query.filter_by(name="Network Basic").first()
if course:
    task = Task(
        title="Task # | Task # | (U) Basic Network Analyst Knowledge | (U) Basic Network Analyst Knowledge | T&R ID | T&R ID | Trainee",
        description="Task # | Task # | (U) Basic Network Analyst Knowledge | (U) Basic Network Analyst Knowledge | T&R ID | T&R ID | Trainee Initials | Trainee Initials | Trainer Initials | Trainer Initials | Trainer Initials | Date Qualified | Date Qualified",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. N",
        description="Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="1.1 | 1.1 | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundame",
        description="1.1 | 1.1 | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="1.1.1 | 1.1.1 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures",
        description="1.1.1 | 1.1.1 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM) Company.  Training Resources & Technical References: CWP 3-33.4 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM) Company.  Training Resources & Technical References: CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="1.1.2 | 1.1.2 | Describe the roles and responsibilities for 3d Network Battalion.  Training Resources & Technical Refere",
        description="1.1.2 | 1.1.2 | Describe the roles and responsibilities for 3d Network Battalion.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the roles and responsibilities for 3d Network Battalion.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="1.1.3 | 1.1.3 | Describe the following mission types: DCO-IDM DODIN Operations Assess Harden Clear Hunt  Training Resour",
        description="1.1.3 | 1.1.3 | Describe the following mission types: DCO-IDM DODIN Operations Assess Harden Clear Hunt  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the following mission types: DCO-IDM DODIN Operations Assess Harden Clear Hunt  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="1.1.4 | 1.1.4 | Explain the structure of a Mission Element and their roles. Team Lead Network Analyst Host Analyst Netwo",
        description="1.1.4 | 1.1.4 | Explain the structure of a Mission Element and their roles. Team Lead Network Analyst Host Analyst Network Technician Intelligence Analyst  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain the structure of a Mission Element and their roles. Team Lead Network Analyst Host Analyst Network Technician Intelligence Analyst  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="1.1.5 | 1.1.5 | Describe relevant policies and procedures governing the DCO-IDM Company.  Training Resources & Technical",
        description="1.1.5 | 1.1.5 | Describe relevant policies and procedures governing the DCO-IDM Company.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information | Describe relevant policies and procedures governing the DCO-IDM Company.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="1.1.6 | 1.1.6 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.  Training Resour",
        description="1.1.6 | 1.1.6 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="1.1.7 | 1.1.7 | (U) Describe the external organizations the Mission Element interfaces with and their importance/signifi",
        description="1.1.7 | 1.1.7 | (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to the mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information | (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to the mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 MAGTF DCO-IDM CoE MCDP 8 - Information |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="1.1.8 | 1.1.8 | Describe the Mission Element Lead responsibilities toward network owner interaction.  Training Resources",
        description="1.1.8 | 1.1.8 | Describe the Mission Element Lead responsibilities toward network owner interaction.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the Mission Element Lead responsibilities toward network owner interaction.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="1.1.9 | 1.1.9 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key s",
        description="1.1.9 | 1.1.9 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeholders.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeholders.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="1.1.10 | 1.1.10 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to c",
        description="1.1.10 | 1.1.10 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrate data collection.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrate data collection.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="1.1.11 | 1.1.11 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.",
        description="1.1.11 | 1.1.11 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="1.1.12 | 1.1.12 | Define Battle Rhythm and discuss why it is useful in preparing for a mission.  Training Resources & Te",
        description="1.1.12 | 1.1.12 | Define Battle Rhythm and discuss why it is useful in preparing for a mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 Joint Publication (JP) 2-01.3: Joint Intelligence Preparation of the Operational Environment (21 May 2014) | Define Battle Rhythm and discuss why it is useful in preparing for a mission.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 Joint Publication (JP) 2-01.3: Joint Intelligence Preparation of the Operational Environment (21 May 2014) |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="1.1.13 | 1.1.13 | Identify and describe information resources at the company to use during mission planning.  Training R",
        description="1.1.13 | 1.1.13 | Identify and describe information resources at the company to use during mission planning.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Identify and describe information resources at the company to use during mission planning.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="1.1.14 | 1.1.14 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.  Training Resources & Te",
        description="1.1.14 | 1.1.14 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.  Training Resources & Technical References: NIST SP 800-30 r1 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.  Training Resources & Technical References: NIST SP 800-30 r1 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="1.1.15 | 1.1.15 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is neces",
        description="1.1.15 | 1.1.15 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="1.1.16 | 1.1.16 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction p",
        description="1.1.16 | 1.1.16 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="1.1.17 | 1.1.17 | Briefing. Explain the importance of an in-brief and what should be included Explain the importance of",
        description="1.1.17 | 1.1.17 | Briefing. Explain the importance of an in-brief and what should be included Explain the importance of an out-brief and what should be included  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Briefing. Explain the importance of an in-brief and what should be included Explain the importance of an out-brief and what should be included  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="1.1.18 | 1.1.18 | Explain the timeline for creating and completing the final report.  Training Resources & Technical Ref",
        description="1.1.18 | 1.1.18 | Explain the timeline for creating and completing the final report.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain the timeline for creating and completing the final report.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="1.1.19 | 1.1.19 | Describe incident response.  Training Resources & Technical References: Joint Publication (JP) 3-12: C",
        description="1.1.19 | 1.1.19 | Describe incident response.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe incident response.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="1.1.20 | 1.1.20 | (U) Describe the purpose of an Equipment Density List (EDL).  Training Resources & Technical Reference",
        description="1.1.20 | 1.1.20 | (U) Describe the purpose of an Equipment Density List (EDL).  Training Resources & Technical References: Local SOP | (U) Describe the purpose of an Equipment Density List (EDL).  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="1.1.21 | 1.1.21 | Explain the purpose and components of a Risk Mitigation Plan.  Training Resources & Technical Referenc",
        description="1.1.21 | 1.1.21 | Explain the purpose and components of a Risk Mitigation Plan.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Explain the purpose and components of a Risk Mitigation Plan.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="1.1.22 | 1.1.22 | Describe priority items or artifacts that may be found in an investigation.  Training Resources & Tech",
        description="1.1.22 | 1.1.22 | Describe priority items or artifacts that may be found in an investigation.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe priority items or artifacts that may be found in an investigation.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="1.1.23 | 1.1.23 | Describe the process in determining the proper mitigations and courses of action for a mission owner.",
        description="1.1.23 | 1.1.23 | Describe the process in determining the proper mitigations and courses of action for a mission owner.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 | Describe the process in determining the proper mitigations and courses of action for a mission owner.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="1.1.24 | 1.1.24 | Discuss the scope and audience of a hot-wash.  Training Resources & Technical References: Joint Public",
        description="1.1.24 | 1.1.24 | Discuss the scope and audience of a hot-wash.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) | Discuss the scope and audience of a hot-wash.  Training Resources & Technical References: Joint Publication (JP) 3-12: Cyberspace Operations (8 June 2018) |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="1.1.25 | 1.1.25 | Explain the importance of the after action review and what should be included.  Training Resources & T",
        description="1.1.25 | 1.1.25 | Explain the importance of the after action review and what should be included.  Training Resources & Technical References: Local SOP | Explain the importance of the after action review and what should be included.  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="1.1.26 | 1.1.26 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission",
        description="1.1.26 | 1.1.26 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.  Training Resources & Technical References: CWP 3-33.4 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.  Training Resources & Technical References: CWP 3-33.4 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="1.1.27 | 1.1.27 | Explain the procedures and required documentation for transporting classified material and what proced",
        description="1.1.27 | 1.1.27 | Explain the procedures and required documentation for transporting classified material and what procedure to follow when passing through airport security.  Training Resources & Technical References: Local SOP | Explain the procedures and required documentation for transporting classified material and what procedure to follow when passing through airport security.  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="1.1.28 | 1.1.28 | (U) Give an example of PKI and the known vulnerabilities in a customer network. | (U) Give an example",
        description="1.1.28 | 1.1.28 | (U) Give an example of PKI and the known vulnerabilities in a customer network. | (U) Give an example of PKI and the known vulnerabilities in a customer network. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="1.1.29 | 1.1.29 | Explain network security implications if the following concepts are poorly implemented: Confidentialit",
        description="1.1.29 | 1.1.29 | Explain network security implications if the following concepts are poorly implemented: Confidentiality Integrity Availability | Explain network security implications if the following concepts are poorly implemented: Confidentiality Integrity Availability |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="1.1.30 | 1.1.30 | (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain th",
        description="1.1.30 | 1.1.30 | (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain the difference between risk and threat as they relate to vulnerabilities. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="1.1.31 | 1.1.31 | Explain network security implications if the following concepts are poorly implemented: Non-repudiatio",
        description="1.1.31 | 1.1.31 | Explain network security implications if the following concepts are poorly implemented: Non-repudiation Authentication Access Control | Explain network security implications if the following concepts are poorly implemented: Non-repudiation Authentication Access Control |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="1.1.32 | 1.1.32 | Explain network security implications associated with implementing Security Technical Implementation G",
        description="1.1.32 | 1.1.32 | Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) | Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="1.1.33 | 1.1.33 | (U) Explain the difference between attributable and non-attributable IP space. | (U) Explain the diffe",
        description="1.1.33 | 1.1.33 | (U) Explain the difference between attributable and non-attributable IP space. | (U) Explain the difference between attributable and non-attributable IP space. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="1.1.34 | 1.1.34 | (U) Describe what constitutes a US Person.  Training Resources & Technical References: USSID SP0018 |",
        description="1.1.34 | 1.1.34 | (U) Describe what constitutes a US Person.  Training Resources & Technical References: USSID SP0018 | (U) Describe what constitutes a US Person.  Training Resources & Technical References: USSID SP0018 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="1.1.35 | 1.1.35 | Explain the following in regards to reports. Delivery Mission owner vulnerabilities Mitigation techniq",
        description="1.1.35 | 1.1.35 | Explain the following in regards to reports. Delivery Mission owner vulnerabilities Mitigation techniques  Training Resources & Technical References: Local SOP | Explain the following in regards to reports. Delivery Mission owner vulnerabilities Mitigation techniques  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="1.1.36 | 1.1.36 | Describe what each of the following DCO-IDM capabilities provide to supported commanders: Discovery an",
        description="1.1.36 | 1.1.36 | Describe what each of the following DCO-IDM capabilities provide to supported commanders: Discovery and Counter Infiltration (D&CI) Threat Mitigation  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” | Describe what each of the following DCO-IDM capabilities provide to supported commanders: Discovery and Counter Infiltration (D&CI) Threat Mitigation  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="1.1.37 | 1.1.37 | As part of a mission, describe the systems that should be evaluated to gain situational awareness of t",
        description="1.1.37 | 1.1.37 | As part of a mission, describe the systems that should be evaluated to gain situational awareness of the mission partner’s network.  Training Resources & Technical References: Local SOP | As part of a mission, describe the systems that should be evaluated to gain situational awareness of the mission partner’s network.  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="1.1.38 | 1.1.38 | Explain the following initial steps that are completed before an evaluation is started: Validate Scope",
        description="1.1.38 | 1.1.38 | Explain the following initial steps that are completed before an evaluation is started: Validate Scope Review Network Design Identify Critical Systems Obtain IP address Scheme Build Exclusion List  Training Resources & Technical References: Local SOP | Explain the following initial steps that are completed before an evaluation is started: Validate Scope Review Network Design Identify Critical Systems Obtain IP address Scheme Build Exclusion List  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="1.1.39 | 1.1.39 | Discuss what a collection plan is. What role network analysts play in the creation of a collection pla",
        description="1.1.39 | 1.1.39 | Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What is the ultimate goal of a collection plan?  Training Resources & Technical References: Local SOP | Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What is the ultimate goal of a collection plan?  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="1.1.40 | 1.1.40 | Explain how the below guidelines can be useful to the Network Analyst. Vendor Security guidance Genera",
        description="1.1.40 | 1.1.40 | Explain how the below guidelines can be useful to the Network Analyst. Vendor Security guidance General best practices DISA Security Technical Implementation Common vulnerabilities and exposures. | Explain how the below guidelines can be useful to the Network Analyst. Vendor Security guidance General best practices DISA Security Technical Implementation Common vulnerabilities and exposures. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="1.1.41 | 1.1.41 | Explain what a SITREP is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, F",
        description="1.1.41 | 1.1.41 | Explain what a SITREP is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” | Explain what a SITREP is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="1.1.42 | 1.1.42 | Explain the following types of orders: FRAGORD OPORD WARNORD EXORD TASKORD  Training Resources & Techn",
        description="1.1.42 | 1.1.42 | Explain the following types of orders: FRAGORD OPORD WARNORD EXORD TASKORD  Training Resources & Technical References: Joint Publication 3-12, “Cyberspace Operations” | Explain the following types of orders: FRAGORD OPORD WARNORD EXORD TASKORD  Training Resources & Technical References: Joint Publication 3-12, “Cyberspace Operations” |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="1.1.43 | 1.1.43 | Explain what “Mission Relevant Key Terrain” (MRT-C) is.  Training Resources & Technical References: CW",
        description="1.1.43 | 1.1.43 | Explain what “Mission Relevant Key Terrain” (MRT-C) is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” | Explain what “Mission Relevant Key Terrain” (MRT-C) is.  Training Resources & Technical References: CWP 3-33.4, “CPT Organization, Functions, and Employment” |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="1.1.44 | 1.1.44 | (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |  |  |  |  |  |",
        description="1.1.44 | 1.1.44 | (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="1.1.45 | 1.1.45 | (U) Walkthrough the layout of MCEN in the INDOPACOM region.  Training Resources & Technical References",
        description="1.1.45 | 1.1.45 | (U) Walkthrough the layout of MCEN in the INDOPACOM region.  Training Resources & Technical References: Introduction to MCEN Course | (U) Walkthrough the layout of MCEN in the INDOPACOM region.  Training Resources & Technical References: Introduction to MCEN Course |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="1.1.46 | 1.1.46 | (U) Explain the difference phases of the operational cycle.  Training Resources & Technical References",
        description="1.1.46 | 1.1.46 | (U) Explain the difference phases of the operational cycle.  Training Resources & Technical References: Local SOP | (U) Explain the difference phases of the operational cycle.  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="1.2 | 1.2 | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fun",
        description="1.2 | 1.2 | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="1.2.1 | 1.2.1 | Describe the following as it relates to Network Address Translation (NAT): One-to-One Dynamic or Pooled",
        description="1.2.1 | 1.2.1 | Describe the following as it relates to Network Address Translation (NAT): One-to-One Dynamic or Pooled Port-Level  Training Resources & Technical References: Arista Edge Threat Management, “1:1 NAT” https://wiki.untangle.com/index.php/1:1_ NAT Techopedia, “Dynamic Network Address Translation (Dynamic NAT)”,  397/dynamic-network-addresstranslation-dynamic-nat | Describe the following as it relates to Network Address Translation (NAT): One-to-One Dynamic or Pooled Port-Level  Training Resources & Technical References: Arista Edge Threat Management, “1:1 NAT” https://wiki.untangle.com/index.php/1:1_ NAT Techopedia, “Dynamic Network Address Translation (Dynamic NAT)”,  397/dynamic-network-addresstranslation-dynamic-nat |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="1.2.2 | 1.2.2 | Explain how encapsulation mismatches on LAN links can affect communication between layers.  Training Res",
        description="1.2.2 | 1.2.2 | Explain how encapsulation mismatches on LAN links can affect communication between layers.  Training Resources & Technical References: Keysight https://jspx?cc=NE&lc=eng&ckey=117535 | Explain how encapsulation mismatches on LAN links can affect communication between layers.  Training Resources & Technical References: Keysight https://jspx?cc=NE&lc=eng&ckey=117535 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="1.2.3 | 1.2.3 | Explain what benefits these network devices provide as secondary network defense systems: Routers Layer-",
        description="1.2.3 | 1.2.3 | Explain what benefits these network devices provide as secondary network defense systems: Routers Layer-3 Switch  Training Resources & Technical References: GIAC.org https:// cpass/102444 FS Community https://community.fs.com/blog/layer-3- switch-vs-router-what-is-your-bestbet.html | Explain what benefits these network devices provide as secondary network defense systems: Routers Layer-3 Switch  Training Resources & Technical References: GIAC.org https:// cpass/102444 FS Community https://community.fs.com/blog/layer-3- switch-vs-router-what-is-your-bestbet.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="1.2.4 | 1.2.4 | Describe the difference between link-state and distance vector routers.  Training Resources & Technical",
        description="1.2.4 | 1.2.4 | Describe the difference between link-state and distance vector routers.  Training Resources & Technical References: CISCO https://community.cisco.com/t5/switchin g/what-different-between- distancevector-and-link-state-routing/td-p/2900912 | Describe the difference between link-state and distance vector routers.  Training Resources & Technical References: CISCO https://community.cisco.com/t5/switchin g/what-different-between- distancevector-and-link-state-routing/td-p/2900912 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="1.2.5 | 1.2.5 | Explain how the following IOS troubleshooting tools can be helpful: The ping Utility Cisco Discovery Pro",
        description="1.2.5 | 1.2.5 | Explain how the following IOS troubleshooting tools can be helpful: The ping Utility Cisco Discovery Protocol (CDP) The ‘Show’ Command Traceroute Debug  Training Resources & Technical References: CISCO https://etworking/troubleshooting/guide/tr1 902.html | Explain how the following IOS troubleshooting tools can be helpful: The ping Utility Cisco Discovery Protocol (CDP) The ‘Show’ Command Traceroute Debug  Training Resources & Technical References: CISCO https://etworking/troubleshooting/guide/tr1 902.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="1.2.6 | 1.2.6 | Describe the most common protocols used for tunneling: PPTP SSH IPSec L2TP  Training Resources & Technic",
        description="1.2.6 | 1.2.6 | Describe the most common protocols used for tunneling: PPTP SSH IPSec L2TP  Training Resources & Technical References: Cactusvpn https:// guide-to-vpn/what-is-pptp/ Techtarget https://searchsecurity.techtarget.com/defi nition/Secure-Shell Techopedia https:// 4842/internet-protocol-security-ipsec | Describe the most common protocols used for tunneling: PPTP SSH IPSec L2TP  Training Resources & Technical References: Cactusvpn https:// guide-to-vpn/what-is-pptp/ Techtarget https://searchsecurity.techtarget.com/defi nition/Secure-Shell Techopedia https:// 4842/internet-protocol-security-ipsec |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="1.2.7 | 1.2.7 | Define and describe some security concerns related to each of the below items: VLANs Port-Mirroring Trun",
        description="1.2.7 | 1.2.7 | Define and describe some security concerns related to each of the below items: VLANs Port-Mirroring Trunking Spanning Tree Protocol  Training Resources & Technical References: Pages02.net  box/newsletter/newsletter_oct2013_articl e1.html Packet Pushers  SANS https:// room/whitepapers/networkdevs/virtual- lansecurity-weaknesses-countermeasures-1090 | Define and describe some security concerns related to each of the below items: VLANs Port-Mirroring Trunking Spanning Tree Protocol  Training Resources & Technical References: Pages02.net  box/newsletter/newsletter_oct2013_articl e1.html Packet Pushers  SANS https:// room/whitepapers/networkdevs/virtual- lansecurity-weaknesses-countermeasures-1090 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="1.2.8 | 1.2.8 | Describe network port security and describe how to implement it.  Training Resources & Technical Referen",
        description="1.2.8 | 1.2.8 | Describe network port security and describe how to implement it.  Training Resources & Technical References: PacketLife  t-security/ | Describe network port security and describe how to implement it.  Training Resources & Technical References: PacketLife  t-security/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="1.2.9 | 1.2.9 | Explain the following in regard to Cisco ACLs: Function Implied last line on an ACL Standard ACL Extende",
        description="1.2.9 | 1.2.9 | Explain the following in regard to Cisco ACLs: Function Implied last line on an ACL Standard ACL Extended ACL  Training Resources & Technical References: Orbit Computer Solutions https://www.orbit-computer- solutions.com/access-control-lists/ | Explain the following in regard to Cisco ACLs: Function Implied last line on an ACL Standard ACL Extended ACL  Training Resources & Technical References: Orbit Computer Solutions https://www.orbit-computer- solutions.com/access-control-lists/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="1.2.10 | 1.2.10 | Define what a packet sniffer is and give two examples of vendor specific packet sniffers.  Training Re",
        description="1.2.10 | 1.2.10 | Define what a packet sniffer is and give two examples of vendor specific packet sniffers.  Training Resources & Technical References: Techpedia https:// 397/dynamic-network- addresstranslation-dynamic-nat | Define what a packet sniffer is and give two examples of vendor specific packet sniffers.  Training Resources & Technical References: Techpedia https:// 397/dynamic-network- addresstranslation-dynamic-nat |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="1.2.11 | 1.2.11 | Describe the use of firewalls, DMZ, and encryption in the MCEN.  Training Resources & Technical Refere",
        description="1.2.11 | 1.2.11 | Describe the use of firewalls, DMZ, and encryption in the MCEN.  Training Resources & Technical References: CISCO https:/ cts/security/firewalls/what-is- afirewall.html TechTarget https://searchsecurity.techtarget.com/defi nition/DMZ TechTarget https://searchsecurity.techtarget.com/defi nition/encryption | Describe the use of firewalls, DMZ, and encryption in the MCEN.  Training Resources & Technical References: CISCO https:/ cts/security/firewalls/what-is- afirewall.html TechTarget https://searchsecurity.techtarget.com/defi nition/DMZ TechTarget https://searchsecurity.techtarget.com/defi nition/encryption |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="1.2.12 | 1.2.12 | (U) Describe the following sections of a switch or router configuration file. Header Chassis Logical S",
        description="1.2.12 | 1.2.12 | (U) Describe the following sections of a switch or router configuration file. Header Chassis Logical Switch  Training Resources & Technical Resources:     Broadcom TechDocs  https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-administration/9-2-x/v26750061/v26749806.html | (U) Describe the following sections of a switch or router configuration file. Header Chassis Logical Switch  Training Resources & Technical Resources:     Broadcom TechDocs  https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-administration/9-2-x/v26750061/v26749806.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="1.2.13 | 1.2.13 | Explain the different privilege levels associated with the following types of  network devices. Cisco",
        description="1.2.13 | 1.2.13 | Explain the different privilege levels associated with the following types of  network devices. Cisco Fortinet NVIDIA Training Resources & Technical References: CISCO https://learningnetwork.cisco.com/docs/ DOC-15878 | Explain the different privilege levels associated with the following types of  network devices. Cisco Fortinet NVIDIA Training Resources & Technical References: CISCO https://learningnetwork.cisco.com/docs/ DOC-15878 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="1.2.14 | 1.2.14 | Describe the difference between the following password hashing/encryptions. MD5 AES128 SHA256 SCRYPT",
        description="1.2.14 | 1.2.14 | Describe the difference between the following password hashing/encryptions. MD5 AES128 SHA256 SCRYPT  Training Resources & Technical References: CISCO https://community.cisco.com/t5/networki ng-documents/understanding-thedifferences-between-the-cisco-password-secret/ta-p/3163238 | Describe the difference between the following password hashing/encryptions. MD5 AES128 SHA256 SCRYPT  Training Resources & Technical References: CISCO https://community.cisco.com/t5/networki ng-documents/understanding-thedifferences-between-the-cisco-password-secret/ta-p/3163238 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="1.2.15 | 1.2.15 | Describe VPN and discuss how they are most often used in a customer network.  Training Resources & Tec",
        description="1.2.15 | 1.2.15 | Describe VPN and discuss how they are most often used in a customer network.  Training Resources & Technical References: Microsoft https://docs.microsoft.com/en- us/previous-versions/windows/it- pro/windows2000-server/bb742566(v=technet.10) | Describe VPN and discuss how they are most often used in a customer network.  Training Resources & Technical References: Microsoft https://docs.microsoft.com/en- us/previous-versions/windows/it- pro/windows2000-server/bb742566(v=technet.10) |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="1.2.16 | 1.2.16 | Describe the components of PKI in an enterprise network environment.  Training Resources & Technical R",
        description="1.2.16 | 1.2.16 | Describe the components of PKI in an enterprise network environment.  Training Resources & Technical References: Networklore https://networklore.com/components-of- pki/ | Describe the components of PKI in an enterprise network environment.  Training Resources & Technical References: Networklore https://networklore.com/components-of- pki/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="1.2.17 | 1.2.17 | Describe what a NetBIOS name is. Compare to a fully qualified domain name (FQDN).  Training Resources",
        description="1.2.17 | 1.2.17 | Describe what a NetBIOS name is. Compare to a fully qualified domain name (FQDN).  Training Resources & Technical References: | Describe what a NetBIOS name is. Compare to a fully qualified domain name (FQDN).  Training Resources & Technical References: |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="1.2.18 | 1.2.18 | (U) Describe the research that can be done on DNS domains using open source tools. | (U) Describe the",
        description="1.2.18 | 1.2.18 | (U) Describe the research that can be done on DNS domains using open source tools. | (U) Describe the research that can be done on DNS domains using open source tools. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="1.2.19 | 1.2.19 | (U) Describe port redirection when dealing with firewalls and ACLs. | (U) Describe port redirection wh",
        description="1.2.19 | 1.2.19 | (U) Describe port redirection when dealing with firewalls and ACLs. | (U) Describe port redirection when dealing with firewalls and ACLs. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="1.2.20 | 1.2.20 | Describe UDP traceroute and the following in regards to it: What OS can use this type of traceroute? R",
        description="1.2.20 | 1.2.20 | Describe UDP traceroute and the following in regards to it: What OS can use this type of traceroute? Relevance to C2 operations  Training Resources & Technical References: HP.com http://ftp.ext.hp.com/pub/hpcp/UDP-ICMP-Traceroutes.pdf | Describe UDP traceroute and the following in regards to it: What OS can use this type of traceroute? Relevance to C2 operations  Training Resources & Technical References: HP.com http://ftp.ext.hp.com/pub/hpcp/UDP-ICMP-Traceroutes.pdf |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="1.2.21 | 1.2.21 | Describe the difference between an unmanaged (isolated) system and a domain joined system.  Training R",
        description="1.2.21 | 1.2.21 | Describe the difference between an unmanaged (isolated) system and a domain joined system.  Training Resources & Technical References: Google.com https://books.google.com/books?id=mBD NBQAAQBAJ&pg=PA407&lpg=PA407&dq=domain+joined+system+vs+unma naged+system&source=bl&ots=6HXE8KJkVl&sig=q14nIy3Eu3B6WpvsDcmcAE_7xHQ&hl=en&sa=X&ved=2ahUKEwia5PLPkvHfAhXoT98KHYifCXEQ6AEwDHoECAEQAQ#v=onepage&q=domain%20joined%20system%20vs%20un managed%20system&f=false | Describe the difference between an unmanaged (isolated) system and a domain joined system.  Training Resources & Technical References: Google.com https://books.google.com/books?id=mBD NBQAAQBAJ&pg=PA407&lpg=PA407&dq=domain+joined+system+vs+unma naged+system&source=bl&ots=6HXE8KJkVl&sig=q14nIy3Eu3B6WpvsDcmcAE_7xHQ&hl=en&sa=X&ved=2ahUKEwia5PLPkvHfAhXoT98KHYifCXEQ6AEwDHoECAEQAQ#v=onepage&q=domain%20joined%20system%20vs%20un managed%20system&f=false |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="1.2.22 | 1.2.22 | Explain how firewalls function: Packet filter Proxy firewall Stateful inspection firewall  Training Re",
        description="1.2.22 | 1.2.22 | Explain how firewalls function: Packet filter Proxy firewall Stateful inspection firewall  Training Resources & Technical References: TechTarget   TechTarget   Techpedia https:// 038/packet-filtering | Explain how firewalls function: Packet filter Proxy firewall Stateful inspection firewall  Training Resources & Technical References: TechTarget   TechTarget   Techpedia https:// 038/packet-filtering |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="1.2.23 | 1.2.23 | Describe the Open Systems Interconnection (OSI) model and list the layers of it. List a network protoc",
        description="1.2.23 | 1.2.23 | Describe the Open Systems Interconnection (OSI) model and list the layers of it. List a network protocol that would be found in each of the layers.  Training Resources & Technical References: Cloudfare https:// lossary/open | Describe the Open Systems Interconnection (OSI) model and list the layers of it. List a network protocol that would be found in each of the layers.  Training Resources & Technical References: Cloudfare https:// lossary/open |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="1.2.24 | 1.2.24 | (U) Explain the difference between routable and non-routable space. | (U) Explain the difference betwe",
        description="1.2.24 | 1.2.24 | (U) Explain the difference between routable and non-routable space. | (U) Explain the difference between routable and non-routable space. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="1.3 | 1.3 | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Anal",
        description="1.3 | 1.3 | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="1.3.1 | 1.3.1 | Describe what ‘Packet Capture’ (PCAP) data is and what information is contained within it.  Training Res",
        description="1.3.1 | 1.3.1 | Describe what ‘Packet Capture’ (PCAP) data is and what information is contained within it.  Training Resources & Technical References: Comparitech https:// | Describe what ‘Packet Capture’ (PCAP) data is and what information is contained within it.  Training Resources & Technical References: Comparitech https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="1.3.2 | 1.3.2 | Describe a potential implementation of Berkley Packet Filters (BPFs) during DCO.  Training Resources & T",
        description="1.3.2 | 1.3.2 | Describe a potential implementation of Berkley Packet Filters (BPFs) during DCO.  Training Resources & Technical References: Biot.com https://biot.com/capstats/bpf.html | Describe a potential implementation of Berkley Packet Filters (BPFs) during DCO.  Training Resources & Technical References: Biot.com https://biot.com/capstats/bpf.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="1.3.3 | 1.3.3 | Describe the purpose of a Request for Comment (RFC). What kinds of information can be found in RFCs?  Tr",
        description="1.3.3 | 1.3.3 | Describe the purpose of a Request for Comment (RFC). What kinds of information can be found in RFCs?  Training Resources & Technical References: Internet Engineering Task Force read | Describe the purpose of a Request for Comment (RFC). What kinds of information can be found in RFCs?  Training Resources & Technical References: Internet Engineering Task Force read |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="1.3.4 | 1.3.4 | Provide a basic description of the fields in an IPv4 /IPv6 header. Version HLEN Type of Service Total Le",
        description="1.3.4 | 1.3.4 | Provide a basic description of the fields in an IPv4 /IPv6 header. Version HLEN Type of Service Total Length Identification Flags Fragment Offset Time to live Protocol Header Checksum Source IP address Destination IP address Option  Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/introduction-and-ipv4-datagram-header/ | Provide a basic description of the fields in an IPv4 /IPv6 header. Version HLEN Type of Service Total Length Identification Flags Fragment Offset Time to live Protocol Header Checksum Source IP address Destination IP address Option  Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/introduction-and-ipv4-datagram-header/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="1.3.5 | 1.3.5 | Provide a basic description of the fields in a TCP header. Source Port Destination Port Sequence Number",
        description="1.3.5 | 1.3.5 | Provide a basic description of the fields in a TCP header. Source Port Destination Port Sequence Number Acknowledgement Number Data Offset Reserved Flags Window  Checksum Urgent Pointer Options  Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/tcp-ip-packet-format/?ref=header_outind | Provide a basic description of the fields in a TCP header. Source Port Destination Port Sequence Number Acknowledgement Number Data Offset Reserved Flags Window  Checksum Urgent Pointer Options  Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/tcp-ip-packet-format/?ref=header_outind |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="1.3.6 | 1.3.6 | Provide a basic description of the fields in an UDP header. Source Port Destination Port Length Cehcksum",
        description="1.3.6 | 1.3.6 | Provide a basic description of the fields in an UDP header. Source Port Destination Port Length Cehcksum Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/user-datagram-protocol-udp/ | Provide a basic description of the fields in an UDP header. Source Port Destination Port Length Cehcksum Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/user-datagram-protocol-udp/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="1.3.7 | 1.3.7 | Provide a basic description of the fields in an ICMP header. Type Code Checksum  Training Resources & Te",
        description="1.3.7 | 1.3.7 | Provide a basic description of the fields in an ICMP header. Type Code Checksum  Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/internet-control-message-protocol-icmp/ | Provide a basic description of the fields in an ICMP header. Type Code Checksum  Training Resources & Technical References: Geeks for Geeks https://www.geeksforgeeks.org/internet-control-message-protocol-icmp/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="1.3.8 | 1.3.8 | Explain what happens when a TCP packet with the SYN flag set arrives at host on a non- listening port.",
        description="1.3.8 | 1.3.8 | Explain what happens when a TCP packet with the SYN flag set arrives at host on a non- listening port.  Describe the interaction when a packet arrives at various destination ports.  Training Resources & Technical References: InformIT  aspx?p=26557&seqNum=5 | Explain what happens when a TCP packet with the SYN flag set arrives at host on a non- listening port.  Describe the interaction when a packet arrives at various destination ports.  Training Resources & Technical References: InformIT  aspx?p=26557&seqNum=5 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="1.3.9 | 1.3.9 | Explain the response to an IP datagram sent to a host that is not available on a valid network.  Trainin",
        description="1.3.9 | 1.3.9 | Explain the response to an IP datagram sent to a host that is not available on a valid network.  Training Resources & Technical References: InformIT  aspx?p=26557&seqNum=5 | Explain the response to an IP datagram sent to a host that is not available on a valid network.  Training Resources & Technical References: InformIT  aspx?p=26557&seqNum=5 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="1.3.10 | 1.3.10 | Explain what happens when a UDP packet arrives on a listening port.  Training Resources & Technical Re",
        description="1.3.10 | 1.3.10 | Explain what happens when a UDP packet arrives on a listening port.  Training Resources & Technical References: InformIT | Explain what happens when a UDP packet arrives on a listening port.  Training Resources & Technical References: InformIT |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="1.3.11 | 1.3.11 | Explain what happens when a UDP packet arrives on a non-listening port.  Training Resources & Technica",
        description="1.3.11 | 1.3.11 | Explain what happens when a UDP packet arrives on a non-listening port.  Training Resources & Technical References: InformIT  aspx?p=26557&seqNum=5 | Explain what happens when a UDP packet arrives on a non-listening port.  Training Resources & Technical References: InformIT  aspx?p=26557&seqNum=5 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="1.3.12 | 1.3.12 | Describe the following fields within an HTTP header: HTTP Header URI URI Variables User Agent HTTP Met",
        description="1.3.12 | 1.3.12 | Describe the following fields within an HTTP header: HTTP Header URI URI Variables User Agent HTTP Method Referrer Status Code  Training Resources & Technical References: Mozilla.org https://developer.mozilla.org/en | Describe the following fields within an HTTP header: HTTP Header URI URI Variables User Agent HTTP Method Referrer Status Code  Training Resources & Technical References: Mozilla.org https://developer.mozilla.org/en |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="1.3.13 | 1.3.13 | Describe the process of identifying anomalous activity and creation of a signature to identify future",
        description="1.3.13 | 1.3.13 | Describe the process of identifying anomalous activity and creation of a signature to identify future instances.  Training Resources & Technical References: Juniper.net https:// en_US/junos/topics/reference/configur ation-statement/security-edit-ip- flags.htm | Describe the process of identifying anomalous activity and creation of a signature to identify future instances.  Training Resources & Technical References: Juniper.net https:// en_US/junos/topics/reference/configur ation-statement/security-edit-ip- flags.htm |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="1.3.14 | 1.3.14 | Explain and describe the following Suricata/Snort IDS rule parameters: Msg Content Nocase offset & dep",
        description="1.3.14 | 1.3.14 | Explain and describe the following Suricata/Snort IDS rule parameters: Msg Content Nocase offset & depth distance & within Pcre Sid Rev flow bits | Explain and describe the following Suricata/Snort IDS rule parameters: Msg Content Nocase offset & depth distance & within Pcre Sid Rev flow bits |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="1.3.15 | 1.3.15 | Explain how the two main types of NIDS differ: Signature-based Heuristic-based  Training Resources & T",
        description="1.3.15 | 1.3.15 | Explain how the two main types of NIDS differ: Signature-based Heuristic-based  Training Resources & Technical References: Electronics Research Group https://erg.abdn.ac.uk/users/gorry/cours e/inet-pages/ip-packet.html Juniper.net https:// en_US/junos/topics/reference/configur ation-statement/security-edit-ip- flags.htm | Explain how the two main types of NIDS differ: Signature-based Heuristic-based  Training Resources & Technical References: Electronics Research Group https://erg.abdn.ac.uk/users/gorry/cours e/inet-pages/ip-packet.html Juniper.net https:// en_US/junos/topics/reference/configur ation-statement/security-edit-ip- flags.htm |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="1.4 | 1.4 | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&",
        description="1.4 | 1.4 | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="1.4.1 | 1.4.1 | (U) Reconnaissance  Training Resources & Technical References: MITRE, “Reconnaissance”, | (U) Reconnaiss",
        description="1.4.1 | 1.4.1 | (U) Reconnaissance  Training Resources & Technical References: MITRE, “Reconnaissance”, | (U) Reconnaissance  Training Resources & Technical References: MITRE, “Reconnaissance”, |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="1.4.2 | 1.4.2 | Resource Development  Training Resources & Technical References: MITRE, “Resource Development”, https://",
        description="1.4.2 | 1.4.2 | Resource Development  Training Resources & Technical References: MITRE, “Resource Development”, https://attack.mitre.org/tactics/TA00432 | Resource Development  Training Resources & Technical References: MITRE, “Resource Development”, https://attack.mitre.org/tactics/TA00432 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    task = Task(
        title="1.4.3 | 1.4.3 | Initial Access  Training Resources & Technical References: MITRE, “ATT&CK Framework”, https://attack.mit",
        description="1.4.3 | 1.4.3 | Initial Access  Training Resources & Technical References: MITRE, “ATT&CK Framework”, https://attack.mitre.org/tactics/TA0001 | Initial Access  Training Resources & Technical References: MITRE, “ATT&CK Framework”, https://attack.mitre.org/tactics/TA0001 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=94)
    db.session.add(course_task)

    task = Task(
        title="1.4.4 | 1.4.4 | Execution  Training Resources & Technical References: MITRE, “Execution”, https://attack.mitre.org/tacti",
        description="1.4.4 | 1.4.4 | Execution  Training Resources & Technical References: MITRE, “Execution”, https://attack.mitre.org/tactics/TA0002 | Execution  Training Resources & Technical References: MITRE, “Execution”, https://attack.mitre.org/tactics/TA0002 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=95)
    db.session.add(course_task)

    task = Task(
        title="1.4.5 | 1.4.5 | Privilege Escalation  Training Resources & Technical References: MITRE, “Privilege Escalation”, https://",
        description="1.4.5 | 1.4.5 | Privilege Escalation  Training Resources & Technical References: MITRE, “Privilege Escalation”, https://attack.mitre.org/tactics/TA0004 | Privilege Escalation  Training Resources & Technical References: MITRE, “Privilege Escalation”, https://attack.mitre.org/tactics/TA0004 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=96)
    db.session.add(course_task)

    task = Task(
        title="1.4.6 | 1.4.6 | Defense Evasion  Training Resources & Technical References: MITRE, “Defense Evasion”, https://attack.mit",
        description="1.4.6 | 1.4.6 | Defense Evasion  Training Resources & Technical References: MITRE, “Defense Evasion”, https://attack.mitre.org/tactics/TA0005 | Defense Evasion  Training Resources & Technical References: MITRE, “Defense Evasion”, https://attack.mitre.org/tactics/TA0005 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=97)
    db.session.add(course_task)

    task = Task(
        title="1.4.7 | 1.4.7 | Credential Access  Training Resources & Technical References: MITRE, “Credential Access”, https://attack",
        description="1.4.7 | 1.4.7 | Credential Access  Training Resources & Technical References: MITRE, “Credential Access”, https://attack.mitre.org/tactics/TA0006 | Credential Access  Training Resources & Technical References: MITRE, “Credential Access”, https://attack.mitre.org/tactics/TA0006 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=98)
    db.session.add(course_task)

    task = Task(
        title="1.4.8 | 1.4.8 | Discovery  Training Resources & Technical References: MITRE, “Discovery”, https://attack.mitre.org/tacti",
        description="1.4.8 | 1.4.8 | Discovery  Training Resources & Technical References: MITRE, “Discovery”, https://attack.mitre.org/tactics/TA0007 | Discovery  Training Resources & Technical References: MITRE, “Discovery”, https://attack.mitre.org/tactics/TA0007 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=99)
    db.session.add(course_task)

    task = Task(
        title="1.4.9 | 1.4.9 | Lateral movement  Training Resources & Technical References: MITRE, “Lateral Movement”, https://attack.m",
        description="1.4.9 | 1.4.9 | Lateral movement  Training Resources & Technical References: MITRE, “Lateral Movement”, https://attack.mitre.org/tactics/TA0008 | Lateral movement  Training Resources & Technical References: MITRE, “Lateral Movement”, https://attack.mitre.org/tactics/TA0008 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=100)
    db.session.add(course_task)

    task = Task(
        title="1.4.10 | 1.4.10 | (U) Collection  Training Resources & Technical References: MITRE, “Collection”, https://attack.mitre.o",
        description="1.4.10 | 1.4.10 | (U) Collection  Training Resources & Technical References: MITRE, “Collection”, https://attack.mitre.org/tactics/TA0009 | (U) Collection  Training Resources & Technical References: MITRE, “Collection”, https://attack.mitre.org/tactics/TA0009 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=101)
    db.session.add(course_task)

    task = Task(
        title="1.4.11 | 1.4.11 | Command and Control  Training Resources & Technical References: MITRE, “Command and Control”, https://",
        description="1.4.11 | 1.4.11 | Command and Control  Training Resources & Technical References: MITRE, “Command and Control”, https://attack.mitre.org/tactics/TA0011 | Command and Control  Training Resources & Technical References: MITRE, “Command and Control”, https://attack.mitre.org/tactics/TA0011 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=102)
    db.session.add(course_task)

    task = Task(
        title="1.4.12 | 1.4.12 | Exfiltration  Training Resources & Technical References: MITRE, “Exfiltration”, https://attack.mitre.o",
        description="1.4.12 | 1.4.12 | Exfiltration  Training Resources & Technical References: MITRE, “Exfiltration”, https://attack.mitre.org/tactics/TA0010 | Exfiltration  Training Resources & Technical References: MITRE, “Exfiltration”, https://attack.mitre.org/tactics/TA0010 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=103)
    db.session.add(course_task)

    task = Task(
        title="1.4.13 | 1.4.13 | Impact  Training Resources & Technical References: MITRE, “Impact”, https://attack.mitre.org/tactics/T",
        description="1.4.13 | 1.4.13 | Impact  Training Resources & Technical References: MITRE, “Impact”, https://attack.mitre.org/tactics/TA0040 | Impact  Training Resources & Technical References: MITRE, “Impact”, https://attack.mitre.org/tactics/TA0040 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=104)
    db.session.add(course_task)

    task = Task(
        title="1.5 | 1.5 | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U)",
        description="1.5 | 1.5 | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=105)
    db.session.add(course_task)

    task = Task(
        title="1.5.1 | 1.5.1 | Describe the different features, characteristics and common uses for port scanners.  Training Resources",
        description="1.5.1 | 1.5.1 | Describe the different features, characteristics and common uses for port scanners.  Training Resources & Technical References: NMAP.org https://nmap.org/ | Describe the different features, characteristics and common uses for port scanners.  Training Resources & Technical References: NMAP.org https://nmap.org/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=106)
    db.session.add(course_task)

    task = Task(
        title="1.5.2 | 1.5.2 | (U) Describe protocol tunneling and methods that malicious adversaries can use it. | (U) Describe protoc",
        description="1.5.2 | 1.5.2 | (U) Describe protocol tunneling and methods that malicious adversaries can use it. | (U) Describe protocol tunneling and methods that malicious adversaries can use it. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=107)
    db.session.add(course_task)

    task = Task(
        title="1.5.3 | 1.5.3 | Explain banner grabbing and the information it provides to identify a remote system. Training Resources",
        description="1.5.3 | 1.5.3 | Explain banner grabbing and the information it provides to identify a remote system. Training Resources & Technical References: TechTarget https://whatis.techtarget.com/definition/b anner-grabbing | Explain banner grabbing and the information it provides to identify a remote system. Training Resources & Technical References: TechTarget https://whatis.techtarget.com/definition/b anner-grabbing |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=108)
    db.session.add(course_task)

    task = Task(
        title="1.5.4 | 1.5.4 | Explain what a man-in-the-middle attack is and the basic requirements for it.  Training Resources & Tech",
        description="1.5.4 | 1.5.4 | Explain what a man-in-the-middle attack is and the basic requirements for it.  Training Resources & Technical References: Wikipedia https://en.wikipedia.org/wiki/Man-in-the- middle_attack | Explain what a man-in-the-middle attack is and the basic requirements for it.  Training Resources & Technical References: Wikipedia https://en.wikipedia.org/wiki/Man-in-the- middle_attack |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=109)
    db.session.add(course_task)

    task = Task(
        title="1.5.5 | 1.5.5 | Describe ARP spoofing.  Training Resources & Technical References: Veracode https:// spoofing | Describe",
        description="1.5.5 | 1.5.5 | Describe ARP spoofing.  Training Resources & Technical References: Veracode https:// spoofing | Describe ARP spoofing.  Training Resources & Technical References: Veracode https:// spoofing |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=110)
    db.session.add(course_task)

    task = Task(
        title="1.5.6 | 1.5.6 | Describe the types of data that would be prioritized by APTs during the post-exploitation phase.  Traini",
        description="1.5.6 | 1.5.6 | Describe the types of data that would be prioritized by APTs during the post-exploitation phase.  Training Resources & Technical References: DNV.com https:// seven-phases-of-a-cyber-attack-118270 | Describe the types of data that would be prioritized by APTs during the post-exploitation phase.  Training Resources & Technical References: DNV.com https:// seven-phases-of-a-cyber-attack-118270 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=111)
    db.session.add(course_task)

    task = Task(
        title="1.5.7 | 1.5.7 | (U) Describe techniques adversaries would use to exfiltrate data. | (U) Describe techniques adversaries",
        description="1.5.7 | 1.5.7 | (U) Describe techniques adversaries would use to exfiltrate data. | (U) Describe techniques adversaries would use to exfiltrate data. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=112)
    db.session.add(course_task)

    task = Task(
        title="1.5.8 | 1.5.8 | Describe the information that can be learned when performing different types of scans?  Training Resourc",
        description="1.5.8 | 1.5.8 | Describe the information that can be learned when performing different types of scans?  Training Resources & Technical References: NMAP.org https://nmap.org/book/osdetect- usage.html | Describe the information that can be learned when performing different types of scans?  Training Resources & Technical References: NMAP.org https://nmap.org/book/osdetect- usage.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=113)
    db.session.add(course_task)

    task = Task(
        title="1.5.9 | 1.5.9 | Describe how an insecurely configured DNS server that allows external, untrusted zone transfers could pr",
        description="1.5.9 | 1.5.9 | Describe how an insecurely configured DNS server that allows external, untrusted zone transfers could provide information to an attacker.  Training Resources & Technical References: HackerTarget.com https://hackertarget.com/zone-transfer/ | Describe how an insecurely configured DNS server that allows external, untrusted zone transfers could provide information to an attacker.  Training Resources & Technical References: HackerTarget.com https://hackertarget.com/zone-transfer/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=114)
    db.session.add(course_task)

    task = Task(
        title="1.5.10 | 1.5.10 | (U) Describe remote access methods and technologies. | (U) Describe remote access methods and technolo",
        description="1.5.10 | 1.5.10 | (U) Describe remote access methods and technologies. | (U) Describe remote access methods and technologies. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=115)
    db.session.add(course_task)

    task = Task(
        title="1.5.11 | 1.5.11 | (U) Describe common techniques used by an adversary to gain initial access. | (U) Describe common tech",
        description="1.5.11 | 1.5.11 | (U) Describe common techniques used by an adversary to gain initial access. | (U) Describe common techniques used by an adversary to gain initial access. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=116)
    db.session.add(course_task)

    task = Task(
        title="1.6 | 1.6 | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U)",
        description="1.6 | 1.6 | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=117)
    db.session.add(course_task)

    task = Task(
        title="1.6.1 | 1.6.1 | Describe the following data sources and use cases for each: PCAP IDS Alerts Network Metadata  Training R",
        description="1.6.1 | 1.6.1 | Describe the following data sources and use cases for each: PCAP IDS Alerts Network Metadata  Training Resources & Technical References: CWP 3-33.4, CPT Organization, Functions, and Employment | Describe the following data sources and use cases for each: PCAP IDS Alerts Network Metadata  Training Resources & Technical References: CWP 3-33.4, CPT Organization, Functions, and Employment |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=118)
    db.session.add(course_task)

    task = Task(
        title="1.6.2 | 1.6.2 | Explain the following terms in the context of network analysis. Traffic Analysis Latency and Jitter Anal",
        description="1.6.2 | 1.6.2 | Explain the following terms in the context of network analysis. Traffic Analysis Latency and Jitter Analysis Threat Detection Vulnerability Assessment Network Utilization and Efficiency Fault Identification and Resolution Trend Analysis and Forecasting Compliance and Policy Enforcement Policy Violation Detection Application Usage  Training Resources & Technical References: Cisco “What is Network Analytics” https://www.cisco.com/c/en/us/solutions/analytics/what-is-network-analytics.html#~data-aggregation | Explain the following terms in the context of network analysis. Traffic Analysis Latency and Jitter Analysis Threat Detection Vulnerability Assessment Network Utilization and Efficiency Fault Identification and Resolution Trend Analysis and Forecasting Compliance and Policy Enforcement Policy Violation Detection Application Usage  Training Resources & Technical References: Cisco “What is Network Analytics” https://www.cisco.com/c/en/us/solutions/analytics/what-is-network-analytics.html#~data-aggregation |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=119)
    db.session.add(course_task)

    task = Task(
        title="1.6.3 | 1.6.3 | Explain link analysis and timeline analysis.  Training Resources & Technical References: ShadowDragon ht",
        description="1.6.3 | 1.6.3 | Explain link analysis and timeline analysis.  Training Resources & Technical References: ShadowDragon https://shadowdragon.io/understanding -link-analysis-and-using-it- ininvestigations/ | Explain link analysis and timeline analysis.  Training Resources & Technical References: ShadowDragon https://shadowdragon.io/understanding -link-analysis-and-using-it- ininvestigations/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=120)
    db.session.add(course_task)

    task = Task(
        title="1.6.4 | 1.6.4 | Explain data stacking and counting, as it pertains to analysis.  Training Resources & Technical Referenc",
        description="1.6.4 | 1.6.4 | Explain data stacking and counting, as it pertains to analysis.  Training Resources & Technical References: DataStory https://the.datastory.guide/hc/en-us/articles/4573570013839-Stacking-Data | Explain data stacking and counting, as it pertains to analysis.  Training Resources & Technical References: DataStory https://the.datastory.guide/hc/en-us/articles/4573570013839-Stacking-Data |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=121)
    db.session.add(course_task)

    task = Task(
        title="1.6.5 | 1.6.5 | Explain what a ‘pivot table’ (data summary table) is.  Training Resources & Technical References: Elasti",
        description="1.6.5 | 1.6.5 | Explain what a ‘pivot table’ (data summary table) is.  Training Resources & Technical References: Elastic.co https:// 6.8/data-table.html Splunk.com https:// /splunk- enterprise/features/tabledatasets.html | Explain what a ‘pivot table’ (data summary table) is.  Training Resources & Technical References: Elastic.co https:// 6.8/data-table.html Splunk.com https:// /splunk- enterprise/features/tabledatasets.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=122)
    db.session.add(course_task)

    task = Task(
        title="1.6.6 | 1.6.6 | Explain the following aspects of an analysts workflow: Detection of an IOC Broadening search from a spec",
        description="1.6.6 | 1.6.6 | Explain the following aspects of an analysts workflow: Detection of an IOC Broadening search from a specific instance to look for similar instances Limiting time spent on a specific task Elevating identified information into a tracked event Reporting details to a team lead  Training Resources & Technical References: Local SOP | Explain the following aspects of an analysts workflow: Detection of an IOC Broadening search from a specific instance to look for similar instances Limiting time spent on a specific task Elevating identified information into a tracked event Reporting details to a team lead  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=123)
    db.session.add(course_task)

    task = Task(
        title="1.6.7 | 1.6.7 | (U) Explain what tactics and techniques procedures (TTPs) are. | (U) Explain what tactics and techniques",
        description="1.6.7 | 1.6.7 | (U) Explain what tactics and techniques procedures (TTPs) are. | (U) Explain what tactics and techniques procedures (TTPs) are. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=124)
    db.session.add(course_task)

    task = Task(
        title="1.6.8 | 1.6.8 | (U) Describe the process of converting a technique into an analytic. | (U) Describe the process of conve",
        description="1.6.8 | 1.6.8 | (U) Describe the process of converting a technique into an analytic. | (U) Describe the process of converting a technique into an analytic. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=125)
    db.session.add(course_task)

    task = Task(
        title="1.6.9 | 1.6.9 | (U) Describe the important information to document in analyst notes? | (U) Describe the important inform",
        description="1.6.9 | 1.6.9 | (U) Describe the important information to document in analyst notes? | (U) Describe the important information to document in analyst notes? |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=126)
    db.session.add(course_task)

    task = Task(
        title="1.6.10 | 1.6.10 | Explain the purpose of a Security Incident and Event Management (SIEM) platform.  Training Resources &",
        description="1.6.10 | 1.6.10 | Explain the purpose of a Security Incident and Event Management (SIEM) platform.  Training Resources & Technical References: Varonis.com https:// | Explain the purpose of a Security Incident and Event Management (SIEM) platform.  Training Resources & Technical References: Varonis.com https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=127)
    db.session.add(course_task)

    task = Task(
        title="1.6.11 | 1.6.11 | Explain what a data model is. Explain the Elastic Common Schema and the Common Information Model.  Tra",
        description="1.6.11 | 1.6.11 | Explain what a data model is. Explain the Elastic Common Schema and the Common Information Model.  Training Resources & Technical References: Elastic.co https:// the-elastic-common-schema | Explain what a data model is. Explain the Elastic Common Schema and the Common Information Model.  Training Resources & Technical References: Elastic.co https:// the-elastic-common-schema |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=128)
    db.session.add(course_task)

    task = Task(
        title="1.6.12 | 1.6.12 | Define a filter and the following usages when using Kibana. Network Traffic Filtering Intrusion Detect",
        description="1.6.12 | 1.6.12 | Define a filter and the following usages when using Kibana. Network Traffic Filtering Intrusion Detection / Prevention System Log Data Filtering Email and Web Filtering Endpoint Filtering  Training Resources & Technical References: Elastic.co https:// cketbeat/current/kibana- queriesfilters.html | Define a filter and the following usages when using Kibana. Network Traffic Filtering Intrusion Detection / Prevention System Log Data Filtering Email and Web Filtering Endpoint Filtering  Training Resources & Technical References: Elastic.co https:// cketbeat/current/kibana- queriesfilters.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=129)
    db.session.add(course_task)

    task = Task(
        title="1.6.13 | 1.6.13 | Describe how a SIEM interacts with an index and with data buckets.  Training Resources & Technical Ref",
        description="1.6.13 | 1.6.13 | Describe how a SIEM interacts with an index and with data buckets.  Training Resources & Technical References: Splunk.com https://docs.splunk.com/Documentation /Splunk/8.0.6/Indexer/Bucketsandclust | Describe how a SIEM interacts with an index and with data buckets.  Training Resources & Technical References: Splunk.com https://docs.splunk.com/Documentation /Splunk/8.0.6/Indexer/Bucketsandclust |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=130)
    db.session.add(course_task)

    task = Task(
        title="1.6.14 | 1.6.14 | Explain the purpose of searching and visualizing, dashboards within a SIEM.  Training Resources & Tech",
        description="1.6.14 | 1.6.14 | Explain the purpose of searching and visualizing, dashboards within a SIEM.  Training Resources & Technical References: Logsign.com https://blog.logsign.com/what | Explain the purpose of searching and visualizing, dashboards within a SIEM.  Training Resources & Technical References: Logsign.com https://blog.logsign.com/what |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=131)
    db.session.add(course_task)

    task = Task(
        title="1.6.15 | 1.6.15 | Explain how the following math functions can be applied during network traffic analysis: Sum distinct",
        description="1.6.15 | 1.6.15 | Explain how the following math functions can be applied during network traffic analysis: Sum distinct count average max/min first/last deviation variance percentile  Training Resources & Technical References: Splunk.com https://docs.splunk.com/Documentation /Splunk/8.0.6/SearchReference/Aggrega tefunctions | Explain how the following math functions can be applied during network traffic analysis: Sum distinct count average max/min first/last deviation variance percentile  Training Resources & Technical References: Splunk.com https://docs.splunk.com/Documentation /Splunk/8.0.6/SearchReference/Aggrega tefunctions |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=132)
    db.session.add(course_task)

    task = Task(
        title="1.6.16 | 1.6.16 | Describe visualizations found in your SIEM environment and give examples of how to use each.  Training",
        description="1.6.16 | 1.6.16 | Describe visualizations found in your SIEM environment and give examples of how to use each.  Training Resources & Technical References: Splunk PECL Security Onion PECL | Describe visualizations found in your SIEM environment and give examples of how to use each.  Training Resources & Technical References: Splunk PECL Security Onion PECL |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=133)
    db.session.add(course_task)

    task = Task(
        title="1.6.17 | 1.6.17 | Describe the following terms relating to analytics: False Negative False Positive True Negative True P",
        description="1.6.17 | 1.6.17 | Describe the following terms relating to analytics: False Negative False Positive True Negative True Positive  Training Resources & Technical References: Google Developers https://developers.google.com/machine- learning/crashcourse/classification/true -false- positivenegative#:~:text=Similarly%2C %20a%20true%20negative%20is,incorr ectly%20predicts%20the%20negative% 20class | Describe the following terms relating to analytics: False Negative False Positive True Negative True Positive  Training Resources & Technical References: Google Developers https://developers.google.com/machine- learning/crashcourse/classification/true -false- positivenegative#:~:text=Similarly%2C %20a%20true%20negative%20is,incorr ectly%20predicts%20the%20negative% 20class |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=134)
    db.session.add(course_task)

    task = Task(
        title="1.6.18 | 1.6.18 | In addition to the SIEM environment, describe how the following tools can be used to analyze network d",
        description="1.6.18 | 1.6.18 | In addition to the SIEM environment, describe how the following tools can be used to analyze network data: Hashes (md5, sha1, etc) Compression tools (gzip, tar, etc) Encoding tools (base64)  Training Resources & Technical References: How to Geek https://www.howtogeek.com/67241/htg-explains-what-are-md5-sha-1-hashes-and-how-do-i-check-them/ AnalytixLabs https://www.analytixlabs.co.in/blog/data-compression-technique/ TutorialsPoint https://www.tutorialspoint.com/what-is-base64-encoding Veeam https://www.veeam.com/blog/yara-rules-malware-detection-analysis.html | In addition to the SIEM environment, describe how the following tools can be used to analyze network data: Hashes (md5, sha1, etc) Compression tools (gzip, tar, etc) Encoding tools (base64)  Training Resources & Technical References: How to Geek https://www.howtogeek.com/67241/htg-explains-what-are-md5-sha-1-hashes-and-how-do-i-check-them/ AnalytixLabs https://www.analytixlabs.co.in/blog/data-compression-technique/ TutorialsPoint https://www.tutorialspoint.com/what-is-base64-encoding Veeam https://www.veeam.com/blog/yara-rules-malware-detection-analysis.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=135)
    db.session.add(course_task)

    task = Task(
        title="1.6.19 | 1.6.19 | Describe the relationship between forensic artifact and ‘Indicator of Compromise’.  Training Resources",
        description="1.6.19 | 1.6.19 | Describe the relationship between forensic artifact and ‘Indicator of Compromise’.  Training Resources & Technical References: AttackIQ | Describe the relationship between forensic artifact and ‘Indicator of Compromise’.  Training Resources & Technical References: AttackIQ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=136)
    db.session.add(course_task)

    task = Task(
        title="1.6.20 | 1.6.20 | Discuss the Pyramid of Pain In regards to detection evasion. Describe the difficulty for an adversary",
        description="1.6.20 | 1.6.20 | Discuss the Pyramid of Pain In regards to detection evasion. Describe the difficulty for an adversary to modify a hash, an IP, and a toolkit.  Training Resources & Technical References: AttackIQ https://attackiq.com/2019/06/26/emulati ng-attacker-activities-and-thepyramid- of-pain/ | Discuss the Pyramid of Pain In regards to detection evasion. Describe the difficulty for an adversary to modify a hash, an IP, and a toolkit.  Training Resources & Technical References: AttackIQ https://attackiq.com/2019/06/26/emulati ng-attacker-activities-and-thepyramid- of-pain/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=137)
    db.session.add(course_task)

    task = Task(
        title="1.6.21 | 1.6.21 | Describe a detection method for each level on the Pyramid of Pain.  Training Resources & Technical Ref",
        description="1.6.21 | 1.6.21 | Describe a detection method for each level on the Pyramid of Pain.  Training Resources & Technical References: EC-Council https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/pyramid-pain-threat-detection/ | Describe a detection method for each level on the Pyramid of Pain.  Training Resources & Technical References: EC-Council https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/pyramid-pain-threat-detection/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=138)
    db.session.add(course_task)

    task = Task(
        title="Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. No",
        description="Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Mdule 2.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references will aid you in a self-study program. All references cited for study are selected according to their credibility and availability.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=139)
    db.session.add(course_task)

    task = Task(
        title="2.1 | 2.1 | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Pa",
        description="2.1 | 2.1 | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK)",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=140)
    db.session.add(course_task)

    task = Task(
        title="2.1.1 | 2.1.1 | Explain how to set a collection file size at 500MB and why an analyst might do this.  Training Resources",
        description="2.1.1 | 2.1.1 | Explain how to set a collection file size at 500MB and why an analyst might do this.  Training Resources & Technical References: Wireshark.org https:// tml_chunked/ | Explain how to set a collection file size at 500MB and why an analyst might do this.  Training Resources & Technical References: Wireshark.org https:// tml_chunked/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=141)
    db.session.add(course_task)

    task = Task(
        title="2.1.2 | 2.1.2 | In what ways can traffic be ingested into the software?  Training Resources & Technical References: Wire",
        description="2.1.2 | 2.1.2 | In what ways can traffic be ingested into the software?  Training Resources & Technical References: Wireshark.org https:// html_chunked/ | In what ways can traffic be ingested into the software?  Training Resources & Technical References: Wireshark.org https:// html_chunked/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=142)
    db.session.add(course_task)

    task = Task(
        title="2.1.3 | 2.1.3 | Explain what type of filter Wireshark uses during live collection and identify what the following Wiresh",
        description="2.1.3 | 2.1.3 | Explain what type of filter Wireshark uses during live collection and identify what the following Wireshark queries will look for: ip.addr == 72.123.35.48 && ip.addr !=72.123.35.47 eth.addr == 3C:52:82:54:9E:28 http.request frame contains “.exe” | Explain what type of filter Wireshark uses during live collection and identify what the following Wireshark queries will look for: ip.addr == 72.123.35.48 && ip.addr !=72.123.35.47 eth.addr == 3C:52:82:54:9E:28 http.request frame contains “.exe” |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=143)
    db.session.add(course_task)

    task = Task(
        title="2.1.4 | 2.1.4 | (U) Explain how to extract a file from HTTP traffic. Explain how to extract a file from any protocol.  D",
        description="2.1.4 | 2.1.4 | (U) Explain how to extract a file from HTTP traffic. Explain how to extract a file from any protocol.  Discuss what follow-on steps should be taken. | (U) Explain how to extract a file from HTTP traffic. Explain how to extract a file from any protocol.  Discuss what follow-on steps should be taken. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=144)
    db.session.add(course_task)

    task = Task(
        title="2.1.5 | 2.1.5 | Explain key differences and similarities between TShark and Wireshark, are they both effective traffic a",
        description="2.1.5 | 2.1.5 | Explain key differences and similarities between TShark and Wireshark, are they both effective traffic analysis tools?  Training Resources & Technical References: Wireshark.org https:// | Explain key differences and similarities between TShark and Wireshark, are they both effective traffic analysis tools?  Training Resources & Technical References: Wireshark.org https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=145)
    db.session.add(course_task)

    task = Task(
        title="2.2 | 2.2 | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U)",
        description="2.2 | 2.2 | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=146)
    db.session.add(course_task)

    task = Task(
        title="2.2.1 | 2.2.1 | How does Tcpdump determine which interface to collect from? How can this be adjusted?  Training Resource",
        description="2.2.1 | 2.2.1 | How does Tcpdump determine which interface to collect from? How can this be adjusted?  Training Resources & Technical References: TCPDUMP https:// | How does Tcpdump determine which interface to collect from? How can this be adjusted?  Training Resources & Technical References: TCPDUMP https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=147)
    db.session.add(course_task)

    task = Task(
        title="2.2.2 | 2.2.2 | (U) Which type of expression can be used to specify the packets to be dumped? | (U) Which type of expres",
        description="2.2.2 | 2.2.2 | (U) Which type of expression can be used to specify the packets to be dumped? | (U) Which type of expression can be used to specify the packets to be dumped? |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=148)
    db.session.add(course_task)

    task = Task(
        title="|  | Training Resources & Technical References: TCPDUMP https:// | Training Resources & Technical References: TCPDUMP h",
        description="|  | Training Resources & Technical References: TCPDUMP https:// | Training Resources & Technical References: TCPDUMP https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=149)
    db.session.add(course_task)

    task = Task(
        title="2.2.3 | 2.2.3 | Explain how to write packets to files of a specific size and why an analyst might do this.  Training Res",
        description="2.2.3 | 2.2.3 | Explain how to write packets to files of a specific size and why an analyst might do this.  Training Resources & Technical References: TCPDUMP https:// | Explain how to write packets to files of a specific size and why an analyst might do this.  Training Resources & Technical References: TCPDUMP https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=150)
    db.session.add(course_task)

    task = Task(
        title="2.2.4 | 2.2.4 | Explain what the following Tcpdump options would deliver: tcpdump -i eth0 host 10.10.1.1 tcpdump port 80",
        description="2.2.4 | 2.2.4 | Explain what the following Tcpdump options would deliver: tcpdump -i eth0 host 10.10.1.1 tcpdump port 80 -w capturefile tcpdump -i eth0 -C 10 -w capturefile | Explain what the following Tcpdump options would deliver: tcpdump -i eth0 host 10.10.1.1 tcpdump port 80 -w capturefile tcpdump -i eth0 -C 10 -w capturefile |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=151)
    db.session.add(course_task)

    task = Task(
        title="2.3 | 2.3 | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Anal",
        description="2.3 | 2.3 | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=152)
    db.session.add(course_task)

    task = Task(
        title="2.3.1 | 2.3.1 | Explain how a traffic analyzer differs from full packet capture.  Training Resources & Technical Referen",
        description="2.3.1 | 2.3.1 | Explain how a traffic analyzer differs from full packet capture.  Training Resources & Technical References: Corelight.com https:// | Explain how a traffic analyzer differs from full packet capture.  Training Resources & Technical References: Corelight.com https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=153)
    db.session.add(course_task)

    task = Task(
        title="2.3.2 | 2.3.2 | Explain what relevant log types a traffic analyzer would make and how it would benefit a network analyst",
        description="2.3.2 | 2.3.2 | Explain what relevant log types a traffic analyzer would make and how it would benefit a network analyst. conn.log http.log dns.log files.log weird.log  Training Resources & Technical References: The Zeek Network Security Monitor https:// | Explain what relevant log types a traffic analyzer would make and how it would benefit a network analyst. conn.log http.log dns.log files.log weird.log  Training Resources & Technical References: The Zeek Network Security Monitor https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=154)
    db.session.add(course_task)

    task = Task(
        title="2.3.3 | 2.3.3 | Explain how to extract files with a traffic analyzer.  Training Resources & Technical References: The Ze",
        description="2.3.3 | 2.3.3 | Explain how to extract files with a traffic analyzer.  Training Resources & Technical References: The Zeek Network Security Monitor https:// /frameworks/files/main.bro.html#type - Files::Info | Explain how to extract files with a traffic analyzer.  Training Resources & Technical References: The Zeek Network Security Monitor https:// /frameworks/files/main.bro.html#type - Files::Info |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=155)
    db.session.add(course_task)

    task = Task(
        title="2.3.4 | 2.3.4 | (U) Demonstrate how to view and/or analyze the information gathered by a traffic analyzer. | (U) Demonst",
        description="2.3.4 | 2.3.4 | (U) Demonstrate how to view and/or analyze the information gathered by a traffic analyzer. | (U) Demonstrate how to view and/or analyze the information gathered by a traffic analyzer. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=156)
    db.session.add(course_task)

    task = Task(
        title="2.3.5 | 2.3.5 | In the absence of a visualization tool, what are some ways zeek log can be analyzed?  Training Resources",
        description="2.3.5 | 2.3.5 | In the absence of a visualization tool, what are some ways zeek log can be analyzed?  Training Resources & Technical References: The Zeek Network Security Monitor https:// mponents/bro-aux/README.html | In the absence of a visualization tool, what are some ways zeek log can be analyzed?  Training Resources & Technical References: The Zeek Network Security Monitor https:// mponents/bro-aux/README.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=157)
    db.session.add(course_task)

    task = Task(
        title="2.3.6 | 2.3.6 | (U) Explain how to calculate an MD5 hash using command line tools. What can an analyst do with this info",
        description="2.3.6 | 2.3.6 | (U) Explain how to calculate an MD5 hash using command line tools. What can an analyst do with this information? | (U) Explain how to calculate an MD5 hash using command line tools. What can an analyst do with this information? |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=158)
    db.session.add(course_task)

    task = Task(
        title="2.4 | 2.4 | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis",
        description="2.4 | 2.4 | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=159)
    db.session.add(course_task)

    task = Task(
        title="2.4.1 | 2.4.1 | Describe the following capabilities of Splunk.  Custom Searches Alerts Dashboards and Reports Incident I",
        description="2.4.1 | 2.4.1 | Describe the following capabilities of Splunk.  Custom Searches Alerts Dashboards and Reports Incident Investigations  Training Resources & Technical References: Splunk PECL | Describe the following capabilities of Splunk.  Custom Searches Alerts Dashboards and Reports Incident Investigations  Training Resources & Technical References: Splunk PECL |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=160)
    db.session.add(course_task)

    task = Task(
        title="2.4.2 | 2.4.2 | (U)  Describe the following capabilities of Security Onion.  Network Traffic Configuration Elastic Stack",
        description="2.4.2 | 2.4.2 | (U)  Describe the following capabilities of Security Onion.  Network Traffic Configuration Elastic Stack Alerts Suricata  Training Resources & Technical References: Security Onion PECL | (U)  Describe the following capabilities of Security Onion.  Network Traffic Configuration Elastic Stack Alerts Suricata  Training Resources & Technical References: Security Onion PECL |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=161)
    db.session.add(course_task)

    task = Task(
        title="2.4.3 | 2.4.3 | (U) Describe the following capabilities of Red Seal.  Network Mapping and Topology Visualization Vulnera",
        description="2.4.3 | 2.4.3 | (U) Describe the following capabilities of Red Seal.  Network Mapping and Topology Visualization Vulnerability and Risk Analysis Attack Pathway Simulation  Training Resources & Technical References: Red Seal PECL | (U) Describe the following capabilities of Red Seal.  Network Mapping and Topology Visualization Vulnerability and Risk Analysis Attack Pathway Simulation  Training Resources & Technical References: Red Seal PECL |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=162)
    db.session.add(course_task)

    task = Task(
        title="2.4.4 | 2.4.4 | (U) Describe the following capabilities of Palo Alto.  Firewall Rules Traffic and Threat Log Monitoring",
        description="2.4.4 | 2.4.4 | (U) Describe the following capabilities of Palo Alto.  Firewall Rules Traffic and Threat Log Monitoring Remote Access Tunnels  Training Resources & Technical References: Palo Alto PECL | (U) Describe the following capabilities of Palo Alto.  Firewall Rules Traffic and Threat Log Monitoring Remote Access Tunnels  Training Resources & Technical References: Palo Alto PECL |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=163)
    db.session.add(course_task)

    task = Task(
        title="2.4.5 | 2.4.5 | Describe the following capabilities of Tanium.  Endpoint Visibility Vulnerability and Patch Management T",
        description="2.4.5 | 2.4.5 | Describe the following capabilities of Tanium.  Endpoint Visibility Vulnerability and Patch Management Threat Hunting and Incident Investigation Compliance and Security Policy Remediation   Training Resources & Technical References: Tanium, “TANIUM USER DOCUMENTATION”, | Describe the following capabilities of Tanium.  Endpoint Visibility Vulnerability and Patch Management Threat Hunting and Incident Investigation Compliance and Security Policy Remediation   Training Resources & Technical References: Tanium, “TANIUM USER DOCUMENTATION”, |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=164)
    db.session.add(course_task)

    task = Task(
        title="2.4.6 | 2.4.6 | (U)  Describe the following capabilities of MDE.  Security Alert and Incident Investigation Threat Respo",
        description="2.4.6 | 2.4.6 | (U)  Describe the following capabilities of MDE.  Security Alert and Incident Investigation Threat Response Advanced Queries Data Analysis  Training Resources & Technical References: X | (U)  Describe the following capabilities of MDE.  Security Alert and Incident Investigation Threat Response Advanced Queries Data Analysis  Training Resources & Technical References: X |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=165)
    db.session.add(course_task)

    task = Task(
        title="2.4.7 | 2.4.7 | Describe the following capabilities of HX.  Endpoint Monitoring Endpoint Threat Detection and Investigat",
        description="2.4.7 | 2.4.7 | Describe the following capabilities of HX.  Endpoint Monitoring Endpoint Threat Detection and Investigation Root Cause Analysis Endpoint Isolation  Training Resources & Technical References: HX Class | Describe the following capabilities of HX.  Endpoint Monitoring Endpoint Threat Detection and Investigation Root Cause Analysis Endpoint Isolation  Training Resources & Technical References: HX Class |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=166)
    db.session.add(course_task)

    task = Task(
        title="2.5 | 2.5 | (U) Software | (U) Software |  |  |  |  |  |  |  |  |",
        description="2.5 | 2.5 | (U) Software | (U) Software |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=167)
    db.session.add(course_task)

    task = Task(
        title="2.5.3 | 2.5.3 | Describe the primary functions PowerShell.  Training Resources & Technical References: Microsoft, “Power",
        description="2.5.3 | 2.5.3 | Describe the primary functions PowerShell.  Training Resources & Technical References: Microsoft, “Powershell Documentation”, https://docs.microsoft.com/en-us/powershell/ | Describe the primary functions PowerShell.  Training Resources & Technical References: Microsoft, “Powershell Documentation”, https://docs.microsoft.com/en-us/powershell/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=168)
    db.session.add(course_task)

    task = Task(
        title="2.5.4 | 2.5.4 | Describe the primary functions Sysinternals.  Training Resources & Technical References: Microsoft, “PsE",
        description="2.5.4 | 2.5.4 | Describe the primary functions Sysinternals.  Training Resources & Technical References: Microsoft, “PsExec v2.34”, https://docs.microsoft.com/en  Microsoft, “Autoruns fo4r Windows v14.09”, | Describe the primary functions Sysinternals.  Training Resources & Technical References: Microsoft, “PsExec v2.34”, https://docs.microsoft.com/en  Microsoft, “Autoruns fo4r Windows v14.09”, |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=169)
    db.session.add(course_task)

    task = Task(
        title="2.5.5 | 2.5.5 | (U) Describe the primary functions of windows native tools.  Regedit Certutil Windows Event Viewer Task",
        description="2.5.5 | 2.5.5 | (U) Describe the primary functions of windows native tools.  Regedit Certutil Windows Event Viewer Task Scheduler Netsh Service Control manager  Training Resources & Technical References: Microsoft, “Registry”, https://docs.microsoft.com/en  Microsoft, “certutil”, https://docs.microsoft.com/en- us/windows-server/administration/windows-commands/certutil Microsoft, “Windows Event log”, https://docs.microsoft.com/en-us/windows/win32/wes/windows- event-log Microsoft, “Task Scheduler for developers:, https://docs.microsoft.com/en-us/windows/win32/taskschd/task- scheduler-start-page Microsoft, “Netsh Command Syntax, Contents, and Formatting”, https://docs.microsoft.com/en-us/windows- server/networking/technologies/netsh/netsh-contexts Microsoft, “sc.exe create”, | (U) Describe the primary functions of windows native tools.  Regedit Certutil Windows Event Viewer Task Scheduler Netsh Service Control manager  Training Resources & Technical References: Microsoft, “Registry”, https://docs.microsoft.com/en  Microsoft, “certutil”, https://docs.microsoft.com/en- us/windows-server/administration/windows-commands/certutil Microsoft, “Windows Event log”, https://docs.microsoft.com/en-us/windows/win32/wes/windows- event-log Microsoft, “Task Scheduler for developers:, https://docs.microsoft.com/en-us/windows/win32/taskschd/task- scheduler-start-page Microsoft, “Netsh Command Syntax, Contents, and Formatting”, https://docs.microsoft.com/en-us/windows- server/networking/technologies/netsh/netsh-contexts Microsoft, “sc.exe create”, |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=170)
    db.session.add(course_task)

    task = Task(
        title="Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assi",
        description="Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task. | Module 3.0 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. (U) For the tasks listed below: What are the steps of this procedure? What are the reasons for each step? Maintain notes. Satisfactorily perform or simulate this task.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=171)
    db.session.add(course_task)

    task = Task(
        title="3.1 | 3.1 | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U)",
        description="3.1 | 3.1 | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=172)
    db.session.add(course_task)

    task = Task(
        title="3.1.1 | 3.1.1 | Given a router configuration, review/analyze the following information: Review/analyze networking device",
        description="3.1.1 | 3.1.1 | Given a router configuration, review/analyze the following information: Review/analyze networking device configuration for the following information: Version Interfaces ACLs (Determine what they are meant to do) Static Routes | Given a router configuration, review/analyze the following information: Review/analyze networking device configuration for the following information: Version Interfaces ACLs (Determine what they are meant to do) Static Routes |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=173)
    db.session.add(course_task)

    task = Task(
        title="3.1.2 | 3.1.2 | When given multiple router configurations, perform the following: Generate a network map Identify if any",
        description="3.1.2 | 3.1.2 | When given multiple router configurations, perform the following: Generate a network map Identify if any rogue systems exist on the network | When given multiple router configurations, perform the following: Generate a network map Identify if any rogue systems exist on the network |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=174)
    db.session.add(course_task)

    task = Task(
        title="3.1.3 | 3.1.3 | (U) Demonstrate the ability to analyze a customer’s perimeter defense strategy. | (U) Demonstrate the ab",
        description="3.1.3 | 3.1.3 | (U) Demonstrate the ability to analyze a customer’s perimeter defense strategy. | (U) Demonstrate the ability to analyze a customer’s perimeter defense strategy. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=175)
    db.session.add(course_task)

    task = Task(
        title="3.1.4 | 3.1.4 | Given the results of a ping sweep and port scan, determine the following: Which hosts are online Host op",
        description="3.1.4 | 3.1.4 | Given the results of a ping sweep and port scan, determine the following: Which hosts are online Host operating systems Service versions associated with each port | Given the results of a ping sweep and port scan, determine the following: Which hosts are online Host operating systems Service versions associated with each port |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=176)
    db.session.add(course_task)

    task = Task(
        title="3.1.5 | 3.1.5 | (U) Analyze the results of a UDP traceroute. | (U) Analyze the results of a UDP traceroute. |  |  |  |",
        description="3.1.5 | 3.1.5 | (U) Analyze the results of a UDP traceroute. | (U) Analyze the results of a UDP traceroute. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=177)
    db.session.add(course_task)

    task = Task(
        title="3.2 | 3.2 | (U) Troubleshooting | (U) Troubleshooting |  |  |  |  |  |  |  |  |",
        description="3.2 | 3.2 | (U) Troubleshooting | (U) Troubleshooting |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=178)
    db.session.add(course_task)

    task = Task(
        title="3.2.1 | 3.2.1 | (U) Demonstrate the ability to identify packet loss. | (U) Demonstrate the ability to identify packet lo",
        description="3.2.1 | 3.2.1 | (U) Demonstrate the ability to identify packet loss. | (U) Demonstrate the ability to identify packet loss. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=179)
    db.session.add(course_task)

    task = Task(
        title="3.2.2 | 3.2.2 | (U) Demonstrate the ability to validate traffic collection, both for missing traffic as well as self-col",
        description="3.2.2 | 3.2.2 | (U) Demonstrate the ability to validate traffic collection, both for missing traffic as well as self-collection. | (U) Demonstrate the ability to validate traffic collection, both for missing traffic as well as self-collection. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=180)
    db.session.add(course_task)

    task = Task(
        title="3.2.3 | 3.2.3 | (U) Demonstrate the ability to communicate connection or access issues to the Crew Lead, this includes r",
        description="3.2.3 | 3.2.3 | (U) Demonstrate the ability to communicate connection or access issues to the Crew Lead, this includes recognized data loss. | (U) Demonstrate the ability to communicate connection or access issues to the Crew Lead, this includes recognized data loss. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=181)
    db.session.add(course_task)

    task = Task(
        title="3.2.4 | 3.2.4 | (U) Demonstrate the ability to troubleshoot information missing from within a SIEM environment. | (U) De",
        description="3.2.4 | 3.2.4 | (U) Demonstrate the ability to troubleshoot information missing from within a SIEM environment. | (U) Demonstrate the ability to troubleshoot information missing from within a SIEM environment. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=182)
    db.session.add(course_task)

    task = Task(
        title="3.3 | 3.3 | (U) Performance | (U) Performance |  |  |  |  |  |  |  |  |",
        description="3.3 | 3.3 | (U) Performance | (U) Performance |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=183)
    db.session.add(course_task)

    task = Task(
        title="3.3.1 | 3.3.1 | Given a packet capture, demonstrate the ability to enumerate hosts and collect information about open po",
        description="3.3.1 | 3.3.1 | Given a packet capture, demonstrate the ability to enumerate hosts and collect information about open ports and services.  Training Resources & Technical References: Infosec Institute https://resources.infosecinstitute.com/w hat | Given a packet capture, demonstrate the ability to enumerate hosts and collect information about open ports and services.  Training Resources & Technical References: Infosec Institute https://resources.infosecinstitute.com/w hat |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=184)
    db.session.add(course_task)

    task = Task(
        title="3.3.2 | 3.3.2 | (U) Given a packet capture, demonstrate the ability to analyze individual layers and highlight important",
        description="3.3.2 | 3.3.2 | (U) Given a packet capture, demonstrate the ability to analyze individual layers and highlight important fields in each layer. | (U) Given a packet capture, demonstrate the ability to analyze individual layers and highlight important fields in each layer. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=185)
    db.session.add(course_task)

    task = Task(
        title="3.3.3 | 3.3.3 | Demonstrate the ability to conduct netflow analysis of network traffic.  Training Resources & Technical",
        description="3.3.3 | 3.3.3 | Demonstrate the ability to conduct netflow analysis of network traffic.  Training Resources & Technical References: Computer Science & Engineering at WashU https:// | Demonstrate the ability to conduct netflow analysis of network traffic.  Training Resources & Technical References: Computer Science & Engineering at WashU https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=186)
    db.session.add(course_task)

    task = Task(
        title="3.3.4 | 3.3.4 | Demonstrate the ability to review/analyze the content of the IP routing table.  Training Resources & Tec",
        description="3.3.4 | 3.3.4 | Demonstrate the ability to review/analyze the content of the IP routing table.  Training Resources & Technical References: RootUsers https:// | Demonstrate the ability to review/analyze the content of the IP routing table.  Training Resources & Technical References: RootUsers https:// |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=187)
    db.session.add(course_task)

    task = Task(
        title="3.3.5 | 3.3.5 | Given a packet capture, demonstrate the ability to identify a man-in-the-middle attack.  Training Resour",
        description="3.3.5 | 3.3.5 | Given a packet capture, demonstrate the ability to identify a man-in-the-middle attack.  Training Resources & Technical References: Black Hat https:// /bh | Given a packet capture, demonstrate the ability to identify a man-in-the-middle attack.  Training Resources & Technical References: Black Hat https:// /bh |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=188)
    db.session.add(course_task)

    task = Task(
        title="3.3.6 | 3.3.6 | Given a packet capture, demonstrate the ability to identify ARP spoofing.  Training Resources & Technica",
        description="3.3.6 | 3.3.6 | Given a packet capture, demonstrate the ability to identify ARP spoofing.  Training Resources & Technical References: Semantic Scholar https://pdfs.semanticscholar.org/5694/8 9f513553bd120d8a2831b3bc2e557d6e | Given a packet capture, demonstrate the ability to identify ARP spoofing.  Training Resources & Technical References: Semantic Scholar https://pdfs.semanticscholar.org/5694/8 9f513553bd120d8a2831b3bc2e557d6e |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=189)
    db.session.add(course_task)

    task = Task(
        title="3.3.7 | 3.3.7 | (U) Given a packet capture, identify DNS tunneling using subdomains. | (U) Given a packet capture, ident",
        description="3.3.7 | 3.3.7 | (U) Given a packet capture, identify DNS tunneling using subdomains. | (U) Given a packet capture, identify DNS tunneling using subdomains. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=190)
    db.session.add(course_task)

    task = Task(
        title="3.3.8 | 3.3.8 | (U) Given a packet capture, identify tunneling using encoded DNS TXT record type. | (U) Given a packet c",
        description="3.3.8 | 3.3.8 | (U) Given a packet capture, identify tunneling using encoded DNS TXT record type. | (U) Given a packet capture, identify tunneling using encoded DNS TXT record type. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=191)
    db.session.add(course_task)

    task = Task(
        title="3.3.9 | 3.3.9 | (U) Given a packet capture, identify common types of scans. | (U) Given a packet capture, identify commo",
        description="3.3.9 | 3.3.9 | (U) Given a packet capture, identify common types of scans. | (U) Given a packet capture, identify common types of scans. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=192)
    db.session.add(course_task)

    task = Task(
        title="3.3.10 | 3.3.10 | (U) Given a packet capture, identify an attacker’s initial intrusion vector into a network. | (U) Give",
        description="3.3.10 | 3.3.10 | (U) Given a packet capture, identify an attacker’s initial intrusion vector into a network. | (U) Given a packet capture, identify an attacker’s initial intrusion vector into a network. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=193)
    db.session.add(course_task)

    task = Task(
        title="3.3.11 | 3.3.11 | Given a packet capture, identify the following actions of an attacker: Situational Awareness Lateral M",
        description="3.3.11 | 3.3.11 | Given a packet capture, identify the following actions of an attacker: Situational Awareness Lateral Movement Mounted Shares Data Exfiltration | Given a packet capture, identify the following actions of an attacker: Situational Awareness Lateral Movement Mounted Shares Data Exfiltration |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=194)
    db.session.add(course_task)

    task = Task(
        title="3.3.12 | 3.3.12 | (U) Given a packet capture, identify an adversary attempting to maintain persistence on a network. | (",
        description="3.3.12 | 3.3.12 | (U) Given a packet capture, identify an adversary attempting to maintain persistence on a network. | (U) Given a packet capture, identify an adversary attempting to maintain persistence on a network. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=195)
    db.session.add(course_task)

    task = Task(
        title="3.3.13 | 3.3.13 | Demonstrate the ability to identify anomalous traffic redirection.  Training Resources & Technical Ref",
        description="3.3.13 | 3.3.13 | Demonstrate the ability to identify anomalous traffic redirection.  Training Resources & Technical References: ResearchGate https:// n/224173111_Redirecting | Demonstrate the ability to identify anomalous traffic redirection.  Training Resources & Technical References: ResearchGate https:// n/224173111_Redirecting |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=196)
    db.session.add(course_task)

    task = Task(
        title="3.3.14 | 3.3.14 | Given a packet capture, demonstrate the ability to identify anomalous open ports.  Training Resources",
        description="3.3.14 | 3.3.14 | Given a packet capture, demonstrate the ability to identify anomalous open ports.  Training Resources & Technical References: Infosec Institute https://resources.infosecinstitute.com/w hat | Given a packet capture, demonstrate the ability to identify anomalous open ports.  Training Resources & Technical References: Infosec Institute https://resources.infosecinstitute.com/w hat |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=197)
    db.session.add(course_task)

    task = Task(
        title="3.3.15 | 3.3.15 | Given a packet capture, demonstrate the ability to verify VLAN and proxy information by completing the",
        description="3.3.15 | 3.3.15 | Given a packet capture, demonstrate the ability to verify VLAN and proxy information by completing the below tasking: Display VLAN information Identify VLAN tagging Identify traffic going through a proxy  Training Resources & Technical References: CISCO https://witches/lan/catalyst2960/software/rele | Given a packet capture, demonstrate the ability to verify VLAN and proxy information by completing the below tasking: Display VLAN information Identify VLAN tagging Identify traffic going through a proxy  Training Resources & Technical References: CISCO https://witches/lan/catalyst2960/software/rele |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=198)
    db.session.add(course_task)

    task = Task(
        title="3.3.16 | 3.3.16 | Demonstrate the ability to identify encapsulation types (ex: PPP, Frame Relay, HDLC, CHAP, PAP)  Train",
        description="3.3.16 | 3.3.16 | Demonstrate the ability to identify encapsulation types (ex: PPP, Frame Relay, HDLC, CHAP, PAP)  Training Resources & Technical References: CISCO https:// os/12_2/switch/configuration/guide | Demonstrate the ability to identify encapsulation types (ex: PPP, Frame Relay, HDLC, CHAP, PAP)  Training Resources & Technical References: CISCO https:// os/12_2/switch/configuration/guide |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=199)
    db.session.add(course_task)

    task = Task(
        title="3.3.17 | 3.3.17 | (U) Given a packet capture, demonstrate the ability to provide a detailed summary of events. | (U) Giv",
        description="3.3.17 | 3.3.17 | (U) Given a packet capture, demonstrate the ability to provide a detailed summary of events. | (U) Given a packet capture, demonstrate the ability to provide a detailed summary of events. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=200)
    db.session.add(course_task)

    task = Task(
        title="3.3.18 | 3.3.18 | (U) Provide a situational awareness report to a superior. This should include all relevant technical d",
        description="3.3.18 | 3.3.18 | (U) Provide a situational awareness report to a superior. This should include all relevant technical details expected for a final report. | (U) Provide a situational awareness report to a superior. This should include all relevant technical details expected for a final report. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=201)
    db.session.add(course_task)

    task = Task(
        title="3.3.19 | 3.3.19 | (U) Given a packet capture and a network map, demonstrate the ability to determine the traffic collect",
        description="3.3.19 | 3.3.19 | (U) Given a packet capture and a network map, demonstrate the ability to determine the traffic collection location. | (U) Given a packet capture and a network map, demonstrate the ability to determine the traffic collection location. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=202)
    db.session.add(course_task)

    task = Task(
        title="3.4 | 3.4 | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Networ",
        description="3.4 | 3.4 | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=203)
    db.session.add(course_task)

    task = Task(
        title="3.4.1 | 3.4.1 | (U) Collect raw PCAP using Wireshark. | (U) Collect raw PCAP using Wireshark. |  |  |  |  |  |  |  |  |",
        description="3.4.1 | 3.4.1 | (U) Collect raw PCAP using Wireshark. | (U) Collect raw PCAP using Wireshark. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=204)
    db.session.add(course_task)

    task = Task(
        title="3.4.2 | 3.4.2 | (U) Collect raw PCAP using TCPdump. | (U) Collect raw PCAP using TCPdump. |  |  |  |  |  |  |  |  |",
        description="3.4.2 | 3.4.2 | (U) Collect raw PCAP using TCPdump. | (U) Collect raw PCAP using TCPdump. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=205)
    db.session.add(course_task)

    task = Task(
        title="3.4.3 | 3.4.3 | (U) Extract an executable file from a provided PCAP file. | (U) Extract an executable file from a provid",
        description="3.4.3 | 3.4.3 | (U) Extract an executable file from a provided PCAP file. | (U) Extract an executable file from a provided PCAP file. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=206)
    db.session.add(course_task)

    task = Task(
        title="3.4.4 | 3.4.4 | Demonstrate the ability to perform queries in either Splunk or Kibana, as team appropriate, to detect th",
        description="3.4.4 | 3.4.4 | Demonstrate the ability to perform queries in either Splunk or Kibana, as team appropriate, to detect the following: HTTP traffic to or from a specified host DNS queries above a specified byte size | Demonstrate the ability to perform queries in either Splunk or Kibana, as team appropriate, to detect the following: HTTP traffic to or from a specified host DNS queries above a specified byte size |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=207)
    db.session.add(course_task)

    task = Task(
        title="3.4.5 | 3.4.5 | Demonstrate the ability to create a dashboard in either Splunk or Kibana, as team appropriate, to captur",
        description="3.4.5 | 3.4.5 | Demonstrate the ability to create a dashboard in either Splunk or Kibana, as team appropriate, to capture the following: SMB file paths requested within the last 7 days All domain names requested through DNS within a specified index | Demonstrate the ability to create a dashboard in either Splunk or Kibana, as team appropriate, to capture the following: SMB file paths requested within the last 7 days All domain names requested through DNS within a specified index |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=208)
    db.session.add(course_task)

    task = Task(
        title="3.4.6 | 3.4.6 | (U) Demonstrate the ability to take historical data and generate zeek logs. | (U) Demonstrate the abilit",
        description="3.4.6 | 3.4.6 | (U) Demonstrate the ability to take historical data and generate zeek logs. | (U) Demonstrate the ability to take historical data and generate zeek logs. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=209)
    db.session.add(course_task)

    task = Task(
        title="3.4.7 | 3.4.7 | (U) Demonstrate the ability to extract a suspicious file from network traffic. Provide all relevant info",
        description="3.4.7 | 3.4.7 | (U) Demonstrate the ability to extract a suspicious file from network traffic. Provide all relevant information to supporting CPT elements (host, network, infrastructure, intelligence, planning, and leadership). | (U) Demonstrate the ability to extract a suspicious file from network traffic. Provide all relevant information to supporting CPT elements (host, network, infrastructure, intelligence, planning, and leadership). |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=210)
    db.session.add(course_task)

    task = Task(
        title="3.4.8 | 3.4.8 | Explain/define the following methods/attributes of C2 Beaconing: Protocol used Frequency/Occurrence Jitt",
        description="3.4.8 | 3.4.8 | Explain/define the following methods/attributes of C2 Beaconing: Protocol used Frequency/Occurrence Jitter | Explain/define the following methods/attributes of C2 Beaconing: Protocol used Frequency/Occurrence Jitter |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=211)
    db.session.add(course_task)

    task = Task(
        title="3.4.9 | 3.4.9 | Explain/define the functions provided by each of the following common SCADA components: MODBUS PLC Air-G",
        description="3.4.9 | 3.4.9 | Explain/define the functions provided by each of the following common SCADA components: MODBUS PLC Air-Gap HMI | Explain/define the functions provided by each of the following common SCADA components: MODBUS PLC Air-Gap HMI |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=212)
    db.session.add(course_task)

    task = Task(
        title="3.4.10 | 3.4.10 | Explain/define basic cloud concepts and how they apply to DCO-IDM Companies in general to include the",
        description="3.4.10 | 3.4.10 | Explain/define basic cloud concepts and how they apply to DCO-IDM Companies in general to include the following: storage networking | Explain/define basic cloud concepts and how they apply to DCO-IDM Companies in general to include the following: storage networking |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=213)
    db.session.add(course_task)

    task = Task(
        title="Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. N",
        description="Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 4.0 – (U) Covers the basic knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=214)
    db.session.add(course_task)

    task = Task(
        title="4.1 | 4.1 | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure",
        description="4.1 | 4.1 | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=215)
    db.session.add(course_task)

    task = Task(
        title="4.1.1 | 4.1.1 | Explain the function of the following appliances: Hub Switches Non-managed and managed Wireless Access P",
        description="4.1.1 | 4.1.1 | Explain the function of the following appliances: Hub Switches Non-managed and managed Wireless Access Point Routers Firewall Wireless Router  Training Resources & Technical References: Webopedia    EtherWAN    Linksys   CISCO    CISCO https:// ecurity/firewalls/what-is-afirewall.html#~types-of-firewalls | Explain the function of the following appliances: Hub Switches Non-managed and managed Wireless Access Point Routers Firewall Wireless Router  Training Resources & Technical References: Webopedia    EtherWAN    Linksys   CISCO    CISCO https:// ecurity/firewalls/what-is-afirewall.html#~types-of-firewalls |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=216)
    db.session.add(course_task)

    task = Task(
        title="4.1.2 | 4.1.2 | (U) Explain the following storage concepts and devices: Redundant storage (RAID 1-RAID60) Non-Redundant",
        description="4.1.2 | 4.1.2 | (U) Explain the following storage concepts and devices: Redundant storage (RAID 1-RAID60) Non-Redundant storage (JBOD, RAID 0) onR Controlr  er  TA,  HD) etor tched e A  rainin es & Tal ces: Wea s:wweboa.coTEH/hext=A%20alsed%20e%0al%et  hts:wwthe/feat uremvs- hernet-tches Linksys https:// center/what-is-a-wifi-access-point/ CISCO https:///small- business/resourcecenter/networking/wh at-is-a-router.html#~how-to-choose- small-businessrouters CISCO https:///security/firewalls/what-is- afirewall.html#~types-of-fire | (U) Explain the following storage concepts and devices: Redundant storage (RAID 1-RAID60) Non-Redundant storage (JBOD, RAID 0) onR Controlr  er  TA,  HD) etor tched e A  rainin es & Tal ces: Wea s:wweboa.coTEH/hext=A%20alsed%20e%0al%et  hts:wwthe/feat uremvs- hernet-tches Linksys https:// center/what-is-a-wifi-access-point/ CISCO https:///small- business/resourcecenter/networking/wh at-is-a-router.html#~how-to-choose- small-businessrouters CISCO https:///security/firewalls/what-is- afirewall.html#~types-of-fire |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=217)
    db.session.add(course_task)

    task = Task(
        title="4.2 | 4.2 | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure",
        description="4.2 | 4.2 | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=218)
    db.session.add(course_task)

    task = Task(
        title="4.2.1 | 4.2.1 | (U) For each of the following hardware pieces of the kit, identify and explain the utility for host or n",
        description="4.2.1 | 4.2.1 | (U) For each of the following hardware pieces of the kit, identify and explain the utility for host or network analysis: a)  Baremetal Sensor b)  Virtual Sensor d)  ASA e)  Packet Broker/In-Line Taps f)	Kit Laptops g)  DMSS Kit Switches h)  PFSense Training Resources & Technical References: PCMag https://m/baremetal Techpedia https://7139/virtual Dell.com Content_data CISCO https://community.cisco.com/t5/security Keysight One.pdf Netgate https://e/features.html | (U) For each of the following hardware pieces of the kit, identify and explain the utility for host or network analysis: a)  Baremetal Sensor b)  Virtual Sensor d)  ASA e)  Packet Broker/In-Line Taps f)	Kit Laptops g)  DMSS Kit Switches h)  PFSense Training Resources & Technical References: PCMag https://m/baremetal Techpedia https://7139/virtual Dell.com Content_data CISCO https://community.cisco.com/t5/security Keysight One.pdf Netgate https://e/features.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=219)
    db.session.add(course_task)

    task = Task(
        title="4.3 | 4.3 | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure",
        description="4.3 | 4.3 | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=220)
    db.session.add(course_task)

    task = Task(
        title="4.3.1 | 4.3.1 | (U) Explain the following analyst tools: a)  ACAS b) Cisco ASDM c)  Redseal d) Wireshark Training Resour",
        description="4.3.1 | 4.3.1 | (U) Explain the following analyst tools: a)  ACAS b) Cisco ASDM c)  Redseal d) Wireshark Training Resources & Technical References: DISA  CISCO - RedSeal https:// Wireshark https://tml_chunked/ | (U) Explain the following analyst tools: a)  ACAS b) Cisco ASDM c)  Redseal d) Wireshark Training Resources & Technical References: DISA  CISCO - RedSeal https:// Wireshark https://tml_chunked/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=221)
    db.session.add(course_task)

    task = Task(
        title="4.3.2 | 4.3.2 | Explain the differences between the following OS's and hypervisors: VMWare ESXi VMWare Workstation Docke",
        description="4.3.2 | 4.3.2 | Explain the differences between the following OS's and hypervisors: VMWare ESXi VMWare Workstation Docker Windows Server Red Hat Enterprise Linux  Training Resources & Technical References: VMware https:// and-esx.html VMware https://ts/w tation-pro.html Docker https://docs.docker.com/get-er/ MakeUseOf https:///window-server-different-windows/ Techpedia https:// 5777/red-hat-enterprise-linux-rhel | Explain the differences between the following OS's and hypervisors: VMWare ESXi VMWare Workstation Docker Windows Server Red Hat Enterprise Linux  Training Resources & Technical References: VMware https:// and-esx.html VMware https://ts/w tation-pro.html Docker https://docs.docker.com/get-er/ MakeUseOf https:///window-server-different-windows/ Techpedia https:// 5777/red-hat-enterprise-linux-rhel |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=222)
    db.session.add(course_task)

    task = Task(
        title="4.3.3 | 4.3.3 | (U) Explain the following traffic capture and analysis software: Zeek Stenographer Suricata  Training Re",
        description="4.3.3 | 4.3.3 | (U) Explain the following traffic capture and analysis software: Zeek Stenographer Suricata  Training Resources & Technical References: ntop.org https:// text=PF_RING%20is%20a%20high% 20speed,active%20traffic%20analysis% 0and%20manipulation The Zeek Network Security Monitor https://zeek.org/ GitHub https://github.com/EmersonElectricCo/ GitHub https://github.com/google/stenographer Suricata https://suricata-ids.org/ | (U) Explain the following traffic capture and analysis software: Zeek Stenographer Suricata  Training Resources & Technical References: ntop.org https:// text=PF_RING%20is%20a%20high% 20speed,active%20traffic%20analysis% 0and%20manipulation The Zeek Network Security Monitor https://zeek.org/ GitHub https://github.com/EmersonElectricCo/ GitHub https://github.com/google/stenographer Suricata https://suricata-ids.org/ |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=223)
    db.session.add(course_task)

    task = Task(
        title="4.3.5 | 4.3.5 | Explain the following types of host logs: Auditd Windows Event Log Sysmon Syslog  Training Resources & T",
        description="4.3.5 | 4.3.5 | Explain the following types of host logs: Auditd Windows Event Log Sysmon Syslog  Training Resources & Technical References: Red Hat https://access.redhat.com/documentation/enus/red_hat_enterprise_linux/6/html/ security_guide/secunderstanding_audit_log_files Loggly https:// guide/windows-logging-basics/ Microsoft https://docs.microsoft.com/en- us/sysinternals/downloads/sysmon Paessler https:// slog#:~:text=Syslog%20stands%20for %20System%20Logging,location%20for%20monitoring%20and%20review | Explain the following types of host logs: Auditd Windows Event Log Sysmon Syslog  Training Resources & Technical References: Red Hat https://access.redhat.com/documentation/enus/red_hat_enterprise_linux/6/html/ security_guide/secunderstanding_audit_log_files Loggly https:// guide/windows-logging-basics/ Microsoft https://docs.microsoft.com/en- us/sysinternals/downloads/sysmon Paessler https:// slog#:~:text=Syslog%20stands%20for %20System%20Logging,location%20for%20monitoring%20and%20review |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=224)
    db.session.add(course_task)

    task = Task(
        title="4.3.6 | 4.3.6 | Explain the following SIEM software: Elastic Splunk  Training Resources & Technical References: Elastic.",
        description="4.3.6 | 4.3.6 | Explain the following SIEM software: Elastic Splunk  Training Resources & Technical References: Elastic.co   Edurek https:// architecture/ Apache Kafka https://kafka.apache.org/intro IDM Magazine https://idm.net.au/blog/0011314-nuix- adds-data-analytics-suite | Explain the following SIEM software: Elastic Splunk  Training Resources & Technical References: Elastic.co   Edurek https:// architecture/ Apache Kafka https://kafka.apache.org/intro IDM Magazine https://idm.net.au/blog/0011314-nuix- adds-data-analytics-suite |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=225)
    db.session.add(course_task)

    task = Task(
        title="4.4 | 4.4 | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Networ",
        description="4.4 | 4.4 | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=226)
    db.session.add(course_task)

    task = Task(
        title="4.4.1 | 4.4.1 | Describe in relation to AAA the following: RADIUS TACACS+ Kerberos NTLM  Training Resources & Technical",
        description="4.4.1 | 4.4.1 | Describe in relation to AAA the following: RADIUS TACACS+ Kerberos NTLM  Training Resources & Technical References: NetworkRADIUS https://networkradius.com/doc/3.0.10/c oncepts/introduction/AAA.html CISCO https:// ecurity/asa/asa96/configuration/general / asa-96-general-config/aaa-tacacs.pdf CISCO https:// ecurity/asa/asa98/asdm78/general/asd m78-general-config/aaa-kerberos.pdf CISCO https:// outers/access/4400/feature/guide/isr_40 00_ntlm-authen.html | Describe in relation to AAA the following: RADIUS TACACS+ Kerberos NTLM  Training Resources & Technical References: NetworkRADIUS https://networkradius.com/doc/3.0.10/c oncepts/introduction/AAA.html CISCO https:// ecurity/asa/asa96/configuration/general / asa-96-general-config/aaa-tacacs.pdf CISCO https:// ecurity/asa/asa98/asdm78/general/asd m78-general-config/aaa-kerberos.pdf CISCO https:// outers/access/4400/feature/guide/isr_40 00_ntlm-authen.html |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=227)
    db.session.add(course_task)

    task = Task(
        title="4.4.2 | 4.4.2 | (U) Explain the different firewall types, benefits, and limitations in regards to the kit: Layer 3 and 4",
        description="4.4.2 | 4.4.2 | (U) Explain the different firewall types, benefits, and limitations in regards to the kit: Layer 3 and 4 [ref. a] Layer 7 Firewall/IPS [ref. a] Proxy Firewall [ref. b] Stateful packet inspection firewall [ref. c] NAT/PAT [ref. d, e]  Training Resources & Technical Reference Server Fault https://serverfault.com/questions/ 2/what-does-a-layer-3-4-firewall- dothat-a-layer-7-does-not BullGuard https:// security-center/pc- security/computersecurity- resources/how-proxy-firewalls- work.aspx Webopedia https:// ateful_inspection.html What Is My IP Address https://whatismyipaddress.com/nat#:~:text= Network%20Address%20Translation% 20(NAT)%20is,computers)%20inside% 20a%20private%20network GeeksforGeeks https:// e-between-network-addresstranslation- nat-and-port-address- translationpat/#:~:text=NAT%20stands %20for%20Network%20Address,stands%20for%2 | (U) Explain the different firewall types, benefits, and limitations in regards to the kit: Layer 3 and 4 [ref. a] Layer 7 Firewall/IPS [ref. a] Proxy Firewall [ref. b] Stateful packet inspection firewall [ref. c] NAT/PAT [ref. d, e]  Training Resources & Technical Reference Server Fault https://serverfault.com/questions/ 2/what-does-a-layer-3-4-firewall- dothat-a-layer-7-does-not BullGuard https:// security-center/pc- security/computersecurity- resources/how-proxy-firewalls- work.aspx Webopedia https:// ateful_inspection.html What Is My IP Address https://whatismyipaddress.com/nat#:~:text= Network%20Address%20Translation% 20(NAT)%20is,computers)%20inside% 20a%20private%20network GeeksforGeeks https:// e-between-network-addresstranslation- nat-and-port-address- translationpat/#:~:text=NAT%20stands %20for%20Network%20Address,stands%20for%2 |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=228)
    db.session.add(course_task)

    task = Task(
        title="4.4.3 | What are an IDS and IPS?  Training Resources & Technical References: TechTarget https://searchsecurity.techtarge",
        description="4.4.3 | What are an IDS and IPS?  Training Resources & Technical References: TechTarget https://searchsecurity.techtarget.com/D o-you-need-an-IDS-or-IPS-or-both | What are an IDS and IPS?  Training Resources & Technical References: TechTarget https://searchsecurity.techtarget.com/D o-you-need-an-IDS-or-IPS-or-both |  |  |  |  |  |  |  |  |  | 4.4.4",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=229)
    db.session.add(course_task)

    task = Task(
        title="In relation to the kit, what is network mapping and why do CPTs do it?  Training Resources & Technical References: Local",
        description="In relation to the kit, what is network mapping and why do CPTs do it?  Training Resources & Technical References: Local SOP | In relation to the kit, what is network mapping and why do CPTs do it?  Training Resources & Technical References: Local SOP |  |  |  |  |  |  |  |  |  | 4.4.5 | Describe the most common protocols used for tunneling and which support encryption in relation to the kit: PPTP SSH IPSec L2TP L2F SSL/TLS  Training Resources & Technical References: Lifewire   SSH https:// Cloudflare     Network World https:// 2163334/what-can-l2tp-do-for- yournetwork-.html Techopedia https:// 25886/layer-two-forwarding-l2f CSO Online",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=230)
    db.session.add(course_task)

    task = Task(
        title="Describe the most common protocols used for tunneling and which support encryption in relation to the kit: PPTP SSH IPSe",
        description="Describe the most common protocols used for tunneling and which support encryption in relation to the kit: PPTP SSH IPSec L2TP L2F SSL/TLS  Training Resources & Technical References: Lifewire   SSH https:// Cloudflare     Network World https:// 2163334/what-can-l2tp-do-for- yournetwork-.html Techopedia https:// 25886/layer-two-forwarding-l2f CSO Online |  |  |  |  |  |  |  |  |  | 4.5 | (U) Mission Deployment | (U) Mission Deployment",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=231)
    db.session.add(course_task)

    task = Task(
        title="(U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployme",
        description="(U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | (U) Mission Deployment | 4.5.1 | Describe the power and hardware requirements in order to set up the kit per the following deployment methods: Fly-In Expeditionary Standalone | Describe the power and hardware requirements in order to set up the kit per the following deployment methods: Fly-In Expeditionary Standalone |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=232)
    db.session.add(course_task)

    task = Task(
        title="|  |  |  |  |  |  |  | 4.6 | (U) Performance | (U) Performance | (U) Performance | (U) Performance",
        description="|  |  |  |  |  |  |  | 4.6 | (U) Performance | (U) Performance | (U) Performance | (U) Performance",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=233)
    db.session.add(course_task)

    task = Task(
        title="(U) Performance | (U) Performance | (U) Performance | (U) Performance | (U) Performance | (U) Performance | (U) Performa",
        description="(U) Performance | (U) Performance | (U) Performance | (U) Performance | (U) Performance | (U) Performance | (U) Performance | 4.6.1 | (U) Draw logical data flow diagram explaining each hardware and software component as well as auxiliary components that aid analysts. | (U) Draw logical data flow diagram explaining each hardware and software component as well as auxiliary components that aid analysts. |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=234)
    db.session.add(course_task)

    task = Task(
        title="|  |  |  |  |  | 4.6.2 | (U) Properly plug in and power the physical kit. | (U) Properly plug in and power the physical",
        description="|  |  |  |  |  | 4.6.2 | (U) Properly plug in and power the physical kit. | (U) Properly plug in and power the physical kit. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=235)
    db.session.add(course_task)

    task = Task(
        title="|  |  |  |  | 4.6.3 | (U) Start and verify collection of traffic in Zeek, Suricata, and Stenographer. | (U) Start and v",
        description="|  |  |  |  | 4.6.3 | (U) Start and verify collection of traffic in Zeek, Suricata, and Stenographer. | (U) Start and verify collection of traffic in Zeek, Suricata, and Stenographer. |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=236)
    db.session.add(course_task)

    task = Task(
        title="|  |  |  | 4.6.4 | (U) Start and verify forwarding of logs to Splunk or Elastic. | (U) Start and verify forwarding of l",
        description="|  |  |  | 4.6.4 | (U) Start and verify forwarding of logs to Splunk or Elastic. | (U) Start and verify forwarding of logs to Splunk or Elastic. |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=237)
    db.session.add(course_task)

    task = Task(
        title="|  |  | 4.6.5 | (U) Gracefully shut down sensor and kit components. | (U) Gracefully shut down sensor and kit component",
        description="|  |  | 4.6.5 | (U) Gracefully shut down sensor and kit components. | (U) Gracefully shut down sensor and kit components. |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=238)
    db.session.add(course_task)

    db.session.commit()

# === Network Senior Tasks ===
course = Course.query.filter_by(name="Network Senior").first()
if course:
    task = Task(
        title="Task # | (U) Senior Network Analyst Knowledge | T&R ID | Trainee Initials | Trainer Initials | Date Qualified",
        description="Task # | (U) Senior Network Analyst Knowledge | T&R ID | Trainee Initials | Trainer Initials | Date Qualified",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studi",
        description="Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 1.0. (U) This module covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="1.1 | (U) Vulnerability Assessment/Security Audit | (U) Vulnerability Assessment/Security Audit |  |  |",
        description="1.1 | (U) Vulnerability Assessment/Security Audit | (U) Vulnerability Assessment/Security Audit |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="1.1.1 | Demonstrate formulating a plan or analysis and risk mitigation using the following mission documentation: Scopin",
        description="1.1.1 | Demonstrate formulating a plan or analysis and risk mitigation using the following mission documentation: Scoping document Network map Customer configurations  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="1.1.2 | Identify key cyber terrain which if seized, afford an advantage to an attacker or defender.  Training Resources",
        description="1.1.2 | Identify key cyber terrain which if seized, afford an advantage to an attacker or defender.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="1.1.3 | (U) Identify critical or high-risk accounts that could afford an advantage to an attacker or defender. |  |  |",
        description="1.1.3 | (U) Identify critical or high-risk accounts that could afford an advantage to an attacker or defender. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="1.1.4 | (U) Provide examples of information that is obtained by scanning a customer’s network. Explain the information t",
        description="1.1.4 | (U) Provide examples of information that is obtained by scanning a customer’s network. Explain the information that is obtained from the scan. Each example provided needs a required tool. Identify potential obstacles/considerations that could affect scans.  Training Resources & Technical References: Local SOP Linux For Devices (https:// linux/nmap-) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="1.1.5 | Provide a scan that will produce operating system, version number, and open ports for a number of hosts.  Traini",
        description="1.1.5 | Provide a scan that will produce operating system, version number, and open ports for a number of hosts.  Training Resources & Technical References: Linux For Devices (https:// linux/nmap-) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="1.2 | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconna",
        description="1.2 | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="1.2.1 | Describe the following reconnaissance methods from Mitre ATT&CK, how it could appear in network traffic, and whe",
        description="1.2.1 | Describe the following reconnaissance methods from Mitre ATT&CK, how it could appear in network traffic, and where to look in your tool set: T1247 Acquire OSINT data sets and information. T1251 Obtain domain/IP registration information. T1254 Conduct active scanning. T1261 Enumerate externally facing software applications technologies, languages, and dependencies. T1252 Map network topology. T1397 Spearphishing for Information.  Training Resources & Technical References: MITRE ATT&CK (https://attack.mitre.org/tactics/pre/) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="1.2.2 | Describe the utility of social engineering for reconnaissance.  Training Resources & Technical References: US-CE",
        description="1.2.2 | Describe the utility of social engineering for reconnaissance.  Training Resources & Technical References: US-CERT – CISA (cert.cisa.gov/ncas/tips/ST04 ) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="1.2.3 | Explain what web scraping is, why an attacker would do it, and how it looks in network traffic.  Training Resour",
        description="1.2.3 | Explain what web scraping is, why an attacker would do it, and how it looks in network traffic.  Training Resources & Technical References: Zyte (https:// ) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="1.2.4 | Explain the information attackers could gather from a DNS zone transfer and what would be observable in network",
        description="1.2.4 | Explain the information attackers could gather from a DNS zone transfer and what would be observable in network traffic.  Training Resources & Technical References: Acunetix (https:// s) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="1.3 | (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation | (U) In",
        description="1.3 | (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="1.3.1 | Describe the following initial exploitation methods from Mitre ATT&CK, how it could appear in network traffic, a",
        description="1.3.1 | Describe the following initial exploitation methods from Mitre ATT&CK, how it could appear in network traffic, and where to look in your tool set: T1189 Drive-by Compromise. T1190 Exploit Public-Facing Application. T1133 External Remote Services. T1566. 001 Spearphishing Attachment. T1566. 002 Spearphishing Link.  Training Resources & Technical References: MITRE ATT&CK https://attack.mitre.org/tactics/TA0001/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="1.3.2 | Describe the protocols/services that are most commonly targeted for attacks. (ex: Brute force, etc.).  Training",
        description="1.3.2 | Describe the protocols/services that are most commonly targeted for attacks. (ex: Brute force, etc.).  Training Resources & Technical References: Forcepoint https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="1.3.3 | Explain the following attacks and their indicators. HTTP GET request brute force attack HTTP POST request brute",
        description="1.3.3 | Explain the following attacks and their indicators. HTTP GET request brute force attack HTTP POST request brute force attack Cross site scripting (XSS) reflected attack Cross site scripting (XSS) persistent  Training Resources & Technical References: Guru99 https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="1.3.4 | Identify and explain various adversarial TTPs that are utilized for initial exploitation of networks. (ex: . Wat",
        description="1.3.4 | Identify and explain various adversarial TTPs that are utilized for initial exploitation of networks. (ex: . Watering Hole, URL shortening).  Training Resources & Technical References: MITRE ATT&CK https://attack.mitre.org/techniques/T1189 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="1.4 | (U) Actions on Target | (U) Actions on Target | (U) Actions on Target | (U) Actions on Target | (U) Actions on Tar",
        description="1.4 | (U) Actions on Target | (U) Actions on Target | (U) Actions on Target | (U) Actions on Target | (U) Actions on Target",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="1.4.1 | Give examples of the following actions on target, their purpose, what they may present as in network traffic, an",
        description="1.4.1 | Give examples of the following actions on target, their purpose, what they may present as in network traffic, and what tool you would use to identify them? Command and control Lateral Movement Data Exfiltration Obfuscation Multi-Stage Malware Deployment Persistence  Training Resources & Technical References: MITRE ATT&CK https://attack.mitre.org/matrices/enterprise The Zeek Network Security Monitor https://docs.zeek.org/en/current/script |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="1.4.2 | Explain Windows Remote Management (WinRM), what ports does it uses, and why an attacker would use it. (Unix) Exp",
        description="1.4.2 | Explain Windows Remote Management (WinRM), what ports does it uses, and why an attacker would use it. (Unix) Explain Secure shell , what ports does it uses, and why an attacker would use it  Training Resources & Technical References: https://posts.specterops.io/offensive |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="1.4.3 | Explain SchTasks, what ports it uses, and why an attacker would use it.  Training Resources & Technical Referenc",
        description="1.4.3 | Explain SchTasks, what ports it uses, and why an attacker would use it.  Training Resources & Technical References: https://posts.specterops.io/offensive |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="1.4.4 | Explain Windows Management Instrumentation (WMI), what ports it uses, and why an attacker would use it.  Trainin",
        description="1.4.4 | Explain Windows Management Instrumentation (WMI), what ports it uses, and why an attacker would use it.  Training Resources & Technical References: https://posts.specterops.io/offensive |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="1.4.5 | Explain BITS Job, what ports it uses, and why an attacker would use it.  Training Resources & Technical Referenc",
        description="1.4.5 | Explain BITS Job, what ports it uses, and why an attacker would use it.  Training Resources & Technical References: SANS https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="1.4.6 | Explain domain fronting and how APTs utilize it to hide malicious activity.  Training Resources & Technical Refe",
        description="1.4.6 | Explain domain fronting and how APTs utilize it to hide malicious activity.  Training Resources & Technical References: FireEye https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="1.4.7 | Describe where in a HTTP request an actor can hide C2 and data exfiltration.  Training Resources & Technical Ref",
        description="1.4.7 | Describe where in a HTTP request an actor can hide C2 and data exfiltration.  Training Resources & Technical References: Active Countermeasures https:// og- |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="1.4.8 | Explain regular web connection. Describe anomalous behaviors and the implications.  Training Resources & Technic",
        description="1.4.8 | Explain regular web connection. Describe anomalous behaviors and the implications.  Training Resources & Technical References: TechTarget https://searchnetworking.techtarget.com/de finition/client |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="1.4.9 | Identify types of DNS records, explain vulnerabilities, exploitations, and how it relates to network security. T",
        description="1.4.9 | Identify types of DNS records, explain vulnerabilities, exploitations, and how it relates to network security. Training Resources & Technical References: SANS  room/whitepapers/dns/detecting |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="1.4.10 | Explain how entropy relates to DNS in regards to network analysis? Training Resources & Technical References: U",
        description="1.4.10 | Explain how entropy relates to DNS in regards to network analysis? Training Resources & Technical References: Unit 42. Paloaltonetworks https://unit42.paloaltonetworks.com/dns |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="1.4.11 | (U) Explain how DNS is used for C2 or data exfiltration?  Explain how to identify other DNS C2 items.  Training",
        description="1.4.11 | (U) Explain how DNS is used for C2 or data exfiltration?  Explain how to identify other DNS C2 items.  Training Resources & Technical References: SANS https://   Unit 42. Paloaltonetworks https://unit42.paloaltonetworks.com/dns |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="1.4.12 | Explain what should be evaluated when looking at a customer’s mapped network drives. Training Resources & Techn",
        description="1.4.12 | Explain what should be evaluated when looking at a customer’s mapped network drives. Training Resources & Technical References: Virus Bulletin https:// /2016/12/spreading |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="1.4.13 | Describe which file types, commands, and actions are indicative of SMB lateral movement.  Training Resources &",
        description="1.4.13 | Describe which file types, commands, and actions are indicative of SMB lateral movement.  Training Resources & Technical References: SANS https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="1.4.14 | Explain the functions of the Windows Service Controller and how it can be leveraged remotely over SMB.  Trainin",
        description="1.4.14 | Explain the functions of the Windows Service Controller and how it can be leveraged remotely over SMB.  Training Resources & Technical References: https://posts.specterops.io/offensive |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="1.4.15 | Using network traffic explain how an analyst could find credential attacks or lateral movement: Successful Logo",
        description="1.4.15 | Using network traffic explain how an analyst could find credential attacks or lateral movement: Successful Logon Failed Logon Network Logon  Training Resources & Technical References: Randy Franklin Smith’s Ultimate Window Security https:// securitylog/encyclopedia/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="1.4.16 | Describe adversarial anti-detection methods and how to identify them in network traffic Training Resources & Te",
        description="1.4.16 | Describe adversarial anti-detection methods and how to identify them in network traffic Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="1.4.17 | Explain/define physical and digital ICS/SCADA components/concepts: MODBUS PLC [talks to and runs everything] Ai",
        description="1.4.17 | Explain/define physical and digital ICS/SCADA components/concepts: MODBUS PLC [talks to and runs everything] Air-Gap HMI |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="1.4.18 | (U) Explain/define IOT. |  |  |  |",
        description="1.4.18 | (U) Explain/define IOT. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="1.4.19 | Explain/define following cloud environments: Infrastructure as a service (IaaS) Platform as a service (PaaS) So",
        description="1.4.19 | Explain/define following cloud environments: Infrastructure as a service (IaaS) Platform as a service (PaaS) Software as a service (SaaS) Mobile Backend as a service (MBaaS) Function as a Service (FaaS) |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="1.5 | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of",
        description="1.5 | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="1.5.1 | Discuss what Intel teams can and should provide you as a Network analyst during a mission  Training Resources &",
        description="1.5.1 | Discuss what Intel teams can and should provide you as a Network analyst during a mission  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="1.5.2 | Discuss what Host teams can and should provide you as a Network analyst during a mission Training Resources & Te",
        description="1.5.2 | Discuss what Host teams can and should provide you as a Network analyst during a mission Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="1.5.3 | Discuss what Network Technician teams can and should provide you as a Network analyst during a mission.  Trainin",
        description="1.5.3 | Discuss what Network Technician teams can and should provide you as a Network analyst during a mission.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="1.5.4 | Discuss how in the role of a lead Network analyst you might interface within the CPT leadership structure Traini",
        description="1.5.4 | Discuss how in the role of a lead Network analyst you might interface within the CPT leadership structure Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="1.5.5 | Discuss how in the role of a lead Network analyst you might interface with the customer  Training Resources & Te",
        description="1.5.5 | Discuss how in the role of a lead Network analyst you might interface with the customer  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="1.5.6 | Discuss the circumstances in which you may need to interface with local CI or law enforcement agencies.  Trainin",
        description="1.5.6 | Discuss the circumstances in which you may need to interface with local CI or law enforcement agencies.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="1.5.7 | Identify the JOPP.  Training Resources & Technical References: https://dnnlgwick.blob.core.windows.net/po rtals/",
        description="1.5.7 | Identify the JOPP.  Training Resources & Technical References: https://dnnlgwick.blob.core.windows.net/po rtals/0/NWCDepartments/Joint%20Mili  - |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="1.5.8 | Explain the purpose of the following documents: Executive Order 12333 as amended DOD Directive 5240.1 DODM 5240.",
        description="1.5.8 | Explain the purpose of the following documents: Executive Order 12333 as amended DOD Directive 5240.1 DODM 5240.01 DOD Directive 5148.13 Foreign Intelligence Surveillance Act of 1978 as amended.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="1.5.9 | Explain the 2nd party and 3rd party policies that impact dissemination and where you will find them.  Training R",
        description="1.5.9 | Explain the 2nd party and 3rd party policies that impact dissemination and where you will find them.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="1.5.10 | Explain the difference between Cyberspace authorities and SIGINT authorities.  Training Resources & Technical R",
        description="1.5.10 | Explain the difference between Cyberspace authorities and SIGINT authorities.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="1.6 | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting",
        description="1.6 | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team)",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="1.6.1 | Describe the role of the following Zeek logs during network analysis. Connection Logs Weird Logs DNS Logs HTTP L",
        description="1.6.1 | Describe the role of the following Zeek logs during network analysis. Connection Logs Weird Logs DNS Logs HTTP Logs  Training Resources & Technical References: Cyber Security Insiders https://www.cybersecurity |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="1.6.2 | Which Windows event logs are most relevant to network analysis? Training Resources & Technical References: Stati",
        description="1.6.2 | Which Windows event logs are most relevant to network analysis? Training Resources & Technical References: Static1.squarespace https://static1.squarespace.com/static/5520 92d5e4b0661088167e5c/t/5b8f091c0e |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="1.6.3 | If given a list of IOCs to hunt for, which selectors are most relevant to network analysis? Which selectors are",
        description="1.6.3 | If given a list of IOCs to hunt for, which selectors are most relevant to network analysis? Which selectors are more relevant to host analysis?  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="1.6.4 | During analysis, describe some selectors that, if discovered should be given to host analysts to leverage  Train",
        description="1.6.4 | During analysis, describe some selectors that, if discovered should be given to host analysts to leverage  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="Module 2.0 – (U) Covers the knowledge and principles needed to understand the equipment or duties to be studied. Normall",
        description="Module 2.0 – (U) Covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 2.0 – (U) Covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 2.0 – (U) Covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 2.0 – (U) Covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 2.0 – (U) Covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability. | Module 2.0 – (U) Covers the knowledge and principles needed to understand the equipment or duties to be studied. Normally, this acquired the knowledge required in the Fundamentals section during the school phase of your training. If you have not been to school or if you need a refresher, the references listed will aid you in a self-study program. All references cited for study are selected according to their credibility and availability.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="2.1 | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/",
        description="2.1 | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="2.1.1 | Explain how IDSs are utilized by CPTs.  Training Resources & Technical References: Local SOP |  |  |  |",
        description="2.1.1 | Explain how IDSs are utilized by CPTs.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="2.1.2 | Explain how rules are developed and employed by IDS.  Training Resources & Technical References: Snort Cookbook",
        description="2.1.2 | Explain how rules are developed and employed by IDS.  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="2.1.3 | Explain the different ways to monitor IDS alerts.  Training Resources & Technical References: Snort Cookbook by",
        description="2.1.3 | Explain the different ways to monitor IDS alerts.  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="2.1.4 | Identify the location of IDS logs.  Training Resources & Technical References: Local SOP |  |  |  |",
        description="2.1.4 | Identify the location of IDS logs.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="2.1.5 | Demonstrate or explain how to filter on content in network traffic using an IDS rule. encrypted data hex or ASCI",
        description="2.1.5 | Demonstrate or explain how to filter on content in network traffic using an IDS rule. encrypted data hex or ASCII  Training Resources & Technical References: Stack Overflow https://stackoverflow.com/questions/34770 81/how |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="2.1.6 | Demonstrate how to make a variable and explain how it could be utilized within an IDS.  Training Resources & Tec",
        description="2.1.6 | Demonstrate how to make a variable and explain how it could be utilized within an IDS.  Training Resources & Technical References: Stack Overflow https://stackoverflow.com/questions/34770 81/how |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="2.1.7 | Explain the process of using selectors/IOCs to create relevant signatures on mission.  Training Resources & Tech",
        description="2.1.7 | Explain the process of using selectors/IOCs to create relevant signatures on mission.  Training Resources & Technical References: Snort https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="2.1.8 | Explain the importance of labeling and categorizing rules within an IDS.  Training Resources & Technical Referen",
        description="2.1.8 | Explain the importance of labeling and categorizing rules within an IDS.  Training Resources & Technical References: Lagout.org https://doc.lagout.org/Others/Snort%20for %20Dummies.pdf |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="2.1.9 | Explain considerations that should be taken when tuning an IDS and explain some effective ways to eliminate fals",
        description="2.1.9 | Explain considerations that should be taken when tuning an IDS and explain some effective ways to eliminate false positives. (HDD space, traffic load, collection strategy, relevant/irrelevant traffic, etc.)  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 SANS https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="2.1.10 | How can a network analyst configure $HOME_NET_IPs?  Training Resources & Technical References: Snort Cookbook b",
        description="2.1.10 | How can a network analyst configure $HOME_NET_IPs?  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="2.1.11 | What does the “flow” keyword do and why would an analyst use it?  Training Resources & Technical References: Sn",
        description="2.1.11 | What does the “flow” keyword do and why would an analyst use it?  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="2.1.12 | Explain the purpose of each of the following rules. alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS (m",
        description="2.1.12 | Explain the purpose of each of the following rules. alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS (msg:\"Figure me out\"; flow:to_server,established; content:\"cmd.exe\"; nocase; classtype:web- application-attack; sid:1002000909; rev:6;) alert tcp !$SMTP_SERVERS any -> !$SMTP_SERVERS 25 (msg:\"Figure me out\";flags:A+;classtype:policyviolation;si d:1111111111111; rev:1;) alert tcp $HTTP_SERVERS $HTTP_PORTS -> $EXTERNAL_NET any (msg:\"Figure me out\"; flow:from_server, established; content:\"HTTP/1.1 403\"; depth:12; classtype:attempted-recon; sid:120887601; rev:7;)  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="2.1.13 | Explain the process of discovering selectors/IOCs while on mission, and then creating relevant signatures to co",
        description="2.1.13 | Explain the process of discovering selectors/IOCs while on mission, and then creating relevant signatures to combat them.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="2.1.14 | Write a Snort rule using a variable that alerts if IRC ports 6667-7001 are being used.  Training Resources & Te",
        description="2.1.14 | Write a Snort rule using a variable that alerts if IRC ports 6667-7001 are being used.  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="2.1.15 | Write a Snort rule using a variable that alerts on communications to or from badwebsite.com.  Training Resource",
        description="2.1.15 | Write a Snort rule using a variable that alerts on communications to or from badwebsite.com.  Training Resources & Technical References: Snort Cookbook by Babbin, Biles, and Orbaugh; Chapter 3. ISBN: 9780596007911 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="2.2 | (U) SIEM | (U) SIEM | (U) SIEM | (U) SIEM | (U) SIEM",
        description="2.2 | (U) SIEM | (U) SIEM | (U) SIEM | (U) SIEM | (U) SIEM",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="2.2.1 | Write queries to find the following items: Brute force attacks over HTTP A shortened URL redirecting the custome",
        description="2.2.1 | Write queries to find the following items: Brute force attacks over HTTP A shortened URL redirecting the customer to another domain More HTTP POST requests than GET requests More data sent to an IP or domain over HTTP/SSL than received A spike in DNS “A” records. Why would an analyst do this? DNS entropy levels by domain, filtering from highest entropy to lowest DNS entropy levels by subdomain, filtering from highest entropy to lowest  Training Resources & Technical References: Splunk https:// y/hunting |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="2.2.2 | Using Windows logs, identify brute force attacks  Training Resources & Technical References: Splunk https://docs",
        description="2.2.2 | Using Windows logs, identify brute force attacks  Training Resources & Technical References: Splunk https://docs.splunk.com/Documentation/Spl unk/8.0.6/SearchReference/Eval |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="2.2.3 | Using Windows logs, identify lateral movement.  Training Resources & Technical References: Splunk https:// y/spo",
        description="2.2.3 | Using Windows logs, identify lateral movement.  Training Resources & Technical References: Splunk https:// y/spotting movement.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="2.2.4 | Explain the process for importing data into SIEM.  Training Resources & Technical References: Local SOP |  |  |",
        description="2.2.4 | Explain the process for importing data into SIEM.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="2.2.5 | Explain a mission scenario in which you would create a dashboard, and why you would choose those specific querie",
        description="2.2.5 | Explain a mission scenario in which you would create a dashboard, and why you would choose those specific queries.  Training Resources & Technical References: Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="2.3 | (U) PCAP | (U) PCAP | (U) PCAP | (U) PCAP | (U) PCAP",
        description="2.3 | (U) PCAP | (U) PCAP | (U) PCAP | (U) PCAP | (U) PCAP",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="2.3.1 | Create a filter for a subnet.  Training Resources & Technical References: Wireshark https:// pages/wireshark-fil",
        description="2.3.1 | Create a filter for a subnet.  Training Resources & Technical References: Wireshark https:// pages/wireshark-filter.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="2.3.2 | Create a filter to look for a specific URL.  Training Resources & Technical References: Wireshark https:// pages",
        description="2.3.2 | Create a filter to look for a specific URL.  Training Resources & Technical References: Wireshark https:// pages/wireshark-filter.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="2.3.3 | Create a filter that would include multiple TCP ports.  Training Resources & Technical References: Wireshark htt",
        description="2.3.3 | Create a filter that would include multiple TCP ports.  Training Resources & Technical References: Wireshark https:// pages/wireshark-filter.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="2.3.4 | Create a filter for an IP range.  Training Resources & Technical References: Wireshark https:// pages/wireshark-",
        description="2.3.4 | Create a filter for an IP range.  Training Resources & Technical References: Wireshark https:// pages/wireshark-filter.html Wireshark https:// |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="2.3.6 | What's the difference between capture filters and display filters? When would each be used?  Training Resources",
        description="2.3.6 | What's the difference between capture filters and display filters? When would each be used?  Training Resources & Technical References: Packet Pushers https://packetpushers.net/understanding- wireshark- capturefilters/#:~:text=In%20Wireshark% 2C%20there%20are%20capture,analyze% 20specific%20packets%20or%20flows |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="2.3.7 | Create a display filter to find HTTP GET requests. Why would an analyst do this?  Training Resources & Technical",
        description="2.3.7 | Create a display filter to find HTTP GET requests. Why would an analyst do this?  Training Resources & Technical References: Wireshark https:// pages/wireshark-filter.html Mozilla.org https://developer.mozilla.org/en- US/docs/Web/HTTP/Methods |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="2.3.8 | Create a display filter using the membership operator to look for DELETE, CONNECT, HEAD, PUT, or TRACE HTTP meth",
        description="2.3.8 | Create a display filter using the membership operator to look for DELETE, CONNECT, HEAD, PUT, or TRACE HTTP methods. Why would an analyst do this?  Training Resources & Technical References: Wireshark https:// pages/wireshark-filter.html Mozilla.org https://developer.mozilla.org/en- US/docs/Web/HTTP/Methods |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="2.3.9 | Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"not ip.addr eq 192.168.1.10\"?  Traini",
        description="2.3.9 | Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"not ip.addr eq 192.168.1.10\"?  Training Resources & Technical References: Wireshark https:// _chunked/ChWorkBuildDisplayFilterSect ion.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="2.3.10 | Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"!(ip.addr == 192.168.1.10)\"?  Traini",
        description="2.3.10 | Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"!(ip.addr == 192.168.1.10)\"?  Training Resources & Technical References: Wireshark https:// _chunked/ChWorkBuildDisplayFilterSect ion.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="2.3.11 | Is there a difference between display filters \"!(ip.addr == 192.168.1.10)\" and \"not ip.addr eq 192.168.1.10\"?",
        description="2.3.11 | Is there a difference between display filters \"!(ip.addr == 192.168.1.10)\" and \"not ip.addr eq 192.168.1.10\"?  Training Resources & Technical References: Wireshark https:// _chunked/ChWorkBuildDisplayFilterSect ion.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="2.3.12 | Explain how to use PCAP to verify sensor placement.  Training Resources & Technical References: Wireshark https",
        description="2.3.12 | Explain how to use PCAP to verify sensor placement.  Training Resources & Technical References: Wireshark https:// Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="2.3.13 | Explain how to utilize PCAP to validate a customer’s network documentation.  Training Resources & Technical Ref",
        description="2.3.13 | Explain how to utilize PCAP to validate a customer’s network documentation.  Training Resources & Technical References: Wireshark https:// Local SOP |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="2.4 | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools",
        description="2.4 | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="2.4.1 | What is JA3?  Training Resources & Technical References: Github https://github.com/salesforce/ja3 |  |  |  |",
        description="2.4.1 | What is JA3?  Training Resources & Technical References: Github https://github.com/salesforce/ja3 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="2.4.2 | What is JA3S?  Training Resources & Technical References: Github https://github.com/salesforce/ja3 |  |  |  |",
        description="2.4.2 | What is JA3S?  Training Resources & Technical References: Github https://github.com/salesforce/ja3 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    task = Task(
        title="2.4.3 | Describe how JA3 and JA3S create fingerprints.  Training Resources & Technical References: Github https://github",
        description="2.4.3 | Describe how JA3 and JA3S create fingerprints.  Training Resources & Technical References: Github https://github.com/salesforce/ja3 |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=94)
    db.session.add(course_task)

    task = Task(
        title="2.4.4 | Why would a network analyst use JA3?  Training Resources & Technical References: Github https://github.com/sales",
        description="2.4.4 | Why would a network analyst use JA3?  Training Resources & Technical References: Github https://github.com/salesforce/ja3 Splunk https:// y/configuringsplunk.html |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=95)
    db.session.add(course_task)

    task = Task(
        title="2.4.5 | How can https://sslbl.abuse.ch/ be utilized by a network analyst?  Training Resources & Technical References: SS",
        description="2.4.5 | How can https://sslbl.abuse.ch/ be utilized by a network analyst?  Training Resources & Technical References: SSL Blacklist https://sslbl.abuse.ch/ja3-fingerprints/ |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=96)
    db.session.add(course_task)

    task = Task(
        title="Module 3 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assign",
        description="Module 3 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. | Module 3 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. | Module 3 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. | Module 3 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. | Module 3 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification. | Module 3 – (U) For optimum training effectiveness, the following items should be completed prior to starting your assigned tasks but shall be completed prior to final qualification.",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=97)
    db.session.add(course_task)

    task = Task(
        title="3.1 | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement",
        description="3.1 | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=98)
    db.session.add(course_task)

    task = Task(
        title="3.1.1 | (U) Demonstrate the ability to develop a sensor placement strategy based on a scoping document, and a provided n",
        description="3.1.1 | (U) Demonstrate the ability to develop a sensor placement strategy based on a scoping document, and a provided network map. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=99)
    db.session.add(course_task)

    task = Task(
        title="3.1.2 | (U) Demonstrate the ability to develop a sensor placement strategy based on knowledge gaps in traffic results. |",
        description="3.1.2 | (U) Demonstrate the ability to develop a sensor placement strategy based on knowledge gaps in traffic results. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=100)
    db.session.add(course_task)

    task = Task(
        title="3.2 | (U) Security Recommendations |  |  |  |",
        description="3.2 | (U) Security Recommendations |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=101)
    db.session.add(course_task)

    task = Task(
        title="3.2.1 | (U) Demonstrate the ability to analyze the network map/network traffic of a customer and provide best practices",
        description="3.2.1 | (U) Demonstrate the ability to analyze the network map/network traffic of a customer and provide best practices or security recommendations. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=102)
    db.session.add(course_task)

    task = Task(
        title="3.2.2 | (U) Demonstrate how in the role as a Network Lead, what actions would take if a vulnerability is discovered on t",
        description="3.2.2 | (U) Demonstrate how in the role as a Network Lead, what actions would take if a vulnerability is discovered on the customer’s network. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=103)
    db.session.add(course_task)

    task = Task(
        title="3.2.3 | (U) Demonstrate the ability to create security recommendations that highlight the priority level of each securit",
        description="3.2.3 | (U) Demonstrate the ability to create security recommendations that highlight the priority level of each security risk discovered as a result of analysis. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=104)
    db.session.add(course_task)

    task = Task(
        title="3.2.4 | Provide security recommendations for the following security risks: Customer utilizing software that is no longer",
        description="3.2.4 | Provide security recommendations for the following security risks: Customer utilizing software that is no longer being supported. Administrative users using the same account to perform all administrative functions on the network. Firewalls not configured properly allowing, unauthorized access to the network. Default policies on software utilized by the customer. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=105)
    db.session.add(course_task)

    task = Task(
        title="3.2.5 | Explain appropriate briefing. Describe the kinds of information a network analyst should provide to a Team Lead",
        description="3.2.5 | Explain appropriate briefing. Describe the kinds of information a network analyst should provide to a Team Lead or Mission Partner.  Training Resources & Technical References: CWP 3-33.4 CPT Organization Functions, and Employment |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=106)
    db.session.add(course_task)

    task = Task(
        title="3.3 | (U) Signature Creation |  |  |  |",
        description="3.3 | (U) Signature Creation |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=107)
    db.session.add(course_task)

    task = Task(
        title="3.3.1 | (U) Demonstrate the ability to, from traffic, identify selectors to create IOC signatures for, and create said s",
        description="3.3.1 | (U) Demonstrate the ability to, from traffic, identify selectors to create IOC signatures for, and create said signatures. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=108)
    db.session.add(course_task)

    task = Task(
        title="3.3.2 | Demonstrate the ability to create signatures for future detection. Late night connections. Beaconing. Long stand",
        description="3.3.2 | Demonstrate the ability to create signatures for future detection. Late night connections. Beaconing. Long standing connections. Command and control. Known bad IP addresses/domains. Unusual traffic patterns. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=109)
    db.session.add(course_task)

    task = Task(
        title="3.4 | (U) Capture Network Traffic |  |  |  |",
        description="3.4 | (U) Capture Network Traffic |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=110)
    db.session.add(course_task)

    task = Task(
        title="3.4.1 | (U) Demonstrate the ability to formulate a data collection plan and defend a proposed mission. |  |  |  |",
        description="3.4.1 | (U) Demonstrate the ability to formulate a data collection plan and defend a proposed mission. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=111)
    db.session.add(course_task)

    task = Task(
        title="3.5 | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traf",
        description="3.5 | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=112)
    db.session.add(course_task)

    task = Task(
        title="3.5.1 | (U) Demonstrate mission execution from customer contact to drafting of an AAR. |  |  |  |",
        description="3.5.1 | (U) Demonstrate mission execution from customer contact to drafting of an AAR. |  |  |  |",
        grading_type="trainer",
        requires_upload=False
    )
    db.session.add(task)
    db.session.flush()  # get task.id
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=113)
    db.session.add(course_task)

    db.session.commit()
