from flask import render_template, Flask, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired()])
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('log.html', title='Авторизация', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('reg.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/index')
def index():
    Tasks = [{"title": "A + B", "AC": "Не решена", "content": "Выведите сумму чисел введеных в 1 строке"}]  # получение списка задач и решенных задач
    return render_template('index.html', title='Главная страница', Task=Tasks)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
