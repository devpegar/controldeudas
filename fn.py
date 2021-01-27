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

def selectDB(table, order):
	query = 'SELECT * FROM ' + table + ' ORDER BY id ' + order
	return query

def insertDB(table, data):
	q = ', ?'
	qq = ''
	for i in range(data):
		qq += q
	query = 'INSERT INTO ' + table + ' VALUES (NULL' + qq + ')'
	return query

def updateBD(table, id, col = []):
	cc = ''
	ii = 0
	for c in col:
		cc += c + ' = ?, '

	query = 'UPDATE ' + table + ' SET ' + cc[:-2] + ' WHERE id = ?'
	
	return query

def get_name(table, id):
	query = 'SELECT name FROM ' + table + ' WHERE id = ?'
	db_rows = run_query(query, (id, ))
	
	for row in db_rows:
		return row[0]

def get_id(table, name):
	query = 'SELECT id FROM ' + table + ' WHERE name = ?'
	db_rows = run_query(query, (name, ))

	for row in db_rows:
		return row[0]

def get_names(table):
	query = 'SELECT name FROM ' + table
	db_rows = run_query(query)
	db_list = []
	for row in db_rows:
		db_list.append(row[0])

	return db_list

def format_currency(num):
	curr = '$ ' + str(num)
	return curr

def format_date(date):
	if date != '':
		a = date.split('-')
		nDate = a[2] + '/' + a[1] + '/' + a[0]
	return nDate

def validateDateFormat(date):
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

def format_date_db(date):
	if date != '':
		a = date.split('/')
		newdate = a[2] + '-' + a[1] + '-' + a[0]
	return newdate


format_date_db('02/02/2021')