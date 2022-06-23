import os
import crud_python_sqlite as cps
from tkinter import messagebox

db_file = 'db/contacts.db'

def load_DB(lst_contacts):
	check = os.path.exists(db_file)
	contacts = ''

	if (not check):
		contacts = cps.create_db(db_file)

	contacts = cps.list_contacts(db_file)

	if len(contacts) == 0:
		print('Banco de dados vazio')
	else:
		populate_list(lst_contacts, contacts)		

def populate_list(lst, array):
	for item in array:
		lst.insert(parent='', index=item[0], values=[item[0], item[1], item[2]])

def clear_list(lst):
	for item in lst.get_children():
		lst.delete(item)

def save_contact(lst, id_var, name, phone, new_or_edit):
	if new_or_edit == 1:
		#print(id_var.get())
		#print(name)
		#print(phone)
		cps.update_contact(db_file, id_var, name, phone)

	else:
		#Salva novo contato
		if (not cps.check_if_exists(db_file, name)):
			cps.insert_contact(db_file, name, phone)
		else:
			msg = messagebox.askquestion('bia-rodrig', 'Contact name already exists. Do you wnat proceed?')
			if msg == 'yes':
				cps.insert_contact(db_file, name, phone)

	contacts = cps.list_contacts(db_file)
	clear_list(lst)
	populate_list(lst, contacts)

def search(lst, search_name):
	contacts = ''
	if len(search_name) == 0:
		contacts = cps.list_contacts(db_file)
	else: 
		contacts = cps.search_contact(db_file, search_name)
	clear_list(lst)
	populate_list(lst, contacts)

def show_details(sel, id_var, name, phone):
	id_var.set(sel[0])
	name.set(sel[1])
	phone.set(sel[2])

def delete_contact(lst, sel):
	id_to_delete = sel[0]
	cps.delete(db_file, id_to_delete)
	messagebox.showinfo('bia-rodrig', 'Contact deleted!')

	contacts = cps.list_contacts(db_file)
	clear_list(lst)
	populate_list(lst, contacts)