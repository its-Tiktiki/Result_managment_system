from flask import Blueprint,redirect,url_for,render_template,session,flash
from app.models.principal import TeacherAddInfo

principal_dashboard_bp = Blueprint("principal_dashboard",__name__,url_prefix="/ptincipal_dashboard")
@principal_dashboard_bp.route("/")

def principal_dashboard():
    
    if not session.get("principal"):
        return redirect(url_for("login.login"))

    principal_id = session.get("principal_id")

    total_teachers = TeacherAddInfo.query.filter_by(
        principal_id=principal_id
    ).count()

    return render_template(
        "principal/principal_dashboard.html",
        total_teachers=total_teachers
    )