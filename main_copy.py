from flask import render_template, Flask, url_for, redirect
from .login_form import LoginForm
from .register_form import RegForm
from data import db_session

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
            about=form.about.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('reg.html', title='Регистрация', form=form)


@app.route('/')
@app.route('/index')
def index():
    Tasks = [{"title": "A + B", "AC": "Не решена",
              "content": "Выведите сумму чисел введеных в 1 строке"}]  # получение списка задач и решенных задач
    return render_template('index.html', title='Главная страница', Task=Tasks)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
