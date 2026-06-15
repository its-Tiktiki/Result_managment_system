from flask import Blueprint,redirect,render_template,session,url_for

assign_subject_dashboard_bp = Blueprint(
    "assign_subject_dashboard",
    __name__,
    url_prefix="/assign_subject_dashboard"
)

@assign_subject_dashboard_bp.route("assign_subject_dashboard")
def assign_subject_dashboard():
       
    if not session.get("principal"):
        return redirect(url_for("login.login"))
    
    return render_template("principal/assign_subject_dashboard.html")