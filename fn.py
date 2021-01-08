import sqlite3
from sqlite3.dbapi2 import Cursor

def run_query(query, parameters = ()):
	with sqlite3.connect('dbase', timeout = 10) as conn:
		cursor = conn.cursor()
		result = cursor.execute(query, parameters)
		conn.commit()
	return result

def validateDate(date):
	i = 0
	for c in date:
		if c == '-':
			i +=1
	if i == 2:
		try:
			year = int(date[0:4])
			month = int(date[5:7])
			day = int(date[8:10])
		except:
			return False


		if year > 1900 and year < 2100:
			if month > 0 and month < 13:
				if day > 0 and day < 32:
					return True
	
	return False