from flask import Blueprint, request, jsonify
from pymysql.err import MySQLError
from models.libro import Libro
from services.libro_service import LibroService
from validaciones import Validacion

# Creando controlador
libro_controller = Blueprint('libro_controller', __name__)
# Metodos


@libro_controller.route("/<int:id>")
def get_by_id(id):
    try:
        item = LibroService.get_by_id(id)
        if item:
            return item
        else:
            return {'Error': f"No existe el id {id}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error


@libro_controller.route("/autor/<int:id>")
def get_book_by_id_with_autor(id):
    try:
        item = LibroService.get_book_by_id_with_autor(id)
        if item:
            return item
        else:
            return {'Error': f"No existe el id {id}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error


@libro_controller.route("/", methods=['POST'], strict_slashes=False)
def create():
    data = request.get_json()
    try:
        
        Validacion.validar(Libro.campos, data)
        LibroService.create(data)
        
        return {"Message": "Libro creado con exito"}, 201  # Created
    except (ValueError) as error:
        return {'Error': f"{error}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error


@libro_controller.route("/")
def get_all():
    try:
        items = LibroService.get_all()
        if items:
            return jsonify(items)
        else:
            return {'Error': "Base de datos empty"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error
