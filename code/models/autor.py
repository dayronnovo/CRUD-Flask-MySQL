class Autor:

    __val_id = [
        (lambda x : type(x) == int, "No es del tipo correcto")
    ]
    __val_str = [
        (lambda x : type(x) == str, "No es del tipo correcto"),
        (lambda x: len(x.strip()) > 0, "No puede ser vacio")
    ]

    campos = {'id': __val_id, 'nombre': __val_str, 'apellido': __val_str, 'fecha_nacimiento': __val_str}
    

    @staticmethod
    def json(id, nombre, apellido, fecha_nacimiento):
        return {'id': id, 'nombre': nombre, 'apellido': apellido, 'fecha_nacimiento': fecha_nacimiento}

    # =============  Validaciones  =============

    # campos = {'id': val_id, 'nombre': val_str, 'apellido': val_str, 'fecha_nacimiento': val_str}

    # def __init__(self, id, nombre, apellido, fecha_nacimiento) -> None:
    #     self.id = id
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.fecha_nacimiento = fecha_nacimiento

    # def __str__(self):
    #     return f"Autor => [id = {self.id}, nombre = {self.nombre}, apellido = {self.apellido}, fecha_nacimiento = {self.fecha_nacimiento}]"

    # @classmethod
    # def constructor(cls, nombre, apellido, fecha_nacimiento):
    #     return cls(None, nombre, apellido, fecha_nacimiento)




# class Autor:
#     campos = {'id': int, 'nombre': str,
#               'apellido': str, 'fecha_nacimiento': str}

#     def __init__(self, id, nombre, apellido, fecha_nacimiento) -> None:
#         self.id = id
#         self.nombre = nombre
#         self.apellido = apellido
#         self.fecha_nacimiento = fecha_nacimiento

#     def validacion():
#         pass

#     @staticmethod
#     def json(id, nombre, apellido, fecha_nacimiento):
#         return {'id': id, 'nombre': nombre, 'apellido': apellido, 'fecha_nacimiento': fecha_nacimiento}

#     @property
#     def id(self):
#         return self.__id

#     @id.setter
#     def id(self, id):
#         if id != None and type(id) != int:
#             raise TypeError("El id esta mal")
#         self.__id = id

#     @property
#     def nombre(self):
#         return self.__nombre

#     @nombre.setter
#     def nombre(self, nombre):
#         if type(nombre) != str:
#             raise TypeError("El nombre no es un string")
#         self.__nombre = nombre

#     @property
#     def apellido(self):
#         return self.__apellido

#     @apellido.setter
#     def apellido(self, apellido):
#         if type(apellido) != str:
#             raise TypeError("El apellido no es un string")
#         self.__apellido = apellido

#     @property
#     def fecha_nacimiento(self):
#         return self.__fecha_nacimiento

#     @fecha_nacimiento.setter
#     def fecha_nacimiento(self, fecha_nacimiento):
#         if type(fecha_nacimiento) == str:
#             raise TypeError("La fecha_nacimiento no es un string")
#         self.__fecha_nacimiento = fecha_nacimiento

#     def __str__(self):
#         return f"Autor => [id = {self.id}, nombre = {self.nombre}, apellido = {self.apellido}, fecha_nacimiento = {self.fecha_nacimiento}]"

#     @classmethod
#     def constructor(cls, nombre, apellido, fecha_nacimiento):
#         return cls(None, nombre, apellido, fecha_nacimiento)
