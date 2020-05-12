import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase_problems


class Problems(SqlAlchemyBase_problems):
	__tablename__ = 'problems'

	id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key =True, autoincrement=True)
	title = sqlalchemy.Column(sqlalchemy.String)
	content = sqlalchemy.Column(sqlalchemy.Text)
	number_max_test = sqlalchemy.Column(sqlalchemy.INTEGER, default=0)
	who_solved = sqlalchemy.Column(sqlalchemy.String, default="")
