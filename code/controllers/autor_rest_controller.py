from flask import Blueprint, request
from models.autor import Autor
from services.autor_service import AutorService

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


# @item_api.route("/")
# def get_all():
#     try:
#         items = ItemService.get_all()
#         if items:
#             return items
#         else:
#             return {'Error': "Base de datos empty"}, 400  # Bad Request
#     except Exception as error:
#         return {'Error': f"{error}"}, 500  # Internal Error


# @item_api.route("/", methods=['POST'])
# def create():
#     data = request.get_json()
#     # print(f"Data Create: \n{data}")
#     try:
#         ItemService.create(data)
#         return {"Message": "Item creado con exito"}, 201  # Created
#     except Exception as error:
#         return {'Error': f"{error}"}, 500  # Internal Error


# @item_api.route("/<int:id>", methods=['DELETE'])
# def delete(id):
#     try:

#         item = ItemService.get_by_id(id)
#         if item:
#             ItemService.delete(id)
#             return {"Message": "Item eliminado con exito"}
#         else:
#             return {'Error': f"No existe el id {id}"}, 400  # Bad Request

#     except Exception as error:
#         return {'Error': f"{error}"}, 500  # Internal Error
