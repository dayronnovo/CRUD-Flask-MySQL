class Autor:
    def __init__(self, id, nombre, apellido, fecha_nacimiento) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    @staticmethod
    def json(id, nombre, apellido, fecha_nacimiento):
        return {'id': id, 'nombre': nombre, 'apellido': apellido, 'fecha_nacimiento': fecha_nacimiento}

    # @property
    # def id(self):
    #     return self.__id

    # @id.setter
    # def id(self, id):
    #     if id != None and type(id) != int:
    #         raise TypeError("El id esta mal")
    #     self.__id = id

    # @property
    # def nombre(self):
    #     return self.__nombre

    # @nombre.setter
    # def nombre(self, nombre):
    #     if type(nombre) != str:
    #         raise TypeError("El nombre no es un string")
    #     self.__nombre = nombre

    # @property
    # def apellido(self):
    #     return self.__apellido

    # @apellido.setter
    # def apellido(self, apellido):
    #     if type(apellido) == str:
    #         self.__apellido = apellido

    # @property
    # def fecha_nacimiento(self):
    #     return self.__fecha_nacimiento

    # @fecha_nacimiento.setter
    # def fecha_nacimiento(self, fecha_nacimiento):
    #     if type(fecha_nacimiento) == date:
    #         self.__fecha_nacimiento = fecha_nacimiento

    @classmethod
    def constructor(cls, nombre, apellido, fecha_nacimiento):
        return cls(None, nombre, apellido, fecha_nacimiento)
