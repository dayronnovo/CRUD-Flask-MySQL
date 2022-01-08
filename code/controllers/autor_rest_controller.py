# from datetime import date
from flask import Blueprint, request
from models.autor import Autor
from services.autor_service import AutorService
from compro_prueba import Validacion

# Creando controlador
autor_controller = Blueprint('autor_controller', __name__)
# Metodos


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


@autor_controller.route("/")
def get_all():
    try:
        items = AutorService.get_all()
        if items:
            return items
        else:
            return {'Error': "Base de datos empty"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error


@autor_controller.route("/", methods=['POST'], strict_slashes=False)
def create():
    data = request.get_json()

    try:
        Validacion.add_argument(data, 'nombre', str, True)
        Validacion.add_argument(data, 'apellido', str, True)
        Validacion.add_argument(data, 'fecha_nacimiento', str, True)

        AutorService.create(data)
        return {"Message": "Item creado con exito"}, 201  # Created
    except (TypeError, ValueError) as error:
        return {'Error': f"{error}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error


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
