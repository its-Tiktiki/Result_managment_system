from flask import Blueprint, redirect, render_template, request, url_for, flash,session
from app.utils.form import LoginForm
from app.extensions import db
from app.models.admin import Admin
from app.models.admin import PrincipalDataInfo

# save default password
DEFUALT_USERNAME = "admin"
DEFUALT_PASSWORD = "admin123"

# make blueprint and route
login_bp = Blueprint("login", __name__, url_prefix="/login")

@login_bp.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        # Check Admin table
        admin = Admin.query.filter_by(
            username=username,
            password=password
        ).first()

        if username == DEFUALT_USERNAME and password == DEFUALT_PASSWORD:
            session["admin"] = True
            flash("Admin login successful!", "success")
            return redirect(url_for("admin_dashboard.admin_dashboard"))

        # Check Principal table
        principal = PrincipalDataInfo.query.filter_by(
            username=username,
            password=password
        ).first()

        if principal:
            session["principal"] = True
            session["principal_id"] = principal.principal_id
            session["principal_id"] = principal.principal_id

            flash(f"Login successful, welcome {principal.first_name}","success")

            return redirect(url_for("principal_dashboard.principal_dashboard"))

        flash("Invalid username or password", "danger")

    return render_template(
        "auth/login.html",
        login_form=login_form,
    )

@login_bp.route("/logout")
def logout():
    session.pop("admin", None)  # Remove admin session
    flash("Logged out successfully!", "success")
    return redirect(url_for("login.login"))