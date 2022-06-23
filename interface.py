#github.com/bia-rodrig

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import back_functions as bf

window = Tk()
window.resizable(False, False)
window.geometry('500x600')
window.title('CRUD Pyton-SQLite')
window.iconbitmap('images/br.ico')

control_new_edit = 0
# 0 New
# 1 Edit

lbl_title = Label(window, text='CRUD - Python/SQLite', font=('Arial', 16)).pack(fill='x')

fr_add_contact = Frame(window, highlightbackground="grey80", highlightthickness=1)
fr_add_contact.pack(fill='both', ipady=20, padx=5, pady=(5,10))

lbl_name = Label(fr_add_contact, text='Name:', font=('Arial', 10)).pack(side='left', padx=10)
txt_name = Entry(fr_add_contact, width=10)
txt_name.pack(side='left')

lbl_phone = Label(fr_add_contact, text='Phone:', font=('Arial', 10)).pack(side='left', padx=(40,10))
txt_phone = Entry(fr_add_contact, width=20)
txt_phone.pack(side='left')

fr_contacts = Frame(window)
fr_contacts.pack(side='top', fill='both', expand='yes')

fr_list = Frame(fr_contacts)
fr_list.pack(side='top', fill='both', expand=1)

txt_search = Entry(fr_list, width=50, fg='grey40', font=('Arial',10, 'italic'))
txt_search.insert(0, 'Type to search')
txt_search.pack(side='top',pady=10)

verticalScrollBar = ttk.Scrollbar(fr_list, orient='vertical')
verticalScrollBar.pack(side='right', fill='y', padx=(0,10))
lst_contacts = ttk.Treeview(fr_list, height=5, selectmode='extended', yscrollcommand=verticalScrollBar.set)
lst_contacts['columns'] = ('ID', 'Name', 'Phone')
lst_contacts.column('#0', width=0, stretch='no')
lst_contacts.column('ID', anchor='w', width=40, minwidth=40)
lst_contacts.column('Name', anchor='w', width=200, minwidth=200)
lst_contacts.column('Phone', anchor='w', width=220, minwidth=150)
lst_contacts.heading('ID', text='ID', anchor='center')
lst_contacts.heading('Name', text='Name', anchor='center')
lst_contacts.heading('Phone', text='Phone', anchor='center')
lst_contacts.pack(side='right', fill='y', padx=(10,0))
verticalScrollBar.config(command=lst_contacts.yview)

fr_details = Frame(fr_contacts, highlightbackground="grey60", highlightthickness=1)
fr_details.pack(side='top', fill='both', expand=1, padx=10, pady=10)

name_var = StringVar()
phone_var = StringVar()
id_var = StringVar()

lbl_details_id = Label(fr_details, textvariable=id_var, font=('Arial'))
lbl_details_id.place(relx=0.5, rely=0.25, anchor=CENTER)

lbl_details_name = Label(fr_details, textvariable=name_var, font=('Arial'))
lbl_details_name.place(relx=0.5, rely=0.5, anchor=CENTER)

lbl_details_phone = Label(fr_details, textvariable=phone_var, font=('Arial'))
lbl_details_phone.place(relx=0.5, rely=0.75, anchor=CENTER)

fr_bottom_buttons = Frame(window)
fr_bottom_buttons.pack(pady=10)

def clear_search(e):
	txt_search.delete(0, 'end')

def get_search(e):
	bf.search(lst_contacts, txt_search.get().upper())

def get_selected_details(e):
	selected = lst_contacts.focus()
	sel_values = lst_contacts.item(selected, 'values')
	bf.show_details(sel_values, id_var, name_var, phone_var)

def edit_contact():
	global control_new_edit
	txt_name.delete(0, 'end')
	txt_name.insert(0, name_var.get())
	txt_phone.delete(0, 'end')
	txt_phone.insert(0, phone_var.get())
	control_new_edit = 1

def new_or_edit():
	global control_new_edit
	bf.save_contact(lst_contacts, id_var.get(), txt_name.get().upper(), txt_phone.get(), control_new_edit)
	control_new_edit = 0

def delete():
	selected = lst_contacts.focus()
	sel_values = lst_contacts.item(selected, 'values')
	msg = messagebox.askquestion('bia-rodrig', 'Are you sure you want to delete {}'.format(sel_values[1]))
	if msg == 'yes':
		bf.delete_contact(lst_contacts, sel_values)

txt_search.bind('<1>', clear_search)
txt_search.bind('<KeyRelease>', get_search)
lst_contacts.bind('<ButtonRelease>', get_selected_details)

btn_save = Button(fr_add_contact, text='Save', width=10, command=new_or_edit).pack(side='right', padx=15)
btn_edit = Button(fr_bottom_buttons, text='Edit', width=10, command=edit_contact).pack(side='left', padx=50)
btn_delete = Button(fr_bottom_buttons, text='Delete', width=10, command=delete).pack(side='right', padx=50)

lbl_footage = Label(window, text='https://bia-rodrig.github.io', font=('Arial', 8)).pack(side='bottom', fill='x')

bf.load_DB(lst_contacts)

window.mainloop()