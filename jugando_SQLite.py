import sqlite3

connection = sqlite3.connect('data.bd')
cursor = connection.cursor()

create_table = "create table items (id INTEGER primary key, name text, price real)"
# Al usar la palabra INTEGER (con mayuscula) hace los id auto_increments
cursor.execute(create_table)

# Insertar uno
item = ('pelota', 6.12)
insert_query = "insert into items (name, price) values (?,?)"
cursor.execute(insert_query, item)


# Insertar varios items
items = [
    ('bicicleta', 63.56),
    ('laptop', 302.64),
    ('audifonos', 12.99)
]
cursor.executemany(insert_query, items)

#  Obtener items
"""select_query = "select * from users"
cursor.execute(select_query)"""


connection.commit()
connection.close()
