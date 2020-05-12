from flask import render_template, Flask, url_for, redirect, request, flash
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from task_form import Add_task_form, Delete_task_form
from login_form import LoginForm
from register_form import RegForm
from data.users import Users
from data.problems import Problems
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init_users()
db_session.global_init_problems()


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session_users()
    return session.query(Users).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session_users()
        user = session.query(Users).filter(form.username.data==Users.username).first()
        if user and user.password != form.password.data:
            return render_template('log.html', title='Авторизация', form=form, error="Неправильный пароль")
        user = session.query(Users).filter(Users.username == form.username.data).first()
        login_user(user)
        return redirect('/')
    return render_template('log.html', title='Авторизация', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        session = db_session.create_session_users()
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
    if current_user.is_authenticated:
        temp_id = current_user.id
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/add_delete_task', methods=['POST', 'GET'])
def add_delete_task():
    form = Add_task_form()
    form1 = Delete_task_form()
    if form.validate_on_submit() and form.description.data and form.title.data:
        session = db_session.create_session_problems()
        session.add(Problems(title=form.title.data, content=form.description.data))
        session.commit()
    if form1.validate_on_submit():
        session = db_session.create_session_problems()
        session.query(Problems).filter(Problems.id == form1.number.data).delete()
        session.commit()
    return render_template("add_task.html", form=form, form1=form1)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
