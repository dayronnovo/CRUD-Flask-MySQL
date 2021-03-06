# from datetime import date
from flask import Blueprint, request, jsonify
from models.autor import Autor
from models.libro import Libro
from services.autor_service import AutorService
from services.libro_service import LibroService
from validaciones import Validacion

# Creando controlador
autor_controller = Blueprint('autor_controller', __name__)
# Metodos

# ======================= Con este solo obtengo el autor =======================


@autor_controller.route("/<int:id>")
def get_by_id(id):
    try:
        item = AutorService.get_by_id(id)
        if item:
            return item
        else:
            return {'Error': f"No existe el id {id}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error

# ======================= Con este obtengo el autor con sus libros =======================


@autor_controller.route("/books/<int:id>")
def get_autor_by_id_with_books(id):
    try:
        autor = AutorService.get_by_id(id)
        libros = LibroService.get_books_by_autor_id(id)
        autor['libros'] = libros
        if autor and libros:
            return autor
        else:
            return {'Error': f"No existe el id {id}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error


@autor_controller.route("/")
def get_all():
    try:
        items = AutorService.get_all()
        if items:
            return jsonify(items)
        else:
            return {'Error': "Base de datos empty"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error


@autor_controller.route("/", methods=['POST'], strict_slashes=False)
def create():
    data = request.get_json()
    try:
        
        Validacion.validar(Autor.campos, data)
        if data.get('libros'):
            for json in data['libros']:
                Validacion.validar(Libro.campos, json)

        AutorService.create(data)
        return {"Message": "Item creado con exito"}, 201  # Created
    except (ValueError) as error:
        return {'Error': f"{error}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error

# ======================= Crear autor con varios libros =======================


@autor_controller.route("/<int:id>", methods=['DELETE'])
def delete(id):
    try:

        item = AutorService.get_by_id(id)
        if item:
            AutorService.delete(id)
            return {"Message": "Item eliminado con exito"}
        else:
            return {'Error': f"No existe el id {id}"}, 400  # Bad Request

    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error
