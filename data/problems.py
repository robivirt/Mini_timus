import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase_problems


class Problems(SqlAlchemyBase_problems):
	__tablename__ = 'problems'

	title = sqlalchemy.Column(sqlalchemy.String)

	content = sqlalchemy.Column(sqlalchemy.Text)

	who_solved = sqlalchemy.Column(sqlalchemy.String, default="")
