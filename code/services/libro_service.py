from models.libro import Libro
from models.autor import Autor
# from typing import Dict, List
# Importar la bd
from conexion_bd_mysql import obtener_conexion


class LibroService:
    TABLE_NAME = "libros"

    @staticmethod
    def get_by_autor_id(id):

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT l.id, l.titulo, l.anio_edicion, l.precio FROM {LibroService.TABLE_NAME} l WHERE l.autor_id = {id}")
        data = cursor.fetchall()
        # print(data)
        conexion.close()

        if len(data) > 0:
            data = [Libro.json(*item) for item in data]
            return {'items': data}
        else:
            return None

    # @staticmethod
    # def get_by_id(id):

    #     conexion = obtener_conexion()
    #     cursor = conexion.cursor()
    #     cursor.execute(
    #         f"SELECT * FROM {LibroService.TABLE_NAME} where id = {id}")
    #     data = cursor.fetchone()
    #     # print(data)  # (1, 'El amor en los tiempos de cólera', 1985, 63.99, 1)
    #     conexion.close()

    #     data = Libro.json(*data) if data else None
    #     # print(data) # {'id': 1, 'titulo': 'El amor en los tiempos de cólera', 'anio_edicion': 1985, 'precio': 63.99, 'autor': 1}
    #     return data if data else None

    # @staticmethod
    # def get_by_id(id):

    #     conexion = obtener_conexion()
    #     cursor = conexion.cursor()
    #     cursor.execute(
    #         f"SELECT l.id, l.titulo, l.anio_edicion, l.precio, a.id, a.nombre, a.apellido, a.fecha_nacimiento FROM {LibroService.TABLE_NAME} l JOIN autores a ON a.id = l.id HAVING l.id = {id} ")
    #     data = cursor.fetchone()
    #     # (1, 'El amor en los tiempos de cólera', 1985, 63.99, 1, 'Gabriel', 'García Márquez', datetime.date(1927, 3, 6))
    #     print(data)
    #     conexion.close()

    #     data = Libro.json(data[0], data[1], data[2], data[3], Autor.json(
    #         data[4], data[5], data[6], data[7])) if data else None
    #     # {'id': 1, 'titulo': 'El amor en los tiempos de cólera', 'anio_edicion': 1985, 'precio': 63.99, 'autor': {'id': 1, 'nombre': 'Gabriel', 'apellido': 'García Márquez', 'fecha_nacimiento': datetime.date(1927, 3, 6)}}
    #     print(data)
    #     return data if data else None
