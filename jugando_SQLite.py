import sqlite3

connection = sqlite3.connect('data.bd')
cursor = connection.cursor()

create_table = "create table items (id integer primary key, name text, password real)"
cursor.execute(create_table)

# Insertar uno
item = (1, 'pelota', 6.12)
insert_query = "insert into items values (?,?,?)"
cursor.execute(insert_query, item)


# Insertar varios items
items = [
    (2, 'bicicleta', 63.56),
    (3, 'laptop', 302.64),
    (4, 'audifonos', 12.99)
]
cursor.executemany(insert_query, items)

#  Obtener items
"""select_query = "select * from users"
cursor.execute(select_query)"""


connection.commit()
connection.close()
