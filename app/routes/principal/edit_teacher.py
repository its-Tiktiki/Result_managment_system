from flask import Blueprint, redirect, url_for, session, render_template
from app.models.principal import TeacherAddInfo
from app.utils.principalForm import AddTecaherForm

edit_tecaher_bp = Blueprint(
    "edit_teacher",
    __name__,
    url_prefix="/edit_teacher"
)

@edit_tecaher_bp.route("/")
def edit_tecaher_view():
    if not session.get("principal"):
        return redirect(url_for("login.login"))

    principal_id = session.get("principal_id")

    teachers_data = TeacherAddInfo.query.filter_by(
        principal_id=principal_id
    ).all()

    return render_template(
        "principal/edit_teacher_view.html",
        teachers_data=teachers_data
    )


@edit_tecaher_bp.route("/principal/<int:teacher_id>/edit",methods=["GET","POST"])
def edit_teacher(teacher_id):
    teacher =TeacherAddInfo.query.get_or_404(teacher_id)
    form = AddTecaherForm(obj=teacher)

    if form.validate_on_submit():
        