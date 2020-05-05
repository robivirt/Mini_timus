import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    nickname = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    solve_problems = sqlalchemy.Column(sqlalchemy.String, default="")
