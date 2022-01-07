from models.autor import Autor
from typing import Dict, List
# Importar la bd
from conexion_bd_mysql import obtener_conexion


class AutorService:

    TABLE_NAME = "autores"

    # @staticmethod
    # def get_by_id(id):
    #     conexion = obtener_conexion()
    #     data = None
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

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT * FROM {AutorService.TABLE_NAME} where id = {id}")
        data = cursor.fetchone()
        conexion.close()

        data = Autor.json(*data) if data else None
        return data if data else None

    @staticmethod
    def get_all():

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            f"SELECT * FROM {AutorService.TABLE_NAME}")
        data = cursor.fetchall()
        conexion.close()

        if len(data) > 0:
            data = [Autor.json(*item) for item in data]
            return {'items': data}
        else:
            return None

    @staticmethod
    def create(item: Dict):  # item es un diccionario
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # cursor.execute(f"INSERT INTO {AutorService.TABLE_NAME} (nombre, apellido, fecha_nacimiento) VALUES (%s,%s,%s)",
        #                (item['nombre'], item['apellido'], item['fecha_nacimiento']))

        sql = f"""INSERT INTO {AutorService.TABLE_NAME} 
        (nombre, apellido, fecha_nacimiento) VALUES (%s,%s,%s)"""

        cursor.execute(
            sql, (item['nombre'], item['apellido'], item['fecha_nacimiento']))

        conexion.commit()
        conexion.close()

    @staticmethod
    def delete(id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            f"delete from {AutorService.TABLE_NAME} where id = ({id})")

        conexion.commit()
        conexion.close()
