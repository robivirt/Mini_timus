from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class SendForm(FlaskForm):
	number_task = IntegerField('Номер задачи', validators=[DataRequired()])
	code = StringField('Код решения', validators=[DataRequired()], widget=TextArea())
	submit = SubmitField('Отправить решение')
