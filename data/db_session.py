import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase_problems = dec.declarative_base()
SqlAlchemyBase_users = dec.declarative_base()

__factory_users = None
__factory_problems = None


def global_init_problems():
    global __factory_problems

    if __factory_problems:
        return

    conn_str = f'sqlite:///db/problems.db?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine_problems = sa.create_engine(conn_str, echo=False)
    __factory_problems = orm.sessionmaker(bind=engine_problems)

    from . import problems

    SqlAlchemyBase_problems.metadata.create_all(engine_problems)


def create_session_problems() -> Session:
    global __factory_problems
    return __factory_problems()


def global_init_users():
    global __factory_users

    if __factory_users:
        return

    conn_str = f'sqlite:///db/users.db?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine_users = sa.create_engine(conn_str, echo=False)
    __factory_users = orm.sessionmaker(bind=engine_users)

    from . import users

    SqlAlchemyBase_users.metadata.create_all(engine_users)




def create_session_users() -> Session:
    global __factory_users
    return __factory_users()
