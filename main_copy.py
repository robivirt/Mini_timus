from flask import render_template, Flask, url_for, redirect
import flask
from .login_form import LoginForm
from .register_form import RegForm
from data.users import Users
from data.problems import Problems
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init_users()
db_session.global_init_problems()


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
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            solve_problems = "",
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('reg.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session_problems()
    Tasks = []
    temp_id = -1
    if 'user' in flask.session:
        temp_id = flask.session['user']
    for problem in session.query(Problems).all():
        AC = "Не решена"
        if str(temp_id) in problem.who_solved.split(','):
            AC = "Решена"
        Tasks.append({"title": problem.title, "content": problem.content, "AC": AC})
    return render_template('index.html', title='Главная страница', Task=Tasks)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
