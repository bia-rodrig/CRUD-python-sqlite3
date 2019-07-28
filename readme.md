# Python - SQLITE3 - CRUD

Aplicação simples que mostra os processos de criar, ler, atualizar e apagar, dados de um banco de dados sqlite3.

### Conexão com o Banco de Dados
```python
connection = sqlite3.connect('db/db_teste.db')
cursor = connection.cursor()
sql = 'CREATE TABLE IF NOT EXISTS Users
			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NAME VARCHAR(100),
			AGE INT)'

cursor.execute(sql)
```
Nome do bando de dados: db_teste.db

Nome da tabela: Users
Colunas da tabela:
* ID: Integer
* Name: Varchar(100)
* Age: Integer

## Comandos CRUD

### Create
```python
sql = "INSERT INTO Users (NAME, AGE) VALUES ('Bianca', 32)"
cursor.execute(sql)
```

### Read
```python
sql = 'SELECT * FROM USERS'
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
	print (row)
```

### Update
```python
sql = "UPDATE Users set name = 'Bianca Rodrigues' WHERE ID=1"
cursor.execute(sql)
```

### Delete
```python
sql = "DELETE FROM Users where ID=1"
cursor.execute(sql)
```

### Grava informações no BD
```python
connection.commit()
```

### Encerra conexão
```python
connection.close()
```


Bianca Rodrigues