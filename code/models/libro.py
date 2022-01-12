from types import LambdaType
from typing import Tuple, List, Dict
class Libro:

    __val_id = [
        (lambda x : type(x) == int, "No es del tipo correcto")
    ]
    __val_str = [
        (lambda x : type(x) == str, "No es del tipo correcto"),
        (lambda x: len(x.strip()) > 0, "No puede ser vacio")
    ]
    __val_precio = [
         (lambda x : type(x) == float, "No es del tipo correcto"),
         (lambda x : x > 0, "Tiene que ser mayor que cero")

    ]

# Explicacion de como trabaja la validacion:
# 1 - (__val_id, True) (lista de validaciones, True/False: si es obligado que venga (Json del controller))
# 2 - (None, True) (no tiene validaciones, True/False: si es obligado que venga)
# Ejemplo:
# campos = {'id': (__val_id, True), 'titulo': (None, True), 'anio_edicion': (__val_str, False), 'precio': (__val_precio, True), 'autor': (__val_id, False)}

    campos:Dict[str, Tuple[List[LambdaType], bool]] = {'id': (__val_id, True), 'titulo': (__val_str, True), 'anio_edicion': (__val_str, True), 'precio': (__val_precio, True), 'autor': (__val_id, False)}

    @staticmethod
    def json(id, titulo, anio_edicion, precio):
        return {'id': id, 'titulo': titulo, 'anio_edicion': anio_edicion, 'precio': precio}