from webbrowser import get

from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models import teacher
from app.models.teacher import AddStudentInfo,MarksTopic
from app.models.assign import Department
from app.utils.add_student_form import SelectSemesterAndDepartmentForm
from app.utils.marks_forms import MarksTopicForm
from app.extensions import db

get_marks_bp = Blueprint(
    "get_marks",
    __name__,
    url_prefix="/get_marks"
)

@get_marks_bp.route("/", methods=["GET", "POST"])
def show_student():

    if not session.get("teacher"):
        return redirect(url_for("login.login"))

    form = SelectSemesterAndDepartmentForm()

    teacher_id = session.get("teacher_id")
    principal_id = session.get("temp_principal_id")   

    departments = Department.query.filter_by(
        principal_id=principal_id
    ).all()

    form.department_id.choices = [
        (d.department_id, f"{d.department_code} - {d.department_name}")
        for d in departments
    ]

    students = AddStudentInfo.query.filter_by(
        teacher_id=teacher_id
    ).all()

    form.semester.choices = [
        (s, f"Semester {s}")
        for s in sorted({x.semester for x in students})
    ]

    form.group.choices = [
        (g, g)
        for g in sorted({x.group for x in students if x.group})
    ]

    student_data = []

    if form.validate_on_submit():

        student_data = AddStudentInfo.query.filter_by(
            teacher_id=teacher_id,
            department_id=form.department_id.data,
            semester=form.semester.data,
            group=form.group.data
        ).all()

    return render_template(
        "teacher/get_marks_system/get_marks_views.html",
        form=form,
        student_data=student_data
    )

@get_marks_bp.route("/",methods=["GET","POST"])
def get_marks_topic_name():
    if not session.get("teacher"):
        return redirect(url_for("login.login"))
    
    form = MarksTopicForm()
    if form.validate_on_submit():
        teacher_id = session.get("teacher_id")

        marks_topic = MarksTopic(
            marks_topic_name=form.add_marks_topic_name.data,
            teacher_id=teacher_id
        )

        db.session.add(marks_topic)
        db.session.commit()
        flash("Marks topic added successfully","success")

        return redirect(url_for("get_marks.get_marks_topic_name"))
    
    return render_template(
        "teacher/get_marks_system/add_marks_topic.html",
        form=form
    )


@get_marks_bp.route("/show_marks_system")
def show_marks_system():
    if not session.get("teacher"):
        return redirect(url_for("login.login"))
    
    teacher_id = session.get("teacher_id")
    marks_topic_name = MarksTopic.query.filter_by(
        teacher_id=teacher_id
    ).all()

    return render_template(
        "teacher/get_marks_system/show_marks_system.html",
        marks_topic_name=marks_topic_name
    )
