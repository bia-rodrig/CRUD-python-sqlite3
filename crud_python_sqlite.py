import sqlite3

#Bianca Rodrigues
#GitHub: https://github.com/bia-rodrig/

#Cria Bando de dados
connection = sqlite3.connect('db/db_teste.db') 
#Conecta ao bando de dados. 
#"db": pasta dentro da pasta do projeto. 
#"test.db": nome do BD. se não existir, vai criar

# Cursor dos comandos SQL
cursor = connection.cursor()


#Cria tabeLa
sql = 'CREATE TABLE IF NOT EXISTS Users
			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NAME VARCHAR(100),
			AGE INT)'

# Nome da tabela: Users
# Colunas: 
#	ID: Integer
#	Name: varchar(100)
#	AGE: Integer
			
cursor.execute(sql)

'''Create '''
sql = "INSERT INTO Users (NAME, AGE) VALUES ('Bianca', 32)"
cursor.execute(sql)

'''Update'''
sql = "UPDATE Users set name = 'Bianca Rodrigues' WHERE ID=1"
cursor.execute(sql)

'''Delete'''
sql = "DELETE FROM Users where ID=1"
cursor.execute(sql)

connection.commit() #para gravar no arquivo

'''READ'''
#seleciona dado da tabela
sql = 'SELECT * FROM USERS'
#sql = 'SELECT ID, NAME, AGE FROM Users where id="1"'

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
	print (row)

connection.close()