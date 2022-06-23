import os, sqlite3

#Bianca Rodrigues
#GitHub: https://github.com/bia-rodrig/

#Check if DB exists and create if doesn't
'''
check = os.path.exists('db_test.db')

if (not check):
	file = open('db_test.db', 'w')
	file.close()
	print('created')

	# connection to DB
	connection = sqlite3.connect('db_test.db')

	# SQLite commands cursor
	cursor = connection.cursor()

	#Create query to table
	sql = 'CREATE TABLE IF NOT EXISTS Contacts (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(100), AGE INT, PHONE VARCHAR(20))'

# Table Name: Contacts
# Colunms:
#	ID: Integer
#	Name: varchar(100)
#	PHONE: VARCHAR(20)
'''


def create_db(db_file):
	file = open(db_file, 'w')
	file.close()
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	sql = 'CREATE TABLE IF NOT EXISTS Contacts (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(100), PHONE VARCHAR(20))'
	cursor.execute(sql)
	connection.close()

def check_if_exists(db_file, name):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM Contacts WHERE NAME=?', (name,))
	result = cursor.fetchall()
	if (len(result) > 0):
		return True
	else: return False

def insert_contact(db_file, name, phone):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	cursor.execute('INSERT INTO Contacts (NAME, PHONE) VALUES (?, ?)', (name, phone))
	connection.commit()
	connection.close()


def update_contact(db_file, id_var, name, phone):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()

	cursor.execute('UPDATE Contacts set NAME = ?, PHONE = ? where ID=?', (name, phone, id_var))
	connection.commit()
	connection.close()
	print('Contact updated\n')

def search_contact(db_file, name):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()

	sql = 'SELECT * FROM Contacts Where NAME LIKE \'%' + name +'%\''

	cursor.execute(sql)
	result = cursor.fetchall()
	connection.close()
	return result


def delete(db_file, contact_id):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	cursor.execute('DELETE FROM Contacts where ID=?', (contact_id,))
	connection.commit()
	connection.close()


def list_contacts(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()
	cursor.execute('SELECT * from Contacts')
	contacts = cursor.fetchall()
	connection.close()
	return contacts