from flask import Blueprint,redirect,url_for,session,render_template,flash
from app.models.assign import Department,Subjects

show_subjects_bp = Blueprint(
    "show_subjects",
    __name__,
    url_prefix="/show_subjects"
)

@show_subjects_bp.route("/")
def show_department():
    if not session.get("principal_id"):
        return redirect(url_for("login.login"))
    
    principal_id = session.get("principal_id")

    all_department = Department.query.filter_by(
        principal_id=principal_id
    ).all()

    return render_template(
        "principal/subject_and_department/show_department.html",
        all_department=all_department
    )
    

@show_subjects_bp.route("/show_subjects")
def show_subjects():
    if not session.get("principal_id"):
        return redirect(url_for("login.login"))
    
    principal_id = session.get("principal_id")

    all_subject = Subjects.query.filter_by(
        principal_id=principal_id
    ).all()

    return render_template(
        "principal/subject_and_department/show_subjects.html",
        all_subject=all_subject
    )