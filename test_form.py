from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.widgets import TextArea
from data.db_session import create_session_problems
from data.problems import Problems


class Add_test_form(FlaskForm):
	number_task = IntegerField('Номер задачи')
	test = StringField('Тест', widget=TextArea())
	answer_test = StringField('Ответ на тест', widget=TextArea())
	submit = SubmitField('Отправить тест')


class Delete_test_form(FlaskForm):
	number_task = IntegerField('Номер задачи')
	number_test = StringField('Номер теста')
	submit = SubmitField('Удалить тест')
