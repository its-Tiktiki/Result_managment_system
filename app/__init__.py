from flask import Flask
from .config import Config
from .extensions import db


def create_app(): 
    app = Flask(__name__) 
    app.config.from_object(Config)
    db.init_app(app) 

    from .routes.student.home import home_bp
    from .routes.auth.login import login_bp 
    from .routes.admin.admin_dashboard import admin_bp 
    from .routes.admin.add_principal import add_principal_bp 
    from .routes.principal.principal_dashboard import principal_dashboard_bp 
    from .routes.principal.add_teacher import add_teacher_bp 
    from .routes.principal.view_teachers import views_teacher_bp 
    from .routes.principal.teacher_details import teacher_details_bp
    from .routes.principal.edit_teacher import edit_tecaher_bp
    from .routes.principal.subject_and_department.assign_subjects import assign_subject_bp 
    from .routes.principal.subject_and_department.assign_subject_dashboard import  assign_subject_dashboard_bp
    from .routes.principal.subject_and_department.show_subjects import show_subjects_bp

    app.register_blueprint(home_bp) 
    app.register_blueprint(login_bp) 
    app.register_blueprint(admin_bp) 
    app.register_blueprint(add_principal_bp) 
    app.register_blueprint(principal_dashboard_bp)
    app.register_blueprint(add_teacher_bp) 
    app.register_blueprint(views_teacher_bp) 
    app.register_blueprint(teacher_details_bp) 
    app.register_blueprint(edit_tecaher_bp)
    app.register_blueprint(assign_subject_bp)
    app.register_blueprint(assign_subject_dashboard_bp)
    app.register_blueprint(show_subjects_bp)
    
    return app