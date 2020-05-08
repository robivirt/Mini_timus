from flask import render_template, Flask, url_for, redirect, request
import flask
from login_form import LoginForm
from register_form import RegForm
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
        flag = True
        session = db_session.create_session_users()
        for user in session.query(User).all():
            if user.username == form.username.data:
                flag = False
        if flag:
            return render_template('log.html', title='Авторизация', form=form,
                                   message='Такого пользователя нет')
        for user in session.query(User).all():
            if user.password == form.password.data:
                flag = False
        if flag:
            return render_template('log.html', title='Авторизация', form=form,
                                   message='Неправильный пароль')
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
        session = db_session.create_session_users()
        if session.query(Users).filter(Users.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Users(
            username=form.username.data,
            email=form.email.data,
            solve_problems="",
            password=form.password.data
        )
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
    return render_template('index.html', Task=Tasks)


@app.route('/problem/<numb>')
def prob(numb):
    session = db_session.create_session_problems()
    content = ""
    name = ""
    for problems in session.query(Problems).all():
        if int(numb) == problems.id:
            content = problems.content
            name = problems.title
    return render_template('page.html', name=name, content=content)


@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
        return "lsfgs;l"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
