import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app, db
from app.models import Course, Task, CourseTask

app = create_app()
app.app_context().push()

# === Host Basic ===
course = Course.query.filter_by(name="Host Basic").first()
if course:
    task = Task(
        title="| 1.1 | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals | (U) DCO-IDM & Mission Knowledge Fundamentals",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="| Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM) Comp",
        description="| Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM) Company.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.1",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="| Describe the roles and responsibilities for 3d Network Battalion.",
        description="| Describe the roles and responsibilities for 3d Network Battalion.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.2",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="| Describe the following mission types:",
        description="| Describe the following mission types:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.3",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="| Explain the structure of a Mission Element and their roles.",
        description="| Explain the structure of a Mission Element and their roles.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.4",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="| Describe relevant policies and procedures governing the DCO-IDM Company.",
        description="| Describe relevant policies and procedures governing the DCO-IDM Company.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.5",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="| Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.",
        description="| Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.6",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="| (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to the m",
        description="| (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to the mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.7",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="| Describe the Mission Element Lead responsibilities toward network owner interaction.",
        description="| Describe the Mission Element Lead responsibilities toward network owner interaction.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.8",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="| Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeholders.",
        description="| Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeholders.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.9",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="| (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrate data",
        description="| (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrate data collection.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.10",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="| Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.",
        description="| Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.11",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="| Define Battle Rhythm and discuss why it is useful in preparing for a mission.",
        description="| Define Battle Rhythm and discuss why it is useful in preparing for a mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.12",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="| Identify and describe information resources at the company to use during mission planning.",
        description="| Identify and describe information resources at the company to use during mission planning.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.13",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="| Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.",
        description="| Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.14",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="| (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.",
        description="| (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.15",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="| Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.",
        description="| Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.16",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="| Briefing.",
        description="| Briefing.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.17",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="| Explain the timeline for creating and completing the final report.",
        description="| Explain the timeline for creating and completing the final report.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.18",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="| Describe incident response.",
        description="| Describe incident response.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.19",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="| (U) Describe the purpose of an Equipment Density List (EDL).",
        description="| (U) Describe the purpose of an Equipment Density List (EDL).",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.20",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="| Explain the purpose and components of a Risk Mitigation Plan.",
        description="| Explain the purpose and components of a Risk Mitigation Plan.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.21",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="| Describe priority items or artifacts that may be found in an investigation.",
        description="| Describe priority items or artifacts that may be found in an investigation.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.22",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="| Describe the process in determining the proper mitigations and courses of action for a mission owner.",
        description="| Describe the process in determining the proper mitigations and courses of action for a mission owner.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.23",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="| Discuss the scope and audience of a hot-wash.",
        description="| Discuss the scope and audience of a hot-wash.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.24",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="| Explain the importance of the after action review and what should be included.",
        description="| Explain the importance of the after action review and what should be included.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.25",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="| Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.",
        description="| Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.26",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="| Explain the procedures and required documentation for transporting classified material and what procedure to follow wh",
        description="| Explain the procedures and required documentation for transporting classified material and what procedure to follow when passing through airport security.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.27",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="| (U) Give an example of PKI and the known vulnerabilities in a",
        description="| (U) Give an example of PKI and the known vulnerabilities in a",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.28",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="| Explain network security implications if the following concepts are poorly implemented:",
        description="| Explain network security implications if the following concepts are poorly implemented:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.29",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="| (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain the difference bet",
        description="| (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain the difference between risk and threat as they relate to vulnerabilities. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.30",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="| Explain network security implications if the following concepts are poorly implemented:",
        description="| Explain network security implications if the following concepts are poorly implemented:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.31",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="| Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) |",
        description="| Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) | Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.32",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="| (U) Explain the difference between attributable and non-attributable IP",
        description="| (U) Explain the difference between attributable and non-attributable IP",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.33",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="| (U) Describe what constitutes a US Person.",
        description="| (U) Describe what constitutes a US Person.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.34",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="| Explain the following in regards to reports.",
        description="| Explain the following in regards to reports.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.35",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="| Describe what each of the following DCO-IDM capabilities provide to supported commanders:",
        description="| Describe what each of the following DCO-IDM capabilities provide to supported commanders:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.36",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="| As part of a mission, describe the systems that should be evaluated to gain situational awareness of the mission partn",
        description="| As part of a mission, describe the systems that should be evaluated to gain situational awareness of the mission partner’s network.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.37",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="| Explain the following initial steps that are completed before an evaluation is started:",
        description="| Explain the following initial steps that are completed before an evaluation is started:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.38",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="| Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What is the u",
        description="| Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What is the ultimate goal of a collection plan?",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.39",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="| Explain how the below guidelines can be useful to the Network Analyst.",
        description="| Explain how the below guidelines can be useful to the Network Analyst.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.40",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="| Explain what a SITREP is.",
        description="| Explain what a SITREP is.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.41",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="| Explain the following types of orders:",
        description="| Explain the following types of orders:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.42",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="| Explain what “Mission Relevant Key Terrain” (MRT-C) is.",
        description="| Explain what “Mission Relevant Key Terrain” (MRT-C) is.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.43",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="| (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |",
        description="| (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.44",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="| (U) Walkthrough the layout of MCEN in the INDOPACOM region.",
        description="| (U) Walkthrough the layout of MCEN in the INDOPACOM region.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.45",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.46 | (U) Explain the difference phases of the operational cycle.",
        description="| 1.1.46 | (U) Explain the difference phases of the operational cycle.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.46",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="| 1.2 | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals | (U) Host Fundamentals",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.1 | Define dead disk.",
        description="| 1.2.1 | Define dead disk.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.1",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.2 | (U) Describe the types of volatile network information that can be obtained from a host for analysis.",
        description="| 1.2.2 | (U) Describe the types of volatile network information that can be obtained from a host for analysis.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.2",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.3 | Memory Acquisition.",
        description="| 1.2.3 | Memory Acquisition.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.3",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.4 | Memory Allocation.",
        description="| 1.2.4 | Memory Allocation.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.4",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.5 | Set User ID and Set Group ID.",
        description="| 1.2.5 | Set User ID and Set Group ID.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.5",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.6 | Logging",
        description="| 1.2.6 | Logging",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.6",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.7 | Describe the default logs that are kept on a Windows System.",
        description="| 1.2.7 | Describe the default logs that are kept on a Windows System.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.7",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.8 | Describe Event Logs content and indicators within the logs that must be analyzed during a vulnerability assess",
        description="| 1.2.8 | Describe Event Logs content and indicators within the logs that must be analyzed during a vulnerability assessment.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.8",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.9 | Unix Profiles.",
        description="| 1.2.9 | Unix Profiles.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.9",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.10 | Active Directory Structures",
        description="| 1.2.10 | Active Directory Structures",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.10",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.11 | Registry Keys.",
        description="| 1.2.11 | Registry Keys.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.11",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.12 | DLL search order.",
        description="| 1.2.12 | DLL search order.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.12",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.13 | Rootkits.",
        description="| 1.2.13 | Rootkits.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.13",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.14 | Portable Executable.",
        description="| 1.2.14 | Portable Executable.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.14",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.15 | Describe the following encoding types.",
        description="| 1.2.15 | Describe the following encoding types.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.15",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.16 | Define exfiltration staging.",
        description="| 1.2.16 | Define exfiltration staging.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.16",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.17 | Describe three methods to obfuscate or hide programs on compromised systems.",
        description="| 1.2.17 | Describe three methods to obfuscate or hide programs on compromised systems.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.17",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.18 | Describe common data and file obfuscation techniques based on file attributes and naming conventions.",
        description="| 1.2.18 | Describe common data and file obfuscation techniques based on file attributes and naming conventions.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.18",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.19 | (U) Describe the purpose of Handles on a Windows operating system.",
        description="| 1.2.19 | (U) Describe the purpose of Handles on a Windows operating system.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.19",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.20 | Discuss how process handles may indicate anomalous or malicious activity.",
        description="| 1.2.20 | Discuss how process handles may indicate anomalous or malicious activity.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.20",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.21 | Explain how analyzing the number of handles associated with a process across a given network could be used to",
        description="| 1.2.21 | Explain how analyzing the number of handles associated with a process across a given network could be used to find anomalous or malicious activity.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.21",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.22 | Services.",
        description="| 1.2.22 | Services.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.22",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.23 | Passwords.",
        description="| 1.2.23 | Passwords.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.23",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.24 | Permission levels.",
        description="| 1.2.24 | Permission levels.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.24",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.25 | Evidence of Program execution. Describe the following artifacts.",
        description="| 1.2.25 | Evidence of Program execution. Describe the following artifacts.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.25",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.26 | Explain the significance of at least two Common Vulnerabilities and Exposures (CVE) reports retrieved from th",
        description="| 1.2.26 | Explain the significance of at least two Common Vulnerabilities and Exposures (CVE) reports retrieved from the National Vulnerability Database that are relevant to III MEF and the INDOPACOM region.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.26",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.27 | (U) Identify two vulnerability scanner benefits and limitations.",
        description="| 1.2.27 | (U) Identify two vulnerability scanner benefits and limitations.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.27",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.28 | Explain the process of identifying anomalous or potentially malicious files using a known good baseline and f",
        description="| 1.2.28 | Explain the process of identifying anomalous or potentially malicious files using a known good baseline and full file system directory listing.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.28",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.29 | Demonstrate how to compare file hashes against known lists which include:",
        description="| 1.2.29 | Demonstrate how to compare file hashes against known lists which include:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.29",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.30 | Explain how and when to use Virus Total.",
        description="| 1.2.30 | Explain how and when to use Virus Total.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.30",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.31 | Describe the significance of the following privilege levels:",
        description="| 1.2.31 | Describe the significance of the following privilege levels:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.31",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.32 | Provide an example command in Windows to recursively list all files, including hidden and system files, of th",
        description="| 1.2.32 | Provide an example command in Windows to recursively list all files, including hidden and system files, of the C: drive.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.32",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.33 | Explain how to check for outdated patches.",
        description="| 1.2.33 | Explain how to check for outdated patches.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.33",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.34 | Explain how to identify multiple installed versions of an application.",
        description="| 1.2.34 | Explain how to identify multiple installed versions of an application.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.34",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.35 | Explain the purpose and significance of the following:",
        description="| 1.2.35 | Explain the purpose and significance of the following:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.35",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.36 | (U) Describe each of the following key Windows processes and their functions:",
        description="| 1.2.36 | (U) Describe each of the following key Windows processes and their functions:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.36",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.37 | (U) Discuss Windows default shares. Include the following points in the discussion:",
        description="| 1.2.37 | (U) Discuss Windows default shares. Include the following points in the discussion:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.37",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.38 | Describe the function, output, and significance of the following native Windows commands:",
        description="| 1.2.38 | Describe the function, output, and significance of the following native Windows commands:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.38",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.39 | (U) Describe the function, output, and significance of the following",
        description="| 1.2.39 | (U) Describe the function, output, and significance of the following",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.39",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.40 | Descrbe t ftion, output, and sigicance of the following Windows Reso Kit tools:",
        description="| 1.2.40 | Descrbe t ftion, output, and sigicance of the following Windows Reso Kit tools:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.40",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.41 | Discuss the significance of the \"at\" command and its relationship with the NT AUTHORITY\SYSTEM account.",
        description="| 1.2.41 | Discuss the significance of the \"at\" command and its relationship with the NT AUTHORITY\SYSTEM account.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.41",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.42 | Compare differences in the function and purpose of NetBIOS names and a Fully Qualified Domain Names (FQDN).",
        description="| 1.2.42 | Compare differences in the function and purpose of NetBIOS names and a Fully Qualified Domain Names (FQDN).",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.42",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.43 | Explain the following Dynamic Host Configuration Protocol (DHCP) topics:",
        description="| 1.2.43 | Explain the following Dynamic Host Configuration Protocol (DHCP) topics:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.43",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.44 | Explain the following Domain Name System (DNS) topics:",
        description="| 1.2.44 | Explain the following Domain Name System (DNS) topics:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.44",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.45 | Discuss how an insecurely configured DNS server that allows external, untrusted zone transfers could provide",
        description="| 1.2.45 | Discuss how an insecurely configured DNS server that allows external, untrusted zone transfers could provide information to an attacker.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.45",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.46 | (U) Describe the following Windows Security Features and how they are leveraged during an assessment:",
        description="| 1.2.46 | (U) Describe the following Windows Security Features and how they are leveraged during an assessment:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.46",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=94)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.47 | Describe alternate data streaming and hiding in plain sight techniques.",
        description="| 1.2.47 | Describe alternate data streaming and hiding in plain sight techniques.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.47",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=95)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.48 | Discuss the significance of the following windows directories:",
        description="| 1.2.48 | Discuss the significance of the following windows directories:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.48",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=96)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.49 | Discuss the significance of the following unix directories:",
        description="| 1.2.49 | Discuss the significance of the following unix directories:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.49",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=97)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.50 | Compare the differences and similarities between “Trusted Installer” and system accounts.",
        description="| 1.2.50 | Compare the differences and similarities between “Trusted Installer” and system accounts.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.50",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=98)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.51 | Describe the following terms and indicate how it is relevant to cyber operations:",
        description="| 1.2.51 | Describe the following terms and indicate how it is relevant to cyber operations:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.51",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=99)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.52 | Describe how 32-bit applications run on a 64-bit Windows platform and what restrictions apply.",
        description="| 1.2.52 | Describe how 32-bit applications run on a 64-bit Windows platform and what restrictions apply.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.52",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=100)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.53 | Describe the different types of virtualization, including application, operating system, hardware, and presen",
        description="| 1.2.53 | Describe the different types of virtualization, including application, operating system, hardware, and presentation.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.53",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=101)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.54 | Describe the different types of hypervisors, containers, and virtual machines.",
        description="| 1.2.54 | Describe the different types of hypervisors, containers, and virtual machines.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.54",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=102)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.55 | List common techniques used to anonymize network traffic from an attack perspective.",
        description="| 1.2.55 | List common techniques used to anonymize network traffic from an attack perspective.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.55",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=103)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.56 | Research an open source vulnerability assessment to answer mission requirements.",
        description="| 1.2.56 | Research an open source vulnerability assessment to answer mission requirements.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.56",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=104)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.57 | Describe best practices to collect, assess, and identify improperly configured host-based firewall settings.",
        description="| 1.2.57 | Describe best practices to collect, assess, and identify improperly configured host-based firewall settings.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.57",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=105)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.58 | (U) Analyze a Microsoft Security Bulletin and/or open source zero day reporting to identify software and oper",
        description="| 1.2.58 | (U) Analyze a Microsoft Security Bulletin and/or open source zero day reporting to identify software and operating system vulnerabilities that are exploitable through available capabilities.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.58",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=106)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.59 | Describe the purpose, access requirements, classification levels, and sensitivities of data repositories used",
        description="| 1.2.59 | Describe the purpose, access requirements, classification levels, and sensitivities of data repositories used to perform mission-essential analytics.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.59",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=107)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.60 | Describe how to collect terminal history for users of a Linux host.",
        description="| 1.2.60 | Describe how to collect terminal history for users of a Linux host.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.60",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=108)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.61 | Describe the information that can be found in /etc/passwd,",
        description="| 1.2.61 | Describe the information that can be found in /etc/passwd,",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.61",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=109)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.62 | Describe intrusion artifacts that can be found in /proc.",
        description="| 1.2.62 | Describe intrusion artifacts that can be found in /proc.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.62",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=110)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.63 | Describe how jumps in index node number can indicate a malicious file.",
        description="| 1.2.63 | Describe how jumps in index node number can indicate a malicious file.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.63",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=111)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.64 | Define Web Proxy.",
        description="| 1.2.64 | Define Web Proxy.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.64",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=112)
    db.session.add(course_task)

    task = Task(
        title="| 1.3 | (U) Discuss the MITRE ATT&CK Framework and identify potential host artifacts. |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=113)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.1 | Reconnaissance",
        description="| 1.3.1 | Reconnaissance",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.1",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=114)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.2 | Resource Development",
        description="| 1.3.2 | Resource Development",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.2",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=115)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.3 | Initial Access",
        description="| 1.3.3 | Initial Access",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.3",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=116)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.4 | Execution",
        description="| 1.3.4 | Execution",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.4",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=117)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.5 | Privilege Escalation",
        description="| 1.3.5 | Privilege Escalation",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.5",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=118)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.6 | Defense Evasion",
        description="| 1.3.6 | Defense Evasion",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.6",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=119)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.7 | Credential Access",
        description="| 1.3.7 | Credential Access",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.7",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=120)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.8 | Discovery",
        description="| 1.3.8 | Discovery",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.8",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=121)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.9 | Lateral movement",
        description="| 1.3.9 | Lateral movement",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.9",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=122)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.10 | (U) Collection",
        description="| 1.3.10 | (U) Collection",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.10",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=123)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.11 | Command and Control",
        description="| 1.3.11 | Command and Control",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.11",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=124)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.12 | Exfiltration",
        description="| 1.3.12 | Exfiltration",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.12",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=125)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.13 | Impact",
        description="| 1.3.13 | Impact",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.13",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=126)
    db.session.add(course_task)

    task = Task(
        title="| 2.1 | (U) Host Analysis |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=127)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.1 | Describe the following capabilities of Splunk.",
        description="| 2.1.1 | Describe the following capabilities of Splunk.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.1",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=128)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.2 | (U)  Describe the following capabilities of Security Onion.",
        description="| 2.1.2 | (U)  Describe the following capabilities of Security Onion.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.2",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=129)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.3 | (U) Describe the following capabilities of Red Seal.",
        description="| 2.1.3 | (U) Describe the following capabilities of Red Seal.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.3",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=130)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.4 | (U) Describe the following capabilities of Palo Alto.",
        description="| 2.1.4 | (U) Describe the following capabilities of Palo Alto.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.4",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=131)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.5 | Describe the following capabilities of Tanium.",
        description="| 2.1.5 | Describe the following capabilities of Tanium.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.5",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=132)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.6 | (U)  Describe the following capabilities of MDE.",
        description="| 2.1.6 | (U)  Describe the following capabilities of MDE.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.6",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=133)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.7 | Describe the following capabilities of HX.",
        description="| 2.1.7 | Describe the following capabilities of HX.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.7",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=134)
    db.session.add(course_task)

    task = Task(
        title="| 2.2 | (U) Software |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=135)
    db.session.add(course_task)

    task = Task(
        title="| 2.2.3 | Describe the primary functions PowerShell.",
        description="| 2.2.3 | Describe the primary functions PowerShell.",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.3",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=136)
    db.session.add(course_task)

    task = Task(
        title="| 2.2.4 | Describe the primary functions Sysinternals.",
        description="| 2.2.4 | Describe the primary functions Sysinternals.",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.4",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=137)
    db.session.add(course_task)

    task = Task(
        title="| 2.2.5 | (U) Describe the primary functions of windows native tools.",
        description="| 2.2.5 | (U) Describe the primary functions of windows native tools.",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.5",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=138)
    db.session.add(course_task)

    task = Task(
        title="| 3.1 | (U) Demonstration |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=139)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.1 | Demonstrate at least two ways to access the following native OS tools locally and remotely:",
        description="| 3.1.1 | Demonstrate at least two ways to access the following native OS tools locally and remotely:",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.1",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=140)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.2 | Analyze and refine vulnerability tools in a test environment to optimize performance in accordance with missio",
        description="| 3.1.2 | Analyze and refine vulnerability tools in a test environment to optimize performance in accordance with mission objectives.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.2",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=141)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.3 | (U) Create a script or program that employs multiple inputs, command line arguments, and environmental variabl",
        description="| 3.1.3 | (U) Create a script or program that employs multiple inputs, command line arguments, and environmental variables to solve a mission requirement. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.3",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=142)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.5 | Identify the appropriate security control measures to implement based on a given threat actor TTP.",
        description="| 3.1.5 | Identify the appropriate security control measures to implement based on a given threat actor TTP.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.5",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=143)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.7 | Explain how to use software debugging tools to identify potential vulnerabilities, illegitimate functionality,",
        description="| 3.1.7 | Explain how to use software debugging tools to identify potential vulnerabilities, illegitimate functionality, and hidden content.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.7",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=144)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.8 | (U) Identify appropriate security controls that align with detecting and inhibiting known adversarial capabili",
        description="| 3.1.8 | (U) Identify appropriate security controls that align with detecting and inhibiting known adversarial capabilities, tactics, techniques, and procedures. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.8",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=145)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.9 | (U) Detect a rogue or unauthorized system within a specified domain on the network using available tools, tech",
        description="| 3.1.9 | (U) Detect a rogue or unauthorized system within a specified domain on the network using available tools, techniques, and information. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.9",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=146)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.10 | Analyze a software baseline to identify systemic issues that could lead to vulnerability exploitation.",
        description="| 3.1.10 | Analyze a software baseline to identify systemic issues that could lead to vulnerability exploitation.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.10",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=147)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.11 | (U) Assess domain-joined and stand-alone systems for improper configurations. |  |  |  |",
        description="| 3.1.11 | (U) Assess domain-joined and stand-alone systems for improper configurations. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.11",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=148)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.12 | Assess domain-joined and stand-alone systems for anomalous or malicious behavior.",
        description="| 3.1.12 | Assess domain-joined and stand-alone systems for anomalous or malicious behavior.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.12",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=149)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.13 | (U) Assess a system and/or host group management, group",
        description="| 3.1.13 | (U) Assess a system and/or host group management, group",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.13",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=150)
    db.session.add(course_task)

    task = Task(
        title="| 4.1 | (U) Hardware |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="4.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=151)
    db.session.add(course_task)

    task = Task(
        title="| 4.1.1 | Explain the function of the following appliances:",
        description="| 4.1.1 | Explain the function of the following appliances:",
        grading_type="trainer",
        requires_upload=False,
        label="4.1.1",
        section_label="4.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=152)
    db.session.add(course_task)

    task = Task(
        title="| 4.1.2 | Explain the following storage concepts and devices:",
        description="| 4.1.2 | Explain the following storage concepts and devices:",
        grading_type="trainer",
        requires_upload=False,
        label="4.1.2",
        section_label="4.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=153)
    db.session.add(course_task)

    task = Task(
        title="| 4.1.3 | For each of the following hardware pieces of the kit, identify and explain the utility for host or network ana",
        description="| 4.1.3 | For each of the following hardware pieces of the kit, identify and explain the utility for host or network analysis:",
        grading_type="trainer",
        requires_upload=False,
        label="4.1.3",
        section_label="4.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=154)
    db.session.add(course_task)

    task = Task(
        title="| 4.2 | (U) Virtual Machines |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="4.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=155)
    db.session.add(course_task)

    task = Task(
        title="| 4.2.1 | (U) For each of the following virtual machines on the kit, identify and explain the utility for host or networ",
        description="| 4.2.1 | (U) For each of the following virtual machines on the kit, identify and explain the utility for host or network analysis:",
        grading_type="trainer",
        requires_upload=False,
        label="4.2.1",
        section_label="4.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=156)
    db.session.add(course_task)

    db.session.commit()

# === Host Senior ===
course = Course.query.filter_by(name="Host Senior").first()
if course:
    task = Task(
        title="| (U) DCO-IDM & Mission Knowledge |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="| Given intelligence reporting describe how to integrate it into tactical planning.",
        description="| Given intelligence reporting describe how to integrate it into tactical planning.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.1",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="| Describe the process of developing analytics to support mission requirements and reporting.",
        description="| Describe the process of developing analytics to support mission requirements and reporting.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.2",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="| Describe the process for surveilling Named Areas of Interest (NAIs).",
        description="| Describe the process for surveilling Named Areas of Interest (NAIs).",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.3",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="| Describe under what circumstances you would need to engage with the local Counter Intelligence or law enforcement agen",
        description="| Describe under what circumstances you would need to engage with the local Counter Intelligence or law enforcement agencies.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.4",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="| Given a critical asset list/key terrain cyber prioritize vulnerabilities for the mission owner.",
        description="| Given a critical asset list/key terrain cyber prioritize vulnerabilities for the mission owner.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.5",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="| Describe the chain of custody and your role in maintaining it and relationship with CI/LE.",
        description="| Describe the chain of custody and your role in maintaining it and relationship with CI/LE.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.6",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate understanding of the following policies and documents:",
        description="| Demonstrate understanding of the following policies and documents:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.7",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="| Explain the difference between Cyberspace authorities and SIGINT authorities.",
        description="| Explain the difference between Cyberspace authorities and SIGINT authorities.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.8",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="| Describe the ME Lead’s responsibilities toward mission owner interaction.",
        description="| Describe the ME Lead’s responsibilities toward mission owner interaction.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.9",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="| Describe how the ME Lead will synchronize efforts with local defenders, customer and key stakeholders.",
        description="| Describe how the ME Lead will synchronize efforts with local defenders, customer and key stakeholders.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.10",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="| Describe how, by working with the mission owner, the ME Lead can determine where to concentrate data collection.",
        description="| Describe how, by working with the mission owner, the ME Lead can determine where to concentrate data collection.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.11",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="| Explain the importance of an out-brief and what should be included.",
        description="| Explain the importance of an out-brief and what should be included.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.12",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="| Explain the importance of the final report and what it should include.",
        description="| Explain the importance of the final report and what it should include.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.13",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="| Explain how to prioritize Host Analyst findings and mitigation recommendations in the final report.",
        description="| Explain how to prioritize Host Analyst findings and mitigation recommendations in the final report.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.14",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="| Describe the ME Leads responsibilities for reporting.",
        description="| Describe the ME Leads responsibilities for reporting.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.15",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="| Describe how to utilize “phase line” when executing the mission and the importance of it.",
        description="| Describe how to utilize “phase line” when executing the mission and the importance of it.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.16",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="| (U) Collection Planning |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="| Discuss what a collection plan is and how pertinent it is to accomplish a successful mission.",
        description="| Discuss what a collection plan is and how pertinent it is to accomplish a successful mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.1",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="| Given a list of resources define what is relevant in building a collection plan.",
        description="| Given a list of resources define what is relevant in building a collection plan.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.2",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="| (U) Identify the steps on building a collection plan.",
        description="| (U) Identify the steps on building a collection plan.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.3",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="| Explain why it is important to understand the customer’s organizational policies for users and computers.",
        description="| Explain why it is important to understand the customer’s organizational policies for users and computers.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.4",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="| Identify the importance of a Pre-Deployment Site Survey.",
        description="| Identify the importance of a Pre-Deployment Site Survey.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.5",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="| Define the term “Rules of Engagement” and how it applies to a mission.",
        description="| Define the term “Rules of Engagement” and how it applies to a mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.6",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="| (U) Host Knowledge |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="| Given organization system policy identify invalid active directory objects.",
        description="| Given organization system policy identify invalid active directory objects.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.1",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="| Given an Active Directory domain audit policy and threat actor tactics, techniques and procedures identify auditing ga",
        description="| Given an Active Directory domain audit policy and threat actor tactics, techniques and procedures identify auditing gaps that would prevent logging.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.2",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate using PowerShell to manage Active Directory applicable to cyber operations.",
        description="| Demonstrate using PowerShell to manage Active Directory applicable to cyber operations.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.3",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="| Interpret and configure host-based firewalls and Host Intrusion Prevention Systems through group policy.",
        description="| Interpret and configure host-based firewalls and Host Intrusion Prevention Systems through group policy.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.4",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="| Explain how to ensure patches are up to date for all domain workstations and determine effectiveness of current proces",
        description="| Explain how to ensure patches are up to date for all domain workstations and determine effectiveness of current process for updating.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.5",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="| Given a list of IOCs identify key log entries/Event IDs ,use a Security information and event management (SIEM) platfo",
        description="| Given a list of IOCs identify key log entries/Event IDs ,use a Security information and event management (SIEM) platform to correlate indicators of compromise, and develop dashboards to better visualize data.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.6",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="| Using a SIEM create alerts to detect the creation of unauthorized accounts.",
        description="| Using a SIEM create alerts to detect the creation of unauthorized accounts.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.7",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="| Configure, forward, and statically analyze logs from all workstations in an enterprise environment.",
        description="| Configure, forward, and statically analyze logs from all workstations in an enterprise environment.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.8",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="| Describe the relationship between the pyramid of pain and the development of signatures and detection methods.",
        description="| Describe the relationship between the pyramid of pain and the development of signatures and detection methods.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.9",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="| (U) Explain how to oversee the tuning of host-based IDS/IPS alerts in order to evaluate their severity while eliminati",
        description="| (U) Explain how to oversee the tuning of host-based IDS/IPS alerts in order to evaluate their severity while eliminating false positives.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.10",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="| Given a list of active processes identify libraries, modules, executables, and binaries against databases of known adv",
        description="| Given a list of active processes identify libraries, modules, executables, and binaries against databases of known advanced malware.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.11",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="| Given and IOC, explain how to utilize tools and analysis techniques to identify processes, libraries, modules, and oth",
        description="| Given and IOC, explain how to utilize tools and analysis techniques to identify processes, libraries, modules, and other activity that have been obfuscated and might indicate the presence of a more advanced rootkit on endpoint.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.12",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="| Given a Prioritized Defended Asset list, identify which dependent systems are key terrain.",
        description="| Given a Prioritized Defended Asset list, identify which dependent systems are key terrain.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.13",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="| Evaluate patch levels on host machines across a complex Windows domain to determine the current patch level consistenc",
        description="| Evaluate patch levels on host machines across a complex Windows domain to determine the current patch level consistency.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.14",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="| Given a host baseline of configuration/state, for host machines on a network conduct a scan for anomalous configuratio",
        description="| Given a host baseline of configuration/state, for host machines on a network conduct a scan for anomalous configurations.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.15",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="| Given a Windows Domain Controller, evaluate information (e.g. users, groups, trust relationships, and security policie",
        description="| Given a Windows Domain Controller, evaluate information (e.g. users, groups, trust relationships, and security policies) from a complex Domain to identify vulnerabilities/misconfiguration, and how to export this information.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.16",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="| Given a script determine what is occurring.",
        description="| Given a script determine what is occurring.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.17",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="| Perform device discovery in order to conduct enumeration of a complex network while limiting the amount of network tra",
        description="| Perform device discovery in order to conduct enumeration of a complex network while limiting the amount of network traffic generated.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.18",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="| Analyze host discovery tool output to generate accurate maps of endpoint systems.",
        description="| Analyze host discovery tool output to generate accurate maps of endpoint systems.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.19",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="| (U) Enterprise Domain Knowledge |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="| (U) Given an enterprise domain, explain how to identify potentially malicious processes, connections, libraries, and o",
        description="| (U) Given an enterprise domain, explain how to identify potentially malicious processes, connections, libraries, and other malicious code/activity from a memory image and perform trend and outlier",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.1",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="| Automate advanced and repetitive tasks on remote workstations within a domain.",
        description="| Automate advanced and repetitive tasks on remote workstations within a domain.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.2",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="| Assess customer security posture across a complex enterprise network to Identify security posture shortcomings.",
        description="| Assess customer security posture across a complex enterprise network to Identify security posture shortcomings.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.3",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="| Given a vulnerability scan and mission owner network information prioritize vulnerabilities for action.",
        description="| Given a vulnerability scan and mission owner network information prioritize vulnerabilities for action.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.4",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="| (U) Risk Mitigation & After Action |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.5",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="| Describe and display knowledge of the “After Action Report” and all areas needed to complete one.",
        description="| Describe and display knowledge of the “After Action Report” and all areas needed to complete one.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.1",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="| Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events related to",
        description="| Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events related to a compromise and recommend mitigations.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.2",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="| Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events related to",
        description="| Utilizing MITRE ATT&CK framework, perform complex root- cause analysis to determine the sequence of events related to a compromise and recommend mitigations",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.3",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate familiarity with STIGs on host machines by using any software platform to generate a report for a complex",
        description="| Demonstrate familiarity with STIGs on host machines by using any software platform to generate a report for a complex network and follow-up with recommendations.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.4",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="| Discuss the term “Lessons Learned” and how it applies to the CPT life cycle.",
        description="| Discuss the term “Lessons Learned” and how it applies to the CPT life cycle.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.5",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="| Given a scenario, identify steps to recover from a full- network compromise.",
        description="| Given a scenario, identify steps to recover from a full- network compromise.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.6",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="| (U) Tools |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="| Identify PS modules that are helpful for local analysis.",
        description="| Identify PS modules that are helpful for local analysis.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.1",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="| Identify PS module that are helpful for remote analysis.",
        description="| Identify PS module that are helpful for remote analysis.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.2",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="| Define what an Agent Based Security System is and how it could be advantageous during a mission.",
        description="| Define what an Agent Based Security System is and how it could be advantageous during a mission.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.3",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="| Deploy an agent based security system to an enterprise network.",
        description="| Deploy an agent based security system to an enterprise network.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.4",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="| Configure and develop rules for CPT host-based agents.",
        description="| Configure and develop rules for CPT host-based agents.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.5",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="| Given the Sysinternals suite identify what the specific capabilities the tools can provide.",
        description="| Given the Sysinternals suite identify what the specific capabilities the tools can provide.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.6",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="| Given a set of sysmon logs identify malicious process creation.",
        description="| Given a set of sysmon logs identify malicious process creation.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.7",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstration |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="| Detect adversary modification of the following:",
        description="| Detect adversary modification of the following:",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.1",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="| Detect adversary addition of user to local administrator group:",
        description="| Detect adversary addition of user to local administrator group:",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.2",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="| Detect adversary addition of root user and sudoer.",
        description="| Detect adversary addition of root user and sudoer.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.3",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="| Detect adversary presence in windows logon and startup scripts.",
        description="| Detect adversary presence in windows logon and startup scripts.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.4",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="| Detect adversary presence in linux logon and startup scripts.",
        description="| Detect adversary presence in linux logon and startup scripts.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.5",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="| Detect adversary addition to BITS jobs.",
        description="| Detect adversary addition to BITS jobs.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.6",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="| Detect DLL Search Order Hijacking.",
        description="| Detect DLL Search Order Hijacking.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.7",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="| Detect malicious hidden files and/or directories.",
        description="| Detect malicious hidden files and/or directories.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.8",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="| Detect the presence of a rootkit.",
        description="| Detect the presence of a rootkit.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.9",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="| Detect the presence of a malicious cronjob.",
        description="| Detect the presence of a malicious cronjob.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.10",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="| Detect the presence of a malware maintaining persistence through scheduled tasks.",
        description="| Detect the presence of a malware maintaining persistence through scheduled tasks.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.11",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="| Detect the presence of malware maintaining persistence through modified services.",
        description="| Detect the presence of malware maintaining persistence through modified services.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.12",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="| Detect the adversary changes to PATH variables.",
        description="| Detect the adversary changes to PATH variables.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.13",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="| Detect the presence of malicious activity using elevated execution permissions from the following methods:",
        description="| Detect the presence of malicious activity using elevated execution permissions from the following methods:",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.14",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="| Detect the use of shortcut modification.",
        description="| Detect the use of shortcut modification.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.15",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="| Detect malicious use of WMI event subscription.",
        description="| Detect malicious use of WMI event subscription.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.16",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="| Detect the use of data staging and encoding used prior to exfiltration.",
        description="| Detect the use of data staging and encoding used prior to exfiltration.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.17",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="| Detect the exfiltration of data over removable devices.",
        description="| Detect the exfiltration of data over removable devices.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.18",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate the ability to search for Indicators of Compromise on a dead disk.",
        description="| Demonstrate the ability to search for Indicators of Compromise on a dead disk.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.19",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="| Triage malware from dead disk and identify the process to get assistance with reverse engineering.",
        description="| Triage malware from dead disk and identify the process to get assistance with reverse engineering.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.20",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="| (U) Detect malware in Memory.",
        description="| (U) Detect malware in Memory.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.21",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="| Discover Files using Alternate Data streams.",
        description="| Discover Files using Alternate Data streams.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.22",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="| Submit tool and capability requirements to resolve mission gaps in accordance with established policies, regulations,",
        description="| Submit tool and capability requirements to resolve mission gaps in accordance with established policies, regulations, and procedures.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.23",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="| Evaluate a comprehensive assessment strategy that leverages available information sources, personnel, and systems to a",
        description="| Evaluate a comprehensive assessment strategy that leverages available information sources, personnel, and systems to address potential vulnerabilities and risk-related practices.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.24",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="| Incorporate open source vulnerability assessment tools into a virtual machine for use in a test environment.",
        description="| Incorporate open source vulnerability assessment tools into a virtual machine for use in a test environment.",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.25",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="| (U) Capstones |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="| Given current intelligence and a network map, create a host collection plan.",
        description="| Given current intelligence and a network map, create a host collection plan.",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.1",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="| Given a scenario and required data, draft or provide input to the host section of a risk mitigation plan.",
        description="| Given a scenario and required data, draft or provide input to the host section of a risk mitigation plan.",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.2",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    db.session.commit()

# === Network Basic ===
course = Course.query.filter_by(name="Network Basic").first()
if course:
    task = Task(
        title="| 1.1 | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals | (U) DCO-IDM Operations & Mission Knowledge Fundamentals",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.1 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-I",
        description="| 1.1.1 | Describe the roles and responsibilities of the Defensive Cyber Operations – Internal Defensive Measures (DCO-IDM) Company.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.1",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.2 | Describe the roles and responsibilities for 3d Network Battalion.",
        description="| 1.1.2 | Describe the roles and responsibilities for 3d Network Battalion.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.2",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.3 | Describe the following mission types:",
        description="| 1.1.3 | Describe the following mission types:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.3",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.4 | Explain the structure of a Mission Element and their roles.",
        description="| 1.1.4 | Explain the structure of a Mission Element and their roles.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.4",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.5 | Describe relevant policies and procedures governing the DCO-IDM Company.",
        description="| 1.1.5 | Describe relevant policies and procedures governing the DCO-IDM Company.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.5",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.6 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.",
        description="| 1.1.6 | Identify the DCO-IDM Company entities an analyst interfaces with during a hunt mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.6",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.7 | (U) Describe the external organizations the Mission Element interfaces with and their importance/significance",
        description="| 1.1.7 | (U) Describe the external organizations the Mission Element interfaces with and their importance/significance to the mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.7",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.8 | Describe the Mission Element Lead responsibilities toward network owner interaction.",
        description="| 1.1.8 | Describe the Mission Element Lead responsibilities toward network owner interaction.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.8",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.9 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeho",
        description="| 1.1.9 | Describe how the Mission Element Lead will synchronize efforts with local defenders, customer, and key stakeholders.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.9",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.10 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentr",
        description="| 1.1.10 | (U) Describe how, by working with the mission owner, the Mission Element Lead can determine where to concentrate data collection.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.10",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.11 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.",
        description="| 1.1.11 | Discuss where all DCO information pertaining to the mission can be found at the DCO-IDM Company level.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.11",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.12 | Define Battle Rhythm and discuss why it is useful in preparing for a mission.",
        description="| 1.1.12 | Define Battle Rhythm and discuss why it is useful in preparing for a mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.12",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.13 | Identify and describe information resources at the company to use during mission planning.",
        description="| 1.1.13 | Identify and describe information resources at the company to use during mission planning.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.13",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.14 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.",
        description="| 1.1.14 | Describe the contents and purpose of a risk assessment IAW NIST SP 800-30 r1.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.14",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.15 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.",
        description="| 1.1.15 | (U) Explain the process of generating a deconfliction plan with the local defender and why it is necessary.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.15",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.16 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.",
        description="| 1.1.16 | Explain how operation notes (OPNOTES) are used to aid the Mission Element Lead in the de-confliction process.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.16",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.17 | Briefing.",
        description="| 1.1.17 | Briefing.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.17",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.18 | Explain the timeline for creating and completing the final report.",
        description="| 1.1.18 | Explain the timeline for creating and completing the final report.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.18",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.19 | Describe incident response.",
        description="| 1.1.19 | Describe incident response.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.19",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.20 | (U) Describe the purpose of an Equipment Density List (EDL).",
        description="| 1.1.20 | (U) Describe the purpose of an Equipment Density List (EDL).",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.20",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.21 | Explain the purpose and components of a Risk Mitigation Plan.",
        description="| 1.1.21 | Explain the purpose and components of a Risk Mitigation Plan.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.21",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.22 | Describe priority items or artifacts that may be found in an investigation.",
        description="| 1.1.22 | Describe priority items or artifacts that may be found in an investigation.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.22",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.23 | Describe the process in determining the proper mitigations and courses of action for a mission owner.",
        description="| 1.1.23 | Describe the process in determining the proper mitigations and courses of action for a mission owner.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.23",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.24 | Discuss the scope and audience of a hot-wash.",
        description="| 1.1.24 | Discuss the scope and audience of a hot-wash.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.24",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.25 | Explain the importance of the after action review and what should be included.",
        description="| 1.1.25 | Explain the importance of the after action review and what should be included.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.25",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.26 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.",
        description="| 1.1.26 | Describe the importance of Title 10, Title 50, and Title 32 and the relevance of each on a DCO mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.26",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.27 | Explain the procedures and required documentation for transporting classified material and what procedure to",
        description="| 1.1.27 | Explain the procedures and required documentation for transporting classified material and what procedure to follow when passing through airport security.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.27",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.28 | (U) Give an example of PKI and the known vulnerabilities in a",
        description="| 1.1.28 | (U) Give an example of PKI and the known vulnerabilities in a",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.28",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.29 | Explain network security implications if the following concepts are poorly implemented:",
        description="| 1.1.29 | Explain network security implications if the following concepts are poorly implemented:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.29",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.30 | (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain the diffe",
        description="| 1.1.30 | (U) Explain the difference between risk and threat as they relate to vulnerabilities. | (U) Explain the difference between risk and threat as they relate to vulnerabilities. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.30",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.31 | Explain network security implications if the following concepts are poorly implemented:",
        description="| 1.1.31 | Explain network security implications if the following concepts are poorly implemented:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.31",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.32 | Explain network security implications associated with implementing Security Technical Implementation Guides (",
        description="| 1.1.32 | Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) | Explain network security implications associated with implementing Security Technical Implementation Guides (STIGs) |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.32",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.33 | (U) Explain the difference between attributable and non-attributable IP",
        description="| 1.1.33 | (U) Explain the difference between attributable and non-attributable IP",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.33",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.34 | (U) Describe what constitutes a US Person.",
        description="| 1.1.34 | (U) Describe what constitutes a US Person.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.34",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.35 | Explain the following in regards to reports.",
        description="| 1.1.35 | Explain the following in regards to reports.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.35",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.36 | Describe what each of the following DCO-IDM capabilities provide to supported commanders:",
        description="| 1.1.36 | Describe what each of the following DCO-IDM capabilities provide to supported commanders:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.36",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.37 | As part of a mission, describe the systems that should be evaluated to gain situational awareness of the miss",
        description="| 1.1.37 | As part of a mission, describe the systems that should be evaluated to gain situational awareness of the mission partner’s network.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.37",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.38 | Explain the following initial steps that are completed before an evaluation is started:",
        description="| 1.1.38 | Explain the following initial steps that are completed before an evaluation is started:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.38",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.39 | Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What",
        description="| 1.1.39 | Discuss what a collection plan is. What role network analysts play in the creation of a collection plan? What is the ultimate goal of a collection plan?",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.39",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.40 | Explain how the below guidelines can be useful to the Network Analyst.",
        description="| 1.1.40 | Explain how the below guidelines can be useful to the Network Analyst.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.40",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.41 | Explain what a SITREP is.",
        description="| 1.1.41 | Explain what a SITREP is.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.41",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.42 | Explain the following types of orders:",
        description="| 1.1.42 | Explain the following types of orders:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.42",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.43 | Explain what “Mission Relevant Key Terrain” (MRT-C) is.",
        description="| 1.1.43 | Explain what “Mission Relevant Key Terrain” (MRT-C) is.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.43",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.44 | (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |  |  |  |  |  |",
        description="| 1.1.44 | (U) Explain/define IOT. | (U) Explain/define IOT. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.44",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.45 | (U) Walkthrough the layout of MCEN in the INDOPACOM region.",
        description="| 1.1.45 | (U) Walkthrough the layout of MCEN in the INDOPACOM region.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.45",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="| 1.1.46 | (U) Explain the difference phases of the operational cycle.",
        description="| 1.1.46 | (U) Explain the difference phases of the operational cycle.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.46",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="| 1.2 | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals | (U) Networking Fundamentals",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.1 | Describe the following as it relates to Network Address Translation (NAT):",
        description="| 1.2.1 | Describe the following as it relates to Network Address Translation (NAT):",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.1",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.2 | Explain how encapsulation mismatches on LAN links can affect communication between layers.",
        description="| 1.2.2 | Explain how encapsulation mismatches on LAN links can affect communication between layers.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.2",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.3 | Explain what benefits these network devices provide as secondary network defense systems:",
        description="| 1.2.3 | Explain what benefits these network devices provide as secondary network defense systems:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.3",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.4 | Describe the difference between link-state and distance vector routers.",
        description="| 1.2.4 | Describe the difference between link-state and distance vector routers.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.4",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.5 | Explain how the following IOS troubleshooting tools can be helpful:",
        description="| 1.2.5 | Explain how the following IOS troubleshooting tools can be helpful:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.5",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.6 | Describe the most common protocols used for tunneling:",
        description="| 1.2.6 | Describe the most common protocols used for tunneling:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.6",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.7 | Define and describe some security concerns related to each of the below items:",
        description="| 1.2.7 | Define and describe some security concerns related to each of the below items:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.7",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.8 | Describe network port security and describe how to implement it.",
        description="| 1.2.8 | Describe network port security and describe how to implement it.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.8",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.9 | Explain the following in regard to Cisco ACLs:",
        description="| 1.2.9 | Explain the following in regard to Cisco ACLs:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.9",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.10 | Define what a packet sniffer is and give two examples of vendor specific packet sniffers.",
        description="| 1.2.10 | Define what a packet sniffer is and give two examples of vendor specific packet sniffers.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.10",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.11 | Describe the use of firewalls, DMZ, and encryption in the MCEN.",
        description="| 1.2.11 | Describe the use of firewalls, DMZ, and encryption in the MCEN.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.11",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.12 | (U) Describe the following sections of a switch or router configuration file.",
        description="| 1.2.12 | (U) Describe the following sections of a switch or router configuration file.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.12",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.13 | Explain the different privilege levels associated with the following types of  network devices.",
        description="| 1.2.13 | Explain the different privilege levels associated with the following types of  network devices.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.13",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.14 | Describe the difference between the following password hashing/encryptions.",
        description="| 1.2.14 | Describe the difference between the following password hashing/encryptions.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.14",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.15 | Describe VPN and discuss how they are most often used in a customer network.",
        description="| 1.2.15 | Describe VPN and discuss how they are most often used in a customer network.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.15",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.16 | Describe the components of PKI in an enterprise network environment.",
        description="| 1.2.16 | Describe the components of PKI in an enterprise network environment.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.16",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.17 | Describe what a NetBIOS name is. Compare to a fully qualified domain name (FQDN).",
        description="| 1.2.17 | Describe what a NetBIOS name is. Compare to a fully qualified domain name (FQDN).",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.17",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.18 | (U) Describe the research that can be done on DNS domains using open source tools. | (U) Describe the researc",
        description="| 1.2.18 | (U) Describe the research that can be done on DNS domains using open source tools. | (U) Describe the research that can be done on DNS domains using open source tools. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.18",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.19 | (U) Describe port redirection when dealing with firewalls and ACLs. | (U) Describe port redirection when deal",
        description="| 1.2.19 | (U) Describe port redirection when dealing with firewalls and ACLs. | (U) Describe port redirection when dealing with firewalls and ACLs. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.19",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.20 | Describe UDP traceroute and the following in regards to it:",
        description="| 1.2.20 | Describe UDP traceroute and the following in regards to it:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.20",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.21 | Describe the difference between an unmanaged (isolated) system and a domain joined system.",
        description="| 1.2.21 | Describe the difference between an unmanaged (isolated) system and a domain joined system.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.21",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.22 | Explain how firewalls function:",
        description="| 1.2.22 | Explain how firewalls function:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.22",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.23 | Describe the Open Systems Interconnection (OSI) model and list the layers of it. List a network protocol that",
        description="| 1.2.23 | Describe the Open Systems Interconnection (OSI) model and list the layers of it. List a network protocol that would be found in each of the layers.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.23",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="| 1.2.24 | (U) Explain the difference between routable and non-routable space. | (U) Explain the difference between rout",
        description="| 1.2.24 | (U) Explain the difference between routable and non-routable space. | (U) Explain the difference between routable and non-routable space. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.24",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="| 1.3 | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis | (U) Traffic Analysis",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.1 | Describe what ‘Packet Capture’ (PCAP) data is and what information is contained within it.",
        description="| 1.3.1 | Describe what ‘Packet Capture’ (PCAP) data is and what information is contained within it.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.1",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.2 | Describe a potential implementation of Berkley Packet Filters (BPFs) during DCO.",
        description="| 1.3.2 | Describe a potential implementation of Berkley Packet Filters (BPFs) during DCO.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.2",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.3 | Describe the purpose of a Request for Comment (RFC). What kinds of information can be found in RFCs?",
        description="| 1.3.3 | Describe the purpose of a Request for Comment (RFC). What kinds of information can be found in RFCs?",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.3",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.4 | Provide a basic description of the fields in an IPv4 /IPv6 header.",
        description="| 1.3.4 | Provide a basic description of the fields in an IPv4 /IPv6 header.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.4",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.5 | Provide a basic description of the fields in a TCP header.",
        description="| 1.3.5 | Provide a basic description of the fields in a TCP header.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.5",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.6 | Provide a basic description of the fields in an UDP header.",
        description="| 1.3.6 | Provide a basic description of the fields in an UDP header.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.6",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.7 | Provide a basic description of the fields in an ICMP header.",
        description="| 1.3.7 | Provide a basic description of the fields in an ICMP header.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.7",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.8 | Explain what happens when a TCP packet with the SYN flag set arrives at host on a non- listening port.",
        description="| 1.3.8 | Explain what happens when a TCP packet with the SYN flag set arrives at host on a non- listening port.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.8",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.9 | Explain the response to an IP datagram sent to a host that is not available on a valid network.",
        description="| 1.3.9 | Explain the response to an IP datagram sent to a host that is not available on a valid network.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.9",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.10 | Explain what happens when a UDP packet arrives on a listening port.",
        description="| 1.3.10 | Explain what happens when a UDP packet arrives on a listening port.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.10",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.11 | Explain what happens when a UDP packet arrives on a non-listening port.",
        description="| 1.3.11 | Explain what happens when a UDP packet arrives on a non-listening port.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.11",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.12 | Describe the following fields within an HTTP header:",
        description="| 1.3.12 | Describe the following fields within an HTTP header:",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.12",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.13 | Describe the process of identifying anomalous activity and creation of a signature to identify future instanc",
        description="| 1.3.13 | Describe the process of identifying anomalous activity and creation of a signature to identify future instances.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.13",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.14 | Explain and describe the following Suricata/Snort IDS rule parameters:",
        description="| 1.3.14 | Explain and describe the following Suricata/Snort IDS rule parameters:",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.14",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="| 1.3.15 | Explain how the two main types of NIDS differ:",
        description="| 1.3.15 | Explain how the two main types of NIDS differ:",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.15",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="| 1.4 | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts | (U) Discuss the MITRE ATT&CK Framework and identify potential network artifacts",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.1 | (U) Reconnaissance",
        description="| 1.4.1 | (U) Reconnaissance",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.1",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.2 | Resource Development",
        description="| 1.4.2 | Resource Development",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.2",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.3 | Initial Access",
        description="| 1.4.3 | Initial Access",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.3",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.4 | Execution",
        description="| 1.4.4 | Execution",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.4",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.5 | Privilege Escalation",
        description="| 1.4.5 | Privilege Escalation",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.5",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=94)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.6 | Defense Evasion",
        description="| 1.4.6 | Defense Evasion",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.6",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=95)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.7 | Credential Access",
        description="| 1.4.7 | Credential Access",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.7",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=96)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.8 | Discovery",
        description="| 1.4.8 | Discovery",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.8",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=97)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.9 | Lateral movement",
        description="| 1.4.9 | Lateral movement",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.9",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=98)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.10 | (U) Collection",
        description="| 1.4.10 | (U) Collection",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.10",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=99)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.11 | Command and Control",
        description="| 1.4.11 | Command and Control",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.11",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=100)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.12 | Exfiltration",
        description="| 1.4.12 | Exfiltration",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.12",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=101)
    db.session.add(course_task)

    task = Task(
        title="| 1.4.13 | Impact",
        description="| 1.4.13 | Impact",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.13",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=102)
    db.session.add(course_task)

    task = Task(
        title="| 1.5 | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology | (U) Hacking Methodology",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.5",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=103)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.1 | Describe the different features, characteristics and common uses for port scanners.",
        description="| 1.5.1 | Describe the different features, characteristics and common uses for port scanners.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.1",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=104)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.2 | (U) Describe protocol tunneling and methods that malicious adversaries can use it. | (U) Describe protocol tun",
        description="| 1.5.2 | (U) Describe protocol tunneling and methods that malicious adversaries can use it. | (U) Describe protocol tunneling and methods that malicious adversaries can use it. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.2",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=105)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.3 | Explain banner grabbing and the information it provides to identify a remote system.",
        description="| 1.5.3 | Explain banner grabbing and the information it provides to identify a remote system.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.3",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=106)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.4 | Explain what a man-in-the-middle attack is and the basic requirements for it.",
        description="| 1.5.4 | Explain what a man-in-the-middle attack is and the basic requirements for it.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.4",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=107)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.5 | Describe ARP spoofing.",
        description="| 1.5.5 | Describe ARP spoofing.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.5",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=108)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.6 | Describe the types of data that would be prioritized by APTs during the post-exploitation phase.",
        description="| 1.5.6 | Describe the types of data that would be prioritized by APTs during the post-exploitation phase.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.6",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=109)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.7 | (U) Describe techniques adversaries would use to exfiltrate data. | (U) Describe techniques adversaries would",
        description="| 1.5.7 | (U) Describe techniques adversaries would use to exfiltrate data. | (U) Describe techniques adversaries would use to exfiltrate data. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.7",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=110)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.8 | Describe the information that can be learned when performing different types of scans?",
        description="| 1.5.8 | Describe the information that can be learned when performing different types of scans?",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.8",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=111)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.9 | Describe how an insecurely configured DNS server that allows external, untrusted zone transfers could provide",
        description="| 1.5.9 | Describe how an insecurely configured DNS server that allows external, untrusted zone transfers could provide information to an attacker.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.9",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=112)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.10 | (U) Describe remote access methods and technologies. | (U) Describe remote access methods and technologies. |",
        description="| 1.5.10 | (U) Describe remote access methods and technologies. | (U) Describe remote access methods and technologies. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.10",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=113)
    db.session.add(course_task)

    task = Task(
        title="| 1.5.11 | (U) Describe common techniques used by an adversary to gain initial access. | (U) Describe common techniques",
        description="| 1.5.11 | (U) Describe common techniques used by an adversary to gain initial access. | (U) Describe common techniques used by an adversary to gain initial access. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.11",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=114)
    db.session.add(course_task)

    task = Task(
        title="| 1.6 | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology | (U) Analyst Methodology",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.6",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=115)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.1 | Describe the following data sources and use cases for each:",
        description="| 1.6.1 | Describe the following data sources and use cases for each:",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.1",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=116)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.2 | Explain the following terms in the context of network analysis.",
        description="| 1.6.2 | Explain the following terms in the context of network analysis.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.2",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=117)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.3 | Explain link analysis and timeline analysis.",
        description="| 1.6.3 | Explain link analysis and timeline analysis.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.3",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=118)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.4 | Explain data stacking and counting, as it pertains to analysis.",
        description="| 1.6.4 | Explain data stacking and counting, as it pertains to analysis.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.4",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=119)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.5 | Explain what a ‘pivot table’ (data summary table) is.",
        description="| 1.6.5 | Explain what a ‘pivot table’ (data summary table) is.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.5",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=120)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.6 | Explain the following aspects of an analysts workflow:",
        description="| 1.6.6 | Explain the following aspects of an analysts workflow:",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.6",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=121)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.7 | (U) Explain what tactics and techniques procedures (TTPs) are. | (U) Explain what tactics and techniques proce",
        description="| 1.6.7 | (U) Explain what tactics and techniques procedures (TTPs) are. | (U) Explain what tactics and techniques procedures (TTPs) are. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.7",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=122)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.8 | (U) Describe the process of converting a technique into an analytic. | (U) Describe the process of converting",
        description="| 1.6.8 | (U) Describe the process of converting a technique into an analytic. | (U) Describe the process of converting a technique into an analytic. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.8",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=123)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.9 | (U) Describe the important information to document in analyst notes? | (U) Describe the important information",
        description="| 1.6.9 | (U) Describe the important information to document in analyst notes? | (U) Describe the important information to document in analyst notes? |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.9",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=124)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.10 | Explain the purpose of a Security Incident and Event Management (SIEM) platform.",
        description="| 1.6.10 | Explain the purpose of a Security Incident and Event Management (SIEM) platform.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.10",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=125)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.11 | Explain what a data model is. Explain the Elastic Common Schema and the Common Information Model.",
        description="| 1.6.11 | Explain what a data model is. Explain the Elastic Common Schema and the Common Information Model.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.11",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=126)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.12 | Define a filter and the following usages when using Kibana.",
        description="| 1.6.12 | Define a filter and the following usages when using Kibana.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.12",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=127)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.13 | Describe how a SIEM interacts with an index and with data buckets.",
        description="| 1.6.13 | Describe how a SIEM interacts with an index and with data buckets.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.13",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=128)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.14 | Explain the purpose of searching and visualizing, dashboards within a SIEM.",
        description="| 1.6.14 | Explain the purpose of searching and visualizing, dashboards within a SIEM.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.14",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=129)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.15 | Explain how the following math functions can be applied during network traffic analysis:",
        description="| 1.6.15 | Explain how the following math functions can be applied during network traffic analysis:",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.15",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=130)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.16 | Describe visualizations found in your SIEM environment and give examples of how to use each.",
        description="| 1.6.16 | Describe visualizations found in your SIEM environment and give examples of how to use each.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.16",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=131)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.17 | Describe the following terms relating to analytics:",
        description="| 1.6.17 | Describe the following terms relating to analytics:",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.17",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=132)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.18 | In addition to the SIEM environment, describe how the following tools can be used to analyze network data:",
        description="| 1.6.18 | In addition to the SIEM environment, describe how the following tools can be used to analyze network data:",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.18",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=133)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.19 | Describe the relationship between forensic artifact and ‘Indicator of Compromise’.",
        description="| 1.6.19 | Describe the relationship between forensic artifact and ‘Indicator of Compromise’.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.19",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=134)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.20 | Discuss the Pyramid of Pain In regards to detection evasion. Describe the difficulty for an adversary to modi",
        description="| 1.6.20 | Discuss the Pyramid of Pain In regards to detection evasion. Describe the difficulty for an adversary to modify a hash, an IP, and a toolkit.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.20",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=135)
    db.session.add(course_task)

    task = Task(
        title="| 1.6.21 | Describe a detection method for each level on the Pyramid of Pain.",
        description="| 1.6.21 | Describe a detection method for each level on the Pyramid of Pain.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.21",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=136)
    db.session.add(course_task)

    task = Task(
        title="| 2.1 | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK) | (U) Packet Capture Analysis Tool (eg. WIRESHARK)",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=137)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.1 | Explain how to set a collection file size at 500MB and why an analyst might do this.",
        description="| 2.1.1 | Explain how to set a collection file size at 500MB and why an analyst might do this.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.1",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=138)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.2 | In what ways can traffic be ingested into the software?",
        description="| 2.1.2 | In what ways can traffic be ingested into the software?",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.2",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=139)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.3 | Explain what type of filter Wireshark uses during live collection and identify what the following Wireshark qu",
        description="| 2.1.3 | Explain what type of filter Wireshark uses during live collection and identify what the following Wireshark queries will look for:",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.3",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=140)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.4 | (U) Explain how to extract a file from HTTP traffic. Explain how to extract a file from any protocol.",
        description="| 2.1.4 | (U) Explain how to extract a file from HTTP traffic. Explain how to extract a file from any protocol.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.4",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=141)
    db.session.add(course_task)

    task = Task(
        title="| 2.1.5 | Explain key differences and similarities between TShark and Wireshark, are they both effective traffic analysi",
        description="| 2.1.5 | Explain key differences and similarities between TShark and Wireshark, are they both effective traffic analysis tools?",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.5",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=142)
    db.session.add(course_task)

    task = Task(
        title="| 2.2 | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump | (U) TCP Dump",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=143)
    db.session.add(course_task)

    task = Task(
        title="| 2.2.1 | How does Tcpdump determine which interface to collect from? How can this be adjusted?",
        description="| 2.2.1 | How does Tcpdump determine which interface to collect from? How can this be adjusted?",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.1",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=144)
    db.session.add(course_task)

    task = Task(
        title="| 2.2.2 | (U) Which type of expression can be used to specify the packets to be dumped? | (U) Which type of expression c",
        description="| 2.2.2 | (U) Which type of expression can be used to specify the packets to be dumped? | (U) Which type of expression can be used to specify the packets to be dumped? |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.2",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=145)
    db.session.add(course_task)

    task = Task(
        title="| 2.2.3 | Explain how to write packets to files of a specific size and why an analyst might do this.",
        description="| 2.2.3 | Explain how to write packets to files of a specific size and why an analyst might do this.",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.3",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=146)
    db.session.add(course_task)

    task = Task(
        title="| 2.2.4 | Explain what the following Tcpdump options would deliver:",
        description="| 2.2.4 | Explain what the following Tcpdump options would deliver:",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.4",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=147)
    db.session.add(course_task)

    task = Task(
        title="| 2.3 | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer | (U) Traffic Analyzer",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=148)
    db.session.add(course_task)

    task = Task(
        title="| 2.3.1 | Explain how a traffic analyzer differs from full packet capture.",
        description="| 2.3.1 | Explain how a traffic analyzer differs from full packet capture.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.1",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=149)
    db.session.add(course_task)

    task = Task(
        title="| 2.3.2 | Explain what relevant log types a traffic analyzer would make and how it would benefit a network analyst.",
        description="| 2.3.2 | Explain what relevant log types a traffic analyzer would make and how it would benefit a network analyst.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.2",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=150)
    db.session.add(course_task)

    task = Task(
        title="| 2.3.3 | Explain how to extract files with a traffic analyzer.",
        description="| 2.3.3 | Explain how to extract files with a traffic analyzer.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.3",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=151)
    db.session.add(course_task)

    task = Task(
        title="| 2.3.4 | (U) Demonstrate how to view and/or analyze the information gathered by a traffic analyzer. | (U) Demonstrate h",
        description="| 2.3.4 | (U) Demonstrate how to view and/or analyze the information gathered by a traffic analyzer. | (U) Demonstrate how to view and/or analyze the information gathered by a traffic analyzer. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.4",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=152)
    db.session.add(course_task)

    task = Task(
        title="| 2.3.5 | In the absence of a visualization tool, what are some ways zeek log can be analyzed?",
        description="| 2.3.5 | In the absence of a visualization tool, what are some ways zeek log can be analyzed?",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.5",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=153)
    db.session.add(course_task)

    task = Task(
        title="| 2.3.6 | (U) Explain how to calculate an MD5 hash using command line tools. What can an analyst do with this informatio",
        description="| 2.3.6 | (U) Explain how to calculate an MD5 hash using command line tools. What can an analyst do with this information? | (U) Explain how to calculate an MD5 hash using command line tools. What can an analyst do with this information? |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.6",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=154)
    db.session.add(course_task)

    task = Task(
        title="| 2.4 | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools | (U) Network Analysis Tools",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=155)
    db.session.add(course_task)

    task = Task(
        title="| 2.4.1 | Describe the following capabilities of Splunk.",
        description="| 2.4.1 | Describe the following capabilities of Splunk.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.1",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=156)
    db.session.add(course_task)

    task = Task(
        title="| 2.4.2 | (U)  Describe the following capabilities of Security Onion.",
        description="| 2.4.2 | (U)  Describe the following capabilities of Security Onion.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.2",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=157)
    db.session.add(course_task)

    task = Task(
        title="| 2.4.3 | (U) Describe the following capabilities of Red Seal.",
        description="| 2.4.3 | (U) Describe the following capabilities of Red Seal.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.3",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=158)
    db.session.add(course_task)

    task = Task(
        title="| 2.4.4 | (U) Describe the following capabilities of Palo Alto.",
        description="| 2.4.4 | (U) Describe the following capabilities of Palo Alto.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.4",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=159)
    db.session.add(course_task)

    task = Task(
        title="| 2.4.5 | Describe the following capabilities of Tanium.",
        description="| 2.4.5 | Describe the following capabilities of Tanium.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.5",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=160)
    db.session.add(course_task)

    task = Task(
        title="| 2.4.6 | (U)  Describe the following capabilities of MDE.",
        description="| 2.4.6 | (U)  Describe the following capabilities of MDE.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.6",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=161)
    db.session.add(course_task)

    task = Task(
        title="| 2.4.7 | Describe the following capabilities of HX.",
        description="| 2.4.7 | Describe the following capabilities of HX.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.7",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=162)
    db.session.add(course_task)

    task = Task(
        title="| 2.5 | (U) Software | (U) Software |  |  |  |  |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.5",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=163)
    db.session.add(course_task)

    task = Task(
        title="| 2.5.3 | Describe the primary functions PowerShell.",
        description="| 2.5.3 | Describe the primary functions PowerShell.",
        grading_type="trainer",
        requires_upload=False,
        label="2.5.3",
        section_label="2.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=164)
    db.session.add(course_task)

    task = Task(
        title="| 2.5.4 | Describe the primary functions Sysinternals.",
        description="| 2.5.4 | Describe the primary functions Sysinternals.",
        grading_type="trainer",
        requires_upload=False,
        label="2.5.4",
        section_label="2.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=165)
    db.session.add(course_task)

    task = Task(
        title="| 2.5.5 | (U) Describe the primary functions of windows native tools.",
        description="| 2.5.5 | (U) Describe the primary functions of windows native tools.",
        grading_type="trainer",
        requires_upload=False,
        label="2.5.5",
        section_label="2.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=166)
    db.session.add(course_task)

    task = Task(
        title="| 3.1 | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery | (U) Network Baselining/Discovery",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=167)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.1 | Given a router configuration, review/analyze the following information:",
        description="| 3.1.1 | Given a router configuration, review/analyze the following information:",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.1",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=168)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.2 | When given multiple router configurations, perform the following:",
        description="| 3.1.2 | When given multiple router configurations, perform the following:",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.2",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=169)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.3 | (U) Demonstrate the ability to analyze a customer’s perimeter defense strategy. | (U) Demonstrate the ability",
        description="| 3.1.3 | (U) Demonstrate the ability to analyze a customer’s perimeter defense strategy. | (U) Demonstrate the ability to analyze a customer’s perimeter defense strategy. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.3",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=170)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.4 | Given the results of a ping sweep and port scan, determine the following:",
        description="| 3.1.4 | Given the results of a ping sweep and port scan, determine the following:",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.4",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=171)
    db.session.add(course_task)

    task = Task(
        title="| 3.1.5 | (U) Analyze the results of a UDP traceroute. | (U) Analyze the results of a UDP traceroute. |  |  |  |  |  |",
        description="| 3.1.5 | (U) Analyze the results of a UDP traceroute. | (U) Analyze the results of a UDP traceroute. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.5",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=172)
    db.session.add(course_task)

    task = Task(
        title="| 3.2 | (U) Troubleshooting | (U) Troubleshooting |  |  |  |  |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=173)
    db.session.add(course_task)

    task = Task(
        title="| 3.2.1 | (U) Demonstrate the ability to identify packet",
        description="| 3.2.1 | (U) Demonstrate the ability to identify packet",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.1",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=174)
    db.session.add(course_task)

    task = Task(
        title="| 3.2.2 | (U) Demonstrate the ability to validate traffic collection, both for missing traffic as well as self-collectio",
        description="| 3.2.2 | (U) Demonstrate the ability to validate traffic collection, both for missing traffic as well as self-collection. | (U) Demonstrate the ability to validate traffic collection, both for missing traffic as well as self-collection. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.2",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=175)
    db.session.add(course_task)

    task = Task(
        title="| 3.2.3 | (U) Demonstrate the ability to communicate connection or access issues to the Crew Lead, this includes recogni",
        description="| 3.2.3 | (U) Demonstrate the ability to communicate connection or access issues to the Crew Lead, this includes recognized data loss. | (U) Demonstrate the ability to communicate connection or access issues to the Crew Lead, this includes recognized data loss. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.3",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=176)
    db.session.add(course_task)

    task = Task(
        title="| 3.2.4 | (U) Demonstrate the ability to troubleshoot information missing from within a SIEM",
        description="| 3.2.4 | (U) Demonstrate the ability to troubleshoot information missing from within a SIEM",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.4",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=177)
    db.session.add(course_task)

    task = Task(
        title="| 3.3 | (U) Performance | (U) Performance |  |  |  |  |  |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=178)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.1 | Given a packet capture, demonstrate the ability to enumerate hosts and collect information about open ports an",
        description="| 3.3.1 | Given a packet capture, demonstrate the ability to enumerate hosts and collect information about open ports and services.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.1",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=179)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.2 | (U) Given a packet capture, demonstrate the ability to analyze individual layers and highlight important field",
        description="| 3.3.2 | (U) Given a packet capture, demonstrate the ability to analyze individual layers and highlight important fields in each layer. | (U) Given a packet capture, demonstrate the ability to analyze individual layers and highlight important fields in each layer. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.2",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=180)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.3 | Demonstrate the ability to conduct netflow analysis of network traffic.",
        description="| 3.3.3 | Demonstrate the ability to conduct netflow analysis of network traffic.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.3",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=181)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.4 | Demonstrate the ability to review/analyze the content of the IP routing table.",
        description="| 3.3.4 | Demonstrate the ability to review/analyze the content of the IP routing table.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.4",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=182)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.5 | Given a packet capture, demonstrate the ability to identify a man-in-the-middle attack.",
        description="| 3.3.5 | Given a packet capture, demonstrate the ability to identify a man-in-the-middle attack.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.5",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=183)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.6 | Given a packet capture, demonstrate the ability to identify ARP spoofing.",
        description="| 3.3.6 | Given a packet capture, demonstrate the ability to identify ARP spoofing.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.6",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=184)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.7 | (U) Given a packet capture, identify DNS tunneling using subdomains. | (U) Given a packet capture, identify DN",
        description="| 3.3.7 | (U) Given a packet capture, identify DNS tunneling using subdomains. | (U) Given a packet capture, identify DNS tunneling using subdomains. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.7",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=185)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.8 | (U) Given a packet capture, identify tunneling using encoded DNS TXT record type. | (U) Given a packet capture",
        description="| 3.3.8 | (U) Given a packet capture, identify tunneling using encoded DNS TXT record type. | (U) Given a packet capture, identify tunneling using encoded DNS TXT record type. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.8",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=186)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.9 | (U) Given a packet capture, identify common types of scans. | (U) Given a packet capture, identify common type",
        description="| 3.3.9 | (U) Given a packet capture, identify common types of scans. | (U) Given a packet capture, identify common types of scans. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.9",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=187)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.10 | (U) Given a packet capture, identify an attacker’s initial intrusion vector into a network. | (U) Given a pac",
        description="| 3.3.10 | (U) Given a packet capture, identify an attacker’s initial intrusion vector into a network. | (U) Given a packet capture, identify an attacker’s initial intrusion vector into a network. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.10",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=188)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.11 | Given a packet capture, identify the following actions of an attacker:",
        description="| 3.3.11 | Given a packet capture, identify the following actions of an attacker:",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.11",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=189)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.12 | (U) Given a packet capture, identify an adversary attempting to maintain persistence on a network. | (U) Give",
        description="| 3.3.12 | (U) Given a packet capture, identify an adversary attempting to maintain persistence on a network. | (U) Given a packet capture, identify an adversary attempting to maintain persistence on a network. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.12",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=190)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.13 | Demonstrate the ability to identify anomalous traffic redirection.",
        description="| 3.3.13 | Demonstrate the ability to identify anomalous traffic redirection.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.13",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=191)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.14 | Given a packet capture, demonstrate the ability to identify anomalous open ports.",
        description="| 3.3.14 | Given a packet capture, demonstrate the ability to identify anomalous open ports.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.14",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=192)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.15 | Given a packet capture, demonstrate the ability to verify VLAN and proxy information by completing the below",
        description="| 3.3.15 | Given a packet capture, demonstrate the ability to verify VLAN and proxy information by completing the below tasking:",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.15",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=193)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.16 | Demonstrate the ability to identify encapsulation types (ex: PPP, Frame Relay, HDLC, CHAP, PAP)",
        description="| 3.3.16 | Demonstrate the ability to identify encapsulation types (ex: PPP, Frame Relay, HDLC, CHAP, PAP)",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.16",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=194)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.17 | (U) Given a packet capture, demonstrate the ability to provide a detailed summary of events. | (U) Given a pa",
        description="| 3.3.17 | (U) Given a packet capture, demonstrate the ability to provide a detailed summary of events. | (U) Given a packet capture, demonstrate the ability to provide a detailed summary of events. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.17",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=195)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.18 | (U) Provide a situational awareness report to a superior. This should include all relevant technical details",
        description="| 3.3.18 | (U) Provide a situational awareness report to a superior. This should include all relevant technical details expected for a final report. | (U) Provide a situational awareness report to a superior. This should include all relevant technical details expected for a final report. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.18",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=196)
    db.session.add(course_task)

    task = Task(
        title="| 3.3.19 | (U) Given a packet capture and a network map, demonstrate the ability to determine the traffic collection loc",
        description="| 3.3.19 | (U) Given a packet capture and a network map, demonstrate the ability to determine the traffic collection location. | (U) Given a packet capture and a network map, demonstrate the ability to determine the traffic collection location. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.19",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=197)
    db.session.add(course_task)

    task = Task(
        title="| 3.4 | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=198)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.1 | (U) Collect raw PCAP using Wireshark. | (U) Collect raw PCAP using Wireshark. |  |  |  |  |  |  |  |  |",
        description="| 3.4.1 | (U) Collect raw PCAP using Wireshark. | (U) Collect raw PCAP using Wireshark. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.1",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=199)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.2 | (U) Collect raw PCAP using TCPdump. | (U) Collect raw PCAP using TCPdump. |  |  |  |  |  |  |  |  |",
        description="| 3.4.2 | (U) Collect raw PCAP using TCPdump. | (U) Collect raw PCAP using TCPdump. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.2",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=200)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.3 | (U) Extract an executable file from a provided PCAP file. | (U) Extract an executable file from a provided PCA",
        description="| 3.4.3 | (U) Extract an executable file from a provided PCAP file. | (U) Extract an executable file from a provided PCAP file. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.3",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=201)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.4 | Demonstrate the ability to perform queries in either Splunk or Kibana, as team appropriate, to detect the foll",
        description="| 3.4.4 | Demonstrate the ability to perform queries in either Splunk or Kibana, as team appropriate, to detect the following:",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.4",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=202)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.5 | Demonstrate the ability to create a dashboard in either Splunk or Kibana, as team appropriate, to capture the",
        description="| 3.4.5 | Demonstrate the ability to create a dashboard in either Splunk or Kibana, as team appropriate, to capture the following:",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.5",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=203)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.6 | (U) Demonstrate the ability to take historical data and generate zeek logs. | (U) Demonstrate the ability to t",
        description="| 3.4.6 | (U) Demonstrate the ability to take historical data and generate zeek logs. | (U) Demonstrate the ability to take historical data and generate zeek logs. |  |  |  |  |  |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.6",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=204)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.7 | (U) Demonstrate the ability to extract a suspicious file from network traffic. Provide all relevant informatio",
        description="| 3.4.7 | (U) Demonstrate the ability to extract a suspicious file from network traffic. Provide all relevant information to supporting CPT elements (host, network, infrastructure,",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.7",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=205)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.8 | Explain/define the following methods/attributes of C2 Beaconing:",
        description="| 3.4.8 | Explain/define the following methods/attributes of C2 Beaconing:",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.8",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=206)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.9 | Explain/define the functions provided by each of the following common SCADA components:",
        description="| 3.4.9 | Explain/define the functions provided by each of the following common SCADA components:",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.9",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=207)
    db.session.add(course_task)

    task = Task(
        title="| 3.4.10 | Explain/define basic cloud concepts and how they apply to DCO-IDM Companies in general to include the followi",
        description="| 3.4.10 | Explain/define basic cloud concepts and how they apply to DCO-IDM Companies in general to include the following:",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.10",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=208)
    db.session.add(course_task)

    task = Task(
        title="| 4.1 | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="4.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=209)
    db.session.add(course_task)

    task = Task(
        title="| 4.1.1 | Explain the function of the following appliances:",
        description="| 4.1.1 | Explain the function of the following appliances:",
        grading_type="trainer",
        requires_upload=False,
        label="4.1.1",
        section_label="4.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=210)
    db.session.add(course_task)

    task = Task(
        title="| 4.1.2 | (U) Explain the following storage concepts and devices:",
        description="| 4.1.2 | (U) Explain the following storage concepts and devices:",
        grading_type="trainer",
        requires_upload=False,
        label="4.1.2",
        section_label="4.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=211)
    db.session.add(course_task)

    task = Task(
        title="| 4.2 | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware | (U) Infrastructure Hardware",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="4.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=212)
    db.session.add(course_task)

    task = Task(
        title="| 4.2.1 | (U) For each of the following hardware pieces",
        description="| 4.2.1 | (U) For each of the following hardware pieces",
        grading_type="trainer",
        requires_upload=False,
        label="4.2.1",
        section_label="4.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=213)
    db.session.add(course_task)

    task = Task(
        title="| 4.3 | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software | (U) Infrastructure Software",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="4.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=214)
    db.session.add(course_task)

    task = Task(
        title="| 4.3.1 | (U) Explain the following analyst tools:",
        description="| 4.3.1 | (U) Explain the following analyst tools:",
        grading_type="trainer",
        requires_upload=False,
        label="4.3.1",
        section_label="4.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=215)
    db.session.add(course_task)

    task = Task(
        title="| 4.3.2 | Explain the differences between the following OS's and hypervisors:",
        description="| 4.3.2 | Explain the differences between the following OS's and hypervisors:",
        grading_type="trainer",
        requires_upload=False,
        label="4.3.2",
        section_label="4.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=216)
    db.session.add(course_task)

    task = Task(
        title="| 4.3.3 | (U) Explain the following traffic capture and analysis software:",
        description="| 4.3.3 | (U) Explain the following traffic capture and analysis software:",
        grading_type="trainer",
        requires_upload=False,
        label="4.3.3",
        section_label="4.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=217)
    db.session.add(course_task)

    task = Task(
        title="| 4.3.5 | Explain the following types of host logs:",
        description="| 4.3.5 | Explain the following types of host logs:",
        grading_type="trainer",
        requires_upload=False,
        label="4.3.5",
        section_label="4.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=218)
    db.session.add(course_task)

    task = Task(
        title="| 4.3.6 | Explain the following SIEM software:",
        description="| 4.3.6 | Explain the following SIEM software:",
        grading_type="trainer",
        requires_upload=False,
        label="4.3.6",
        section_label="4.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=219)
    db.session.add(course_task)

    task = Task(
        title="| 4.4 | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network | (U) Network",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="4.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=220)
    db.session.add(course_task)

    task = Task(
        title="| 4.4.1 | Describe in relation to AAA the following:",
        description="| 4.4.1 | Describe in relation to AAA the following:",
        grading_type="trainer",
        requires_upload=False,
        label="4.4.1",
        section_label="4.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=221)
    db.session.add(course_task)

    task = Task(
        title="| 4.4.2 | (U) Explain the different firewall types, benefits, and limitations in regards to the kit:",
        description="| 4.4.2 | (U) Explain the different firewall types, benefits, and limitations in regards to the kit:",
        grading_type="trainer",
        requires_upload=False,
        label="4.4.2",
        section_label="4.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=222)
    db.session.add(course_task)

    task = Task(
        title="| What are an IDS and IPS?",
        description="| What are an IDS and IPS?",
        grading_type="trainer",
        requires_upload=False,
        label="4.4.3",
        section_label="4.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=223)
    db.session.add(course_task)

    db.session.commit()

# === Network Senior ===
course = Course.query.filter_by(name="Network Senior").first()
if course:
    task = Task(
        title="| (U) Vulnerability Assessment/Security Audit | (U) Vulnerability Assessment/Security Audit |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=1)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate formulating a plan or analysis and risk mitigation using the following mission documentation:",
        description="| Demonstrate formulating a plan or analysis and risk mitigation using the following mission documentation:",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.1",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=2)
    db.session.add(course_task)

    task = Task(
        title="| Identify key cyber terrain which if seized, afford an advantage to an attacker or defender.",
        description="| Identify key cyber terrain which if seized, afford an advantage to an attacker or defender.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.2",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=3)
    db.session.add(course_task)

    task = Task(
        title="| (U) Identify critical or high-risk accounts that",
        description="| (U) Identify critical or high-risk accounts that",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.3",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=4)
    db.session.add(course_task)

    task = Task(
        title="| (U) Provide examples of information that is obtained by scanning a customer’s network. Explain the information that is",
        description="| (U) Provide examples of information that is obtained by scanning a customer’s network. Explain the information that is obtained from the scan. Each example provided needs a required tool. Identify potential obstacles/considerations that could affect scans.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.4",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=5)
    db.session.add(course_task)

    task = Task(
        title="| Provide a scan that will produce operating system, version number, and open ports for a number of hosts.",
        description="| Provide a scan that will produce operating system, version number, and open ports for a number of hosts.",
        grading_type="trainer",
        requires_upload=False,
        label="1.1.5",
        section_label="1.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=6)
    db.session.add(course_task)

    task = Task(
        title="| (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance | (U) Adversary Reconnaissance",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=7)
    db.session.add(course_task)

    task = Task(
        title="| Describe the following reconnaissance methods from Mitre ATT&CK, how it could appear in network traffic, and where to",
        description="| Describe the following reconnaissance methods from Mitre ATT&CK, how it could appear in network traffic, and where to look in your tool set:",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.1",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=8)
    db.session.add(course_task)

    task = Task(
        title="| Describe the utility of social engineering for reconnaissance.",
        description="| Describe the utility of social engineering for reconnaissance.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.2",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=9)
    db.session.add(course_task)

    task = Task(
        title="| Explain what web scraping is, why an attacker would do it, and how it looks in network traffic.",
        description="| Explain what web scraping is, why an attacker would do it, and how it looks in network traffic.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.3",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=10)
    db.session.add(course_task)

    task = Task(
        title="| Explain the information attackers could gather from a DNS zone transfer and what would be observable in network traffi",
        description="| Explain the information attackers could gather from a DNS zone transfer and what would be observable in network traffic.",
        grading_type="trainer",
        requires_upload=False,
        label="1.2.4",
        section_label="1.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=11)
    db.session.add(course_task)

    task = Task(
        title="| (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation | (U) Initial Exploitation",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=12)
    db.session.add(course_task)

    task = Task(
        title="| Describe the following initial exploitation methods from Mitre ATT&CK, how it could appear in network traffic, and whe",
        description="| Describe the following initial exploitation methods from Mitre ATT&CK, how it could appear in network traffic, and where to look in your tool set:",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.1",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=13)
    db.session.add(course_task)

    task = Task(
        title="| Describe the protocols/services that are most commonly targeted for attacks. (ex: Brute force, etc.).",
        description="| Describe the protocols/services that are most commonly targeted for attacks. (ex: Brute force, etc.).",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.2",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=14)
    db.session.add(course_task)

    task = Task(
        title="| Explain the following attacks and their indicators.",
        description="| Explain the following attacks and their indicators.",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.3",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=15)
    db.session.add(course_task)

    task = Task(
        title="| Identify and explain various adversarial TTPs that are utilized for initial exploitation of networks. (ex: . Watering",
        description="| Identify and explain various adversarial TTPs that are utilized for initial exploitation of networks. (ex: . Watering Hole, URL shortening).",
        grading_type="trainer",
        requires_upload=False,
        label="1.3.4",
        section_label="1.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=16)
    db.session.add(course_task)

    task = Task(
        title="| (U) Actions on Target | (U) Actions on Target | (U) Actions on Target | (U) Actions on Target | (U) Actions on Target",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=17)
    db.session.add(course_task)

    task = Task(
        title="| Give examples of the following actions on target, their purpose, what they may present as in network traffic, and what",
        description="| Give examples of the following actions on target, their purpose, what they may present as in network traffic, and what tool you would use to identify them?",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.1",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=18)
    db.session.add(course_task)

    task = Task(
        title="| Explain Windows Remote Management",
        description="| Explain Windows Remote Management",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.2",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=19)
    db.session.add(course_task)

    task = Task(
        title="| Explain SchTasks, what ports it uses, and why an attacker would use it.",
        description="| Explain SchTasks, what ports it uses, and why an attacker would use it.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.3",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=20)
    db.session.add(course_task)

    task = Task(
        title="| Explain Windows Management Instrumentation (WMI), what ports it uses, and why an attacker would use it.",
        description="| Explain Windows Management Instrumentation (WMI), what ports it uses, and why an attacker would use it.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.4",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=21)
    db.session.add(course_task)

    task = Task(
        title="| Explain BITS Job, what ports it uses, and why an attacker would use it.",
        description="| Explain BITS Job, what ports it uses, and why an attacker would use it.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.5",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=22)
    db.session.add(course_task)

    task = Task(
        title="| Explain domain fronting and how APTs utilize it to hide malicious activity.",
        description="| Explain domain fronting and how APTs utilize it to hide malicious activity.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.6",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=23)
    db.session.add(course_task)

    task = Task(
        title="| Describe where in a HTTP request an actor can hide C2 and data exfiltration.",
        description="| Describe where in a HTTP request an actor can hide C2 and data exfiltration.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.7",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=24)
    db.session.add(course_task)

    task = Task(
        title="| Explain regular web connection. Describe anomalous behaviors and the implications.",
        description="| Explain regular web connection. Describe anomalous behaviors and the implications.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.8",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=25)
    db.session.add(course_task)

    task = Task(
        title="| Identify types of DNS records, explain vulnerabilities, exploitations, and how it relates to network security.",
        description="| Identify types of DNS records, explain vulnerabilities, exploitations, and how it relates to network security.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.9",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=26)
    db.session.add(course_task)

    task = Task(
        title="| Explain how entropy relates to DNS in regards to network analysis?",
        description="| Explain how entropy relates to DNS in regards to network analysis?",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.10",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=27)
    db.session.add(course_task)

    task = Task(
        title="| (U) Explain how DNS is used for C2 or data exfiltration?",
        description="| (U) Explain how DNS is used for C2 or data exfiltration?",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.11",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=28)
    db.session.add(course_task)

    task = Task(
        title="| Explain what should be evaluated when looking at a customer’s mapped network drives.",
        description="| Explain what should be evaluated when looking at a customer’s mapped network drives.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.12",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=29)
    db.session.add(course_task)

    task = Task(
        title="| Describe which file types, commands, and actions are indicative of SMB lateral movement.",
        description="| Describe which file types, commands, and actions are indicative of SMB lateral movement.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.13",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=30)
    db.session.add(course_task)

    task = Task(
        title="| Explain the functions of the Windows Service Controller and how it can be leveraged remotely over SMB.",
        description="| Explain the functions of the Windows Service Controller and how it can be leveraged remotely over SMB.",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.14",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=31)
    db.session.add(course_task)

    task = Task(
        title="| Using network traffic explain how an analyst could find credential attacks or lateral movement:",
        description="| Using network traffic explain how an analyst could find credential attacks or lateral movement:",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.15",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=32)
    db.session.add(course_task)

    task = Task(
        title="| Describe adversarial anti-detection methods and how to identify them in network traffic",
        description="| Describe adversarial anti-detection methods and how to identify them in network traffic",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.16",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=33)
    db.session.add(course_task)

    task = Task(
        title="| Explain/define physical and digital ICS/SCADA components/concepts:",
        description="| Explain/define physical and digital ICS/SCADA components/concepts:",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.17",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=34)
    db.session.add(course_task)

    task = Task(
        title="| (U) Explain/define IOT. |  |  |  |",
        description="| (U) Explain/define IOT. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.18",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=35)
    db.session.add(course_task)

    task = Task(
        title="| Explain/define following cloud environments:",
        description="| Explain/define following cloud environments:",
        grading_type="trainer",
        requires_upload=False,
        label="1.4.19",
        section_label="1.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=36)
    db.session.add(course_task)

    task = Task(
        title="| (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies | (U) Utilization of DCO-IDM Resources/Policies",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.5",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=37)
    db.session.add(course_task)

    task = Task(
        title="| Discuss what Intel teams can and should provide you as a Network analyst during a mission",
        description="| Discuss what Intel teams can and should provide you as a Network analyst during a mission",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.1",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=38)
    db.session.add(course_task)

    task = Task(
        title="| Discuss what Host teams can and should provide you as a Network analyst during a mission",
        description="| Discuss what Host teams can and should provide you as a Network analyst during a mission",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.2",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=39)
    db.session.add(course_task)

    task = Task(
        title="| Discuss what Network Technician teams can and should provide you as a Network analyst during a mission.",
        description="| Discuss what Network Technician teams can and should provide you as a Network analyst during a mission.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.3",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=40)
    db.session.add(course_task)

    task = Task(
        title="| Discuss how in the role of a lead Network analyst you might interface within the CPT leadership structure",
        description="| Discuss how in the role of a lead Network analyst you might interface within the CPT leadership structure",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.4",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=41)
    db.session.add(course_task)

    task = Task(
        title="| Discuss how in the role of a lead Network analyst you might interface with the customer",
        description="| Discuss how in the role of a lead Network analyst you might interface with the customer",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.5",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=42)
    db.session.add(course_task)

    task = Task(
        title="| Discuss the circumstances in which you may need to interface with local CI or law enforcement agencies.",
        description="| Discuss the circumstances in which you may need to interface with local CI or law enforcement agencies.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.6",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=43)
    db.session.add(course_task)

    task = Task(
        title="| Identify the JOPP.",
        description="| Identify the JOPP.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.7",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=44)
    db.session.add(course_task)

    task = Task(
        title="| Explain the purpose of the following documents:",
        description="| Explain the purpose of the following documents:",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.8",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=45)
    db.session.add(course_task)

    task = Task(
        title="| Explain the 2nd party and 3rd party policies that impact dissemination and where you will find them.",
        description="| Explain the 2nd party and 3rd party policies that impact dissemination and where you will find them.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.9",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=46)
    db.session.add(course_task)

    task = Task(
        title="| Explain the difference between Cyberspace authorities and SIGINT authorities.",
        description="| Explain the difference between Cyberspace authorities and SIGINT authorities.",
        grading_type="trainer",
        requires_upload=False,
        label="1.5.10",
        section_label="1.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=47)
    db.session.add(course_task)

    task = Task(
        title="| (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team) | (U) Utilization of Threat Hunting Tools (Tools are unique to service and team)",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="1.6",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=48)
    db.session.add(course_task)

    task = Task(
        title="| Describe the role of the following Zeek logs during network analysis.",
        description="| Describe the role of the following Zeek logs during network analysis.",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.1",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=49)
    db.session.add(course_task)

    task = Task(
        title="| Which Windows event logs are most relevant to network analysis?",
        description="| Which Windows event logs are most relevant to network analysis?",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.2",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=50)
    db.session.add(course_task)

    task = Task(
        title="| If given a list of IOCs to hunt for, which selectors are most relevant to network analysis? Which selectors are more r",
        description="| If given a list of IOCs to hunt for, which selectors are most relevant to network analysis? Which selectors are more relevant to host analysis?",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.3",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=51)
    db.session.add(course_task)

    task = Task(
        title="| During analysis, describe some selectors that, if discovered should be given to host analysts to leverage",
        description="| During analysis, describe some selectors that, if discovered should be given to host analysts to leverage",
        grading_type="trainer",
        requires_upload=False,
        label="1.6.4",
        section_label="1.6",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=52)
    db.session.add(course_task)

    task = Task(
        title="| 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata | 2.1 (U) Snort/Suricata",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=53)
    db.session.add(course_task)

    task = Task(
        title="| Explain how IDSs are utilized by CPTs.",
        description="| Explain how IDSs are utilized by CPTs.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.1",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=54)
    db.session.add(course_task)

    task = Task(
        title="| Explain how rules are developed and employed by IDS.",
        description="| Explain how rules are developed and employed by IDS.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.2",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=55)
    db.session.add(course_task)

    task = Task(
        title="| Explain the different ways to monitor IDS alerts.",
        description="| Explain the different ways to monitor IDS alerts.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.3",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=56)
    db.session.add(course_task)

    task = Task(
        title="| Identify the location of IDS logs.",
        description="| Identify the location of IDS logs.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.4",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=57)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate or explain how to filter on content in network traffic using an IDS rule.",
        description="| Demonstrate or explain how to filter on content in network traffic using an IDS rule.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.5",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=58)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate how to make a variable and explain how it could be utilized within an IDS.",
        description="| Demonstrate how to make a variable and explain how it could be utilized within an IDS.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.6",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=59)
    db.session.add(course_task)

    task = Task(
        title="| Explain the process of using selectors/IOCs to create relevant signatures on mission.",
        description="| Explain the process of using selectors/IOCs to create relevant signatures on mission.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.7",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=60)
    db.session.add(course_task)

    task = Task(
        title="| Explain the importance of labeling and categorizing rules within an IDS.",
        description="| Explain the importance of labeling and categorizing rules within an IDS.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.8",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=61)
    db.session.add(course_task)

    task = Task(
        title="| Explain considerations that should be taken when tuning an IDS and explain some effective ways to eliminate false posi",
        description="| Explain considerations that should be taken when tuning an IDS and explain some effective ways to eliminate false positives. (HDD space, traffic load, collection strategy, relevant/irrelevant traffic, etc.)",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.9",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=62)
    db.session.add(course_task)

    task = Task(
        title="| How can a network analyst configure",
        description="| How can a network analyst configure",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.10",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=63)
    db.session.add(course_task)

    task = Task(
        title="| What does the “flow” keyword do and why would an analyst use it?",
        description="| What does the “flow” keyword do and why would an analyst use it?",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.11",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=64)
    db.session.add(course_task)

    task = Task(
        title="| Explain the purpose of each of the following rules.",
        description="| Explain the purpose of each of the following rules.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.12",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=65)
    db.session.add(course_task)

    task = Task(
        title="| Explain the process of discovering selectors/IOCs while on mission, and then creating relevant signatures to combat th",
        description="| Explain the process of discovering selectors/IOCs while on mission, and then creating relevant signatures to combat them.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.13",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=66)
    db.session.add(course_task)

    task = Task(
        title="| Write a Snort rule using a variable that alerts if IRC ports 6667-7001 are being used.",
        description="| Write a Snort rule using a variable that alerts if IRC ports 6667-7001 are being used.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.14",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=67)
    db.session.add(course_task)

    task = Task(
        title="| Write a Snort rule using a variable that alerts on communications to or from badwebsite.com.",
        description="| Write a Snort rule using a variable that alerts on communications to or from badwebsite.com.",
        grading_type="trainer",
        requires_upload=False,
        label="2.1.15",
        section_label="2.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=68)
    db.session.add(course_task)

    task = Task(
        title="| (U) SIEM | (U) SIEM | (U) SIEM | (U) SIEM | (U) SIEM",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=69)
    db.session.add(course_task)

    task = Task(
        title="| Write queries to find the following items:",
        description="| Write queries to find the following items:",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.1",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=70)
    db.session.add(course_task)

    task = Task(
        title="| Using Windows logs, identify brute force attacks",
        description="| Using Windows logs, identify brute force attacks",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.2",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=71)
    db.session.add(course_task)

    task = Task(
        title="| Using Windows logs, identify lateral movement.",
        description="| Using Windows logs, identify lateral movement.",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.3",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=72)
    db.session.add(course_task)

    task = Task(
        title="| Explain the process for importing data into SIEM.",
        description="| Explain the process for importing data into SIEM.",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.4",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=73)
    db.session.add(course_task)

    task = Task(
        title="| Explain a mission scenario in which you would create a dashboard, and why you would choose those specific queries.",
        description="| Explain a mission scenario in which you would create a dashboard, and why you would choose those specific queries.",
        grading_type="trainer",
        requires_upload=False,
        label="2.2.5",
        section_label="2.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=74)
    db.session.add(course_task)

    task = Task(
        title="| (U) PCAP | (U) PCAP | (U) PCAP | (U) PCAP | (U) PCAP",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=75)
    db.session.add(course_task)

    task = Task(
        title="| Create a filter for a subnet.",
        description="| Create a filter for a subnet.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.1",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=76)
    db.session.add(course_task)

    task = Task(
        title="| Create a filter to look for a specific URL.",
        description="| Create a filter to look for a specific URL.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.2",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=77)
    db.session.add(course_task)

    task = Task(
        title="| Create a filter that would include multiple TCP ports.",
        description="| Create a filter that would include multiple TCP ports.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.3",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=78)
    db.session.add(course_task)

    task = Task(
        title="| Create a filter for an IP range.",
        description="| Create a filter for an IP range.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.4",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=79)
    db.session.add(course_task)

    task = Task(
        title="| What's the difference between capture filters and display filters? When would each be used?",
        description="| What's the difference between capture filters and display filters? When would each be used?",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.6",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=80)
    db.session.add(course_task)

    task = Task(
        title="| Create a display filter to find HTTP GET requests. Why would an analyst do this?",
        description="| Create a display filter to find HTTP GET requests. Why would an analyst do this?",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.7",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=81)
    db.session.add(course_task)

    task = Task(
        title="| Create a display filter using the membership operator to look for DELETE, CONNECT, HEAD, PUT, or TRACE HTTP methods. W",
        description="| Create a display filter using the membership operator to look for DELETE, CONNECT, HEAD, PUT, or TRACE HTTP methods. Why would an analyst do this?",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.8",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=82)
    db.session.add(course_task)

    task = Task(
        title="| Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"not ip.addr eq 192.168.1.10\"?",
        description="| Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"not ip.addr eq 192.168.1.10\"?",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.9",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=83)
    db.session.add(course_task)

    task = Task(
        title="| Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"!(ip.addr == 192.168.1.10)\"?",
        description="| Is there a difference between display filters \"ip.addr!=192.168.1.10\" and \"!(ip.addr == 192.168.1.10)\"?",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.10",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=84)
    db.session.add(course_task)

    task = Task(
        title="| Is there a difference between display filters \"!(ip.addr == 192.168.1.10)\" and \"not ip.addr eq 192.168.1.10\"?",
        description="| Is there a difference between display filters \"!(ip.addr == 192.168.1.10)\" and \"not ip.addr eq 192.168.1.10\"?",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.11",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=85)
    db.session.add(course_task)

    task = Task(
        title="| Explain how to use PCAP to verify sensor placement.",
        description="| Explain how to use PCAP to verify sensor placement.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.12",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=86)
    db.session.add(course_task)

    task = Task(
        title="| Explain how to utilize PCAP to validate a customer’s network documentation.",
        description="| Explain how to utilize PCAP to validate a customer’s network documentation.",
        grading_type="trainer",
        requires_upload=False,
        label="2.3.13",
        section_label="2.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=87)
    db.session.add(course_task)

    task = Task(
        title="| (U) Additional Tools | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools | (U) Additional Tools",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="2.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=88)
    db.session.add(course_task)

    task = Task(
        title="| What is JA3?",
        description="| What is JA3?",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.1",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=89)
    db.session.add(course_task)

    task = Task(
        title="| What is JA3S?",
        description="| What is JA3S?",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.2",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=90)
    db.session.add(course_task)

    task = Task(
        title="| Describe how JA3 and JA3S create fingerprints.",
        description="| Describe how JA3 and JA3S create fingerprints.",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.3",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=91)
    db.session.add(course_task)

    task = Task(
        title="| Why would a network analyst use JA3?",
        description="| Why would a network analyst use JA3?",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.4",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=92)
    db.session.add(course_task)

    task = Task(
        title="| How can https://sslbl.abuse.ch/ be utilized by a network analyst?",
        description="| How can https://sslbl.abuse.ch/ be utilized by a network analyst?",
        grading_type="trainer",
        requires_upload=False,
        label="2.4.5",
        section_label="2.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=93)
    db.session.add(course_task)

    task = Task(
        title="| (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement | (U) Sensor Placement",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.1",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=94)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate the ability to develop a sensor placement strategy based on a scoping document, and a provided network",
        description="| (U) Demonstrate the ability to develop a sensor placement strategy based on a scoping document, and a provided network map. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.1",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=95)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate the ability to develop a sensor placement strategy based on knowledge gaps in traffic results. |  |  |",
        description="| (U) Demonstrate the ability to develop a sensor placement strategy based on knowledge gaps in traffic results. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.1.2",
        section_label="3.1",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=96)
    db.session.add(course_task)

    task = Task(
        title="| (U) Security Recommendations |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.2",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=97)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate the ability to analyze the network map/network traffic of a customer and provide best practices or sec",
        description="| (U) Demonstrate the ability to analyze the network map/network traffic of a customer and provide best practices or security recommendations. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.1",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=98)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate how in the role as a Network Lead, what actions would take if a vulnerability is discovered on the cus",
        description="| (U) Demonstrate how in the role as a Network Lead, what actions would take if a vulnerability is discovered on the customer’s network. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.2",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=99)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate the ability to create security recommendations that highlight the priority level of each security risk",
        description="| (U) Demonstrate the ability to create security recommendations that highlight the priority level of each security risk discovered as a result of analysis. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.3",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=100)
    db.session.add(course_task)

    task = Task(
        title="| Provide security recommendations for the following security risks:",
        description="| Provide security recommendations for the following security risks:",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.4",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=101)
    db.session.add(course_task)

    task = Task(
        title="| Explain appropriate briefing. Describe the kinds of information a network analyst should provide to a Team Lead or Mis",
        description="| Explain appropriate briefing. Describe the kinds of information a network analyst should provide to a Team Lead or Mission Partner.",
        grading_type="trainer",
        requires_upload=False,
        label="3.2.5",
        section_label="3.2",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=102)
    db.session.add(course_task)

    task = Task(
        title="| (U) Signature Creation |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.3",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=103)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate the ability to, from traffic, identify selectors to create IOC signatures for, and create said signatu",
        description="| (U) Demonstrate the ability to, from traffic, identify selectors to create IOC signatures for, and create said signatures. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.1",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=104)
    db.session.add(course_task)

    task = Task(
        title="| Demonstrate the ability to create signatures for future detection.",
        description="| Demonstrate the ability to create signatures for future detection.",
        grading_type="trainer",
        requires_upload=False,
        label="3.3.2",
        section_label="3.3",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=105)
    db.session.add(course_task)

    task = Task(
        title="| (U) Capture Network Traffic |  |  |  |",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.4",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=106)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate the ability to formulate a data collection plan and defend a proposed mission. |  |  |  |",
        description="| (U) Demonstrate the ability to formulate a data collection plan and defend a proposed mission. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.4.1",
        section_label="3.4",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=107)
    db.session.add(course_task)

    task = Task(
        title="| (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic | (U) Capture Network Traffic",
        description="",
        grading_type="trainer",
        requires_upload=False,
        label="3.5",
        section_label="",
        is_section_header=True
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=108)
    db.session.add(course_task)

    task = Task(
        title="| (U) Demonstrate mission execution from customer contact to drafting of an AAR. |  |  |  |",
        description="| (U) Demonstrate mission execution from customer contact to drafting of an AAR. |  |  |  |",
        grading_type="trainer",
        requires_upload=False,
        label="3.5.1",
        section_label="3.5",
        is_section_header=False
    )
    db.session.add(task)
    db.session.flush()
    course_task = CourseTask(course_id=course.id, task_id=task.id, sequence=109)
    db.session.add(course_task)

    db.session.commit()
