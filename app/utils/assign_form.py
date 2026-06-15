from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired

class DepartmentForm(FlaskForm):
    department_id = IntegerField(
        "Department Id",
        validators=[DataRequired()]
    )
    department_name = StringField(
        "Department Name",
        validators=[DataRequired()]
    )

    submit = SubmitField("Save Departmant")


class SubjectForm(FlaskForm):

    department_id = SelectField(
        "Department",
        validators=[DataRequired()],
        choices=[]
    )
    semester = SelectField(
        "Semister",
        choices=[
            ("1","Semester 1"),
            ("2","Semester 2"),
            ("3","Semester 3"),
            ("4","Semester 4"),
            ("5","Semester 5"),
            ("6","Semester 6"),
            ("7","Semester 7"),
        ]
    )
    subject_code = IntegerField(
        "Subject code",
        validators=[DataRequired()]
    )
    subject_name = StringField(
        "Subject Name",
        validators=[DataRequired()]
    )

    submit = SubmitField("Save subject")

