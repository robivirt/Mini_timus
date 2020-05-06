import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase_users


class Users(SqlAlchemyBase_users):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    solve_problems = sqlalchemy.Column(sqlalchemy.String, default="")
