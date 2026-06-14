from flask import Blueprint,redirect,render_template,url_for,session
from app.models.principal import TeacherAddInfo

teacher_details_bp = Blueprint(
    "teacher_details",
    __name__,
    url_prefix="/teacher_details"
)

@teacher_details_bp.route("/principal/<int:teacher_id>")
def teacher_details(teacher_id):

    if not session.get("principal"):
        return redirect(url_for("login.login"))
    
    teacher = TeacherAddInfo.query.get_or_404(teacher_id)

    return render_template(
        "principal/teacher_details.html",
        teacher = teacher
    )
    

    
