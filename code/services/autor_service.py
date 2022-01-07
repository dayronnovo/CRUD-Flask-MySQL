from models.autor import Autor
from typing import Dict
# Importar la bd
from conexion_bd_mysql import obtener_conexion


class AutorService:

    TABLE_NAME = "autores"

    # @staticmethod
    # def get_by_id(id):
    #     conexion = obtener_conexion()
    #     data = ''
    #     with conexion.cursor() as cursor:
    #         # cursor.execute(
    #         #     f"SELECT * FROM {AutorService.TABLE_NAME} where id = %s", (id,))
    #         cursor.execute(
    #             f"SELECT * FROM {AutorService.TABLE_NAME} where id = {id}")
    #         data = cursor.fetchone()
    #     conexion.close()

    #     data = Autor.json(*data) if data else None
    #     return data if data else None

    @staticmethod
    def get_by_id(id):
        # connection = sqlite3.connect('dat.bd')  # Probe la excepcion asi
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT * FROM {AutorService.TABLE_NAME} where id = {id}")
        data = cursor.fetchone()
        conexion.close()

        data = Autor.json(*data) if data else None
        return data if data else None

    # @staticmethod
    # def get_all():
    #     # items = []
    #     connection = sqlite3.connect('data.bd')
    #     cursor = connection.cursor()

    #     query = f"select * from {ItemService.TABLE_NAME}"
    #     # Siempre tiene que ser una tupla
    #     result = cursor.execute(query)
    #     rows = result.fetchall()

    #     connection.close()

    #     if len(rows) > 0:
    #         items = [Item.json(*item) for item in rows]
    #         return {'items': items}
    #     else:
    #         return None

    # @staticmethod
    # def create(item: Dict):  # item es un diccionario
    #     connection = sqlite3.connect('data.bd')
    #     cursor = connection.cursor()

    #     # query = f"insert into {ItemService.TABLE_NAME} values (?,?)"
    #     # SQLite
    #     query = f"insert into {ItemService.TABLE_NAME} values (?,?,?)"
    #     # Siempre tiene que ser una tupla
    #     # cursor.execute(query, (item['name'], item['price']))
    #     cursor.execute(query, (None, item['name'], item['price']))  # SQLite

    #     connection.commit()
    #     connection.close()

    # @staticmethod
    # def delete(id):
        connection = sqlite3.connect('data.bd')
        cursor = connection.cursor()

        query = f"delete from {ItemService.TABLE_NAME} where id = (?)"
        # Siempre tiene que ser una tupla
        cursor.execute(query, (id,))

        connection.commit()
        connection.close()
