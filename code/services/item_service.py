import sqlite3
from models.item import Item


class ItemService:

    TABLE_NAME = "items"

    @staticmethod
    def get_by_id(id):
        # item = ''
        # try:
        # connection = sqlite3.connect('dat.bd')  # Probe la excepcion asi
        connection = sqlite3.connect('data.bd')
        cursor = connection.cursor()

        query = f"select * from {ItemService.TABLE_NAME} where id = ?"
        # Siempre tiene que ser una tupla
        result = cursor.execute(query, (id,))
        row = result.fetchone()

        # item = Item(row[0], row[1], row[2]) if row else None
        item = Item(*row) if row else None
        # except Exception as error:
        #     raise Exception("Error interno")
        # finally:
        # No hace falta el commit porque no agregamos ningun dato
        connection.close()
        return item.json() if item else None

    @staticmethod
    def create(item):
        connection = sqlite3.connect('data.bd')
        cursor = connection.cursor()

        query = f"insert into {ItemService.TABLE_NAME} values (?,?)"
        # Siempre tiene que ser una tupla
        cursor.execute(query, (item.name, item.price))

        connection.commit()
        connection.close()
