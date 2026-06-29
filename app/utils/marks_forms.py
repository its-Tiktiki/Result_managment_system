from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class MarksTopicForm(FlaskForm):
    add_marks_topic_name = StringField(
        "Marks Topic Name",
        validators=[DataRequired()]
    )
    submit = SubmitField("Add Marks System")