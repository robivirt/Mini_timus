import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase_users


class Users(SqlAlchemyBase_users):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    solve_problems = sqlalchemy.Column(sqlalchemy.String, default="")
