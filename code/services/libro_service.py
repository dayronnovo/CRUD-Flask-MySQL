from models.libro import Libro
from models.autor import Autor
from typing import Dict, List
# Importar la bd
from conexion_bd_mysql import obtener_conexion


class LibroService:
    TABLE_NAME = "libros"

# ======================= Con este solo obtengo el libro =======================
    @staticmethod
    def get_by_id(id):

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT l.id, l.titulo, l.anio_edicion, l.precio FROM {LibroService.TABLE_NAME} l where l.id = {id}")
        data = cursor.fetchone()
        conexion.close()

        data = Libro.json(*data) if data else None

        return data if data else None

# ======================= Con este obtengo el libro con su autor =======================
    @staticmethod
    def get_book_by_id_with_autor(id):

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT l.id, l.titulo, l.anio_edicion, l.precio, a.id, a.nombre, a.apellido, a.fecha_nacimiento FROM {LibroService.TABLE_NAME} l JOIN autores a ON a.id = l.id HAVING l.id = {id} ")
        data = cursor.fetchone()

        conexion.close()

        libro = Libro.json(data[0], data[1], data[2], data[3])
        autor = Autor.json(data[4], data[5], data[6], data[7])
        libro['autor'] = autor

        return libro if libro else None

    # =============================================================================
    # Con este metodo obtengo los libros de un autor. Lo uso en el AutorService
    # =============================================================================
    @staticmethod
    def get_books_by_autor_id(id):

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT l.id, l.titulo, l.anio_edicion, l.precio FROM {LibroService.TABLE_NAME} l WHERE l.autor_id = {id}")
        data = cursor.fetchall()
        conexion.close()

        if len(data) > 0:
            data = [Libro.json(*item) for item in data]
            return data
        else:
            return None

    @staticmethod
    def create(item: Dict):  # item es un diccionario
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # id, titulo, anio_edicion, precio, autor

        sql = f"""INSERT INTO {LibroService.TABLE_NAME} 
        (titulo, anio_edicion, precio, autor_id) VALUES (%s,%s,%s,%s)"""

        cursor.execute(
            sql, (item['titulo'], item['anio_edicion'], item['precio'], item.get('autor')))

        conexion.commit()
        conexion.close()

    @staticmethod
    def get_all():

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            f"SELECT * FROM {LibroService.TABLE_NAME}")
        data = cursor.fetchall()
        conexion.close()

        if len(data) > 0:
            data = [Libro.json(*item) for item in data]

            return data
        else:
            return None
