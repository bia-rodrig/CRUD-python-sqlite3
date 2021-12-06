import os, sqlite3

#Bianca Rodrigues
#GitHub: https://github.com/bia-rodrig/

#Check if DB exists and create if doesn't
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
#	AGE: Integer
#	PHONE: VARCHAR(20)

	# Execute create table command
	cursor.execute(sql)
	print('Table created')
	connection.close() # always close connection after an execute

op = 5 # initializing option variable

print('1 - Insert contact')
print('2 - Update contact')
print('3 - Delete contact')
print('4 - List')
print('0 - Exit')


def insert_contact():
	print('\nInsert contact info:')
	name = input('Name: ')
	age = input('Age: ')
	phone = input('Phone: ')

	connection = sqlite3.connect('db_test.db')
	cursor = connection.cursor()

	# Insert contact
	cursor.execute('INSERT INTO Contacts (NAME, AGE, PHONE) VALUES (?, ?, ?)', (name, age, phone))
	connection.commit()
	connection.close()
	print('Contact inserted\n')


def update_contact():
	print('\nInform contact ID to update:')
	select_id = input('ID: ')

	new_name = input('Name: ')
	new_age = input('Age: ')
	new_phone = input('Phone: ')

	connection = sqlite3.connect('db_test.db')
	cursor = connection.cursor()

	cursor.execute('UPDATE Contacts set NAME = ?, AGE = ?, PHONE = ? where ID=?', (new_name, new_age, new_phone, select_id))
	connection.commit()
	connection.close()
	print('Contact updated\n')


def delete_contact():
	print('\nInform contact ID to delete:')
	select_id = input('ID: ')

	connection = sqlite3.connect('db_test.db')
	cursor = connection.cursor()

	cursor.execute('DELETE FROM Contacts where ID=?', (select_id))
	connection.commit()
	connection.close()
	print('Contact deleted\n')




def list_contacts():
	print('\nContacts list:')
	connection = sqlite3.connect('db_test.db')
	cursor = connection.cursor()
	cursor.execute('SELECT * from Contacts')
	contacts = cursor.fetchall()
	for item in contacts:
		print(item)
	connection.close()
	print('\n')


def exit():
	print('Finished')

switch = {'1': insert_contact, '2': update_contact, '3': delete_contact, '4': list_contacts, '0': exit}


while int(op) != 0:
	op = input('Choose an option:')
	if (int(op) <= 4):
		call = switch.get(op)
		call()
	else:
		print('Invalid option')