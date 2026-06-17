from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired

class CurriculamForm(FlaskForm):
    department_id = SelectField(
        "Departments",
        choices=[],
        validators=[DataRequired()]
    )

    semester = SelectField(
        "semester",
        choices=[
            ("0","Select"),
            ("1","Semester 1"),
            ("2","Semester 2"),
            ("3","Semester 3"),
            ("4","Semester 4"),
            ("5","Semester 5"),
            ("6","Semester 6"),
            ("7","Semester 7"),
        ]
    )

    subject_id = SelectField(
        "Subject",
        choices=[],
        coerce=int
    )

    submit = SubmitField(
        "Assign Subject"
    )

class DepartmentForm(FlaskForm):
    department_id = IntegerField(
        "Department ID",
        validators=[DataRequired()]
    )
    department_name = StringField(
        "Department Name",
        validators=[DataRequired()]
    )

    submit = SubmitField("Save Department")
class SubjectForm(FlaskForm):
    subject_code = StringField(
        "Subject Code",
        validators=[DataRequired()]
    )
    subject_name = StringField(
        "Subject Name",
        validators=[DataRequired()]
    )
    submit = SubmitField("Save Subject")