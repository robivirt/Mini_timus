from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from data.db_session import create_session_users
from data.users import Users


class RegForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', 
    	validators=[DataRequired(), EqualTo('password', message="Пароли не совпадают")])
    submit = SubmitField('Зарегестрироваться')

    def validate_email(self, email):
    	session = create_session_users()
    	if session.query(Users).filter(Users.email == email.data).first():
    		raise ValidationError("На такую почту уже зарегестрирован аккаунт")
