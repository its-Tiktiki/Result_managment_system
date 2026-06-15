from flask import Blueprint,redirect,url_for,render_template,flash,session
from app.utils.assign_form import DepartmentForm,SubjectForm
from app.extensions import db
from app.models.principal import Department,Subjects

assign_subject_bp = Blueprint(
    "assign_subject",
    __name__,
    url_prefix="/assign_subject"
)

@assign_subject_bp.route("/add_department", methods=["GET", "POST"])
def add_department():

    if not session.get("principal"):
        return redirect(url_for("login.login"))
    
    form = DepartmentForm()

    if form.validate_on_submit():
        department_id = form.department_id.data
        department_name = form.department_name.data

        department = Department(
            department_id = department_id,
            department_name = department_name
        )

        db.session.add(department)
        db.session.commit()

        flash("Departmet Add successfully","success")

        return redirect(url_for("assign_subject_dashboard.assign_subject_dashboard"))
    
    return render_template("principal/add_department.html",form=form)


@assign_subject_bp.route("add_subject",methods=["GET","POST"])
def add_subject():

    if not session.get("principal"):
        return redirect(url_for("login.login"))
    
    form = SubjectForm()
    departments = Department.query.all()

    form.department_id.choices = [
        (
            dept.department_id,
            dept.department_name
        )

        for dept in departments
    ]


    if form.validate_on_submit():
        subject = Subjects(
            subject_code = form.subject_code.data,
            subject_name = form.subject_name.data,
            semester = form.semester.data,
            department_id = form.department_id.data
        )

        db.session.add(subject)
        db.session.commit()

        flash("Subject added successfully","success")
        return redirect(url_for("assign_subject_dashboard.assign_subject_dashboard"))
    
    return render_template(
        "principal/add_subject.html",
        form=form
    )