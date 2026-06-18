from app.extensions import db

class Department(db.Model):
    __tablename__ = "departments"

    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(150), nullable=False, unique=True)

    principal_id = db.Column(
        db.Integer,
        db.ForeignKey("principal_info.principal_id"),
        nullable=False
    )

class Subjects(db.Model):
    __tablename__ = "subjects"

    subject_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    subject_code = db.Column(db.String(10),nullable=False)
    subject_name = db.Column(db.String(150), nullable=False)
    principal_id = db.Column(
        db.Integer,
        db.ForeignKey("principal_info.principal_id"),
        nullable=False
    )


class Curriculum(db.Model):
    __tablename__ = "curriculum"

    curriculum_id = db.Column(db.Integer, primary_key=True,autoincrement=True)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "departments.department_id"
        ),
        nullable = False
    )

    semester = db.Column(db.Integer, nullable=False)
    subject_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "subjects.subject_id"
        ),
        nullable = False 
    )

class AssignTeacher(db.Model):
    __tablename__ = "assign_teacher"
    assign_teaher_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    
    