from models.autor import Autor
from typing import Dict, List
# Importar el LibroService
from services.libro_service import LibroService
# Importar la bd
from conexion_bd_mysql import ConexionBdMySql


class AutorService:

    TABLE_NAME = "autores"

    @staticmethod
    def get_by_id(id):
        with ConexionBdMySql.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:

                cursor.execute(
                    f"SELECT * FROM {AutorService.TABLE_NAME} where id = {id}")
                data = cursor.fetchone()

        data = Autor.json(*data) if data else None
        return data if data else None

    @staticmethod
    def get_all():
        with ConexionBdMySql.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:

                cursor.execute(
                    f"SELECT * FROM {AutorService.TABLE_NAME}")
                data = cursor.fetchall()

        if len(data) > 0:
            data = [Autor.json(*item) for item in data]
            return data
        else:
            return None

    @staticmethod
    def create(item: Dict):
        with ConexionBdMySql.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:

                sql = f"""INSERT INTO {AutorService.TABLE_NAME} 
        (nombre, apellido, fecha_nacimiento) VALUES (%s,%s,%s)"""

                cursor.execute(
                    sql, (item['nombre'], item['apellido'], item['fecha_nacimiento']))

                conexion.commit()
        # Obtengo el id del autor que acabo de insertar
                if item.get('libros') != None:
                    sql = "SELECT LAST_INSERT_ID() as lastid"
                    cursor.execute(sql)
                    id_autor = cursor.fetchone()

            # agrego el id del autor a todos los "objetos" libros
                    libros = item['libros']
                    for libro in libros:
                        libro['autor'] = id_autor[0]
                    LibroService.create_many_widh_autor(libros)

    @staticmethod
    def delete(id):
        with ConexionBdMySql.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:

                cursor.execute(
                    f"delete from {AutorService.TABLE_NAME} where id = ({id})")

                conexion.commit()
