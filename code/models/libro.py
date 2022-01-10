# from autor import Autor


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

    campos = {'id': __val_id, 'titulo': __val_str, 'anio_edicion': __val_str, 'precio': __val_precio}

    @staticmethod
    def json(id, titulo, anio_edicion, precio):
        return {'id': id, 'titulo': titulo, 'anio_edicion': anio_edicion, 'precio': precio}

    # def __init__(self, id, titulo, anio_edicion, precio) -> None:
    #     self.id = id
    #     self.titulo = titulo
    #     self.anio_edicion = anio_edicion
    #     self.precio = precio

    # @property
    # def id(self):
    #     return self.__id

    # @id.setter
    # def id(self, id):
    #     if id != None and type(id) != int:
    #         raise TypeError("El id esta mal")
    #     self.__id = id

    # @property
    # def titulo(self):
    #     return self.__titulo

    # @titulo.setter
    # def titulo(self, titulo):
    #     if type(titulo) != str:
    #         raise TypeError("El titulo no es un string")
    #     self.__titulo = titulo

    # @property
    # def anio_edicion(self):
    #     return self.__anio_edicion

    # @anio_edicion.setter
    # def anio_edicion(self, anio_edicion):
    #     if type(anio_edicion) != str:
    #         raise TypeError("El anio_edicion no es un string")
    #     self.__anio_edicion = anio_edicion

    # @property
    # def precio(self):
    #     return self.__precio

    # @precio.setter
    # def precio(self, precio):
    #     if type(precio) != float:
    #         raise TypeError("El precio no es un float")
    #     self.__precio = precio

    # @classmethod
    # def constructor(cls, titulo, anio_edicion, precio):
    #     return cls(None, titulo, anio_edicion, precio)
