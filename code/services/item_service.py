import sqlite3
from models.item import Item
from typing import Dict


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
        item = Item.json(*row) if row else None
        # except Exception as error:
        #     raise Exception("Error interno")
        # finally:
        # No hace falta el commit porque no agregamos ningun dato
        connection.close()
        return item if item else None

    @staticmethod
    def get_all():
        # items = []
        connection = sqlite3.connect('data.bd')
        cursor = connection.cursor()

        query = f"select * from {ItemService.TABLE_NAME}"
        # Siempre tiene que ser una tupla
        result = cursor.execute(query)
        rows = result.fetchall()

        connection.close()

        if len(rows) > 0:
            items = [Item.json(*item) for item in rows]
            return {'items': items}
        else:
            return None

    @staticmethod
    def create(item: Dict):  # item es un diccionario
        connection = sqlite3.connect('data.bd')
        cursor = connection.cursor()

        # query = f"insert into {ItemService.TABLE_NAME} values (?,?)"
        # SQLite
        query = f"insert into {ItemService.TABLE_NAME} values (?,?,?)"
        # Siempre tiene que ser una tupla
        # cursor.execute(query, (item['name'], item['price']))
        cursor.execute(query, (None, item['name'], item['price']))  # SQLite

        connection.commit()
        connection.close()

    @staticmethod
    def delete(id):
        connection = sqlite3.connect('data.bd')
        cursor = connection.cursor()

        query = f"delete from {ItemService.TABLE_NAME} where id = (?)"
        # Siempre tiene que ser una tupla
        cursor.execute(query, (id,))

        connection.commit()
        connection.close()
