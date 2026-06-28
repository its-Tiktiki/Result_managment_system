from flask import Blueprint,redirect,url_for,render_template,session

get_marks_dashboard_bp = Blueprint(
    "get_marks_dashboard",
    __name__,
    url_prefix="/get_marks_dashboard"
)

@get_marks_dashboard_bp.route("/")
def get_marks_dashboard():
    if not session.get("teacher"):
        return redirect(url_for("login.login"))
    
    return render_template("teacher/get_marks_system/get_marks_dashboard.html")