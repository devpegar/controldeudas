import sqlite3
from sqlite3.dbapi2 import Cursor

def run_query(query, parameters = ()):
	with sqlite3.connect('dbase', timeout = 10) as conn:
		cursor = conn.cursor()
		result = cursor.execute(query, parameters)
		conn.commit()
	return result