from flask import Blueprint
from models.item import Item
from services.item_service import ItemService

item_api = Blueprint('item_api', __name__)

# Metodos


@item_api.route("/<string:id>")
def get_by_id(id):
    try:
        item = ItemService.get_by_id(id)
        if item:
            return item
        else:
            return {'Error': f"No existe el id {id}"}, 400  # Bad Request
    except Exception as error:
        return {'Error': f"{error}"}, 500  # Internal Error
