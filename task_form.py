from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import TextArea
from data.db_session import create_session_problems
from data.problems import Problems


class Add_task_form(FlaskForm):
	title = StringField('Название задачи', validators=[])
	description = StringField('Текст задачи', validators=[], widget=TextArea())
	submit = SubmitField('Отправить задачу')


class Delete_task_form(FlaskForm):
	number = IntegerField('Номер задачи')
	submit = SubmitField('Удалить задачу')

