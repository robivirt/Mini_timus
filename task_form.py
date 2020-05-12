from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from data.db_session import create_session_problems
from data.problems import Problems


class Add_task_form(FlaskForm):
	title = StringField('Название задачи', validators=[])
	description = TextField('Текст задачи', validators=[])
	submit = SubmitField('Отправить задачу')

	def title_validate(self, title):
		session = create_session_problems()
		if session.query(Problems).filter(Problems.title==title).first():
			raise ValidationError('Уже есть задача с таким названием')


class Delete_task_form(FlaskForm):
	number = IntegerField('Номер задачи')
	submit = SubmitField('Удалить задачу')

	def number_validate(self, number):
		session = create_session_problems()
		if not session.query(Problems).filter(Problems.id == number).first():
			raise ValidationError('Нет задачи с таким номером')
