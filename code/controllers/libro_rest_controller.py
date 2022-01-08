from flask import Blueprint, request
from models.libro import Libro
from services.libro_service import LibroService
from compro_prueba import Validacion

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


@libro_controller.route("/libro_autor/<int:id>")
def get_by_autor_id(id):
    try:
        item = LibroService.get_by_autor_id(id)
        if item:
            return item
        else:
            return {'Error': f"No existe el id {id}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error
