class Autor:
    def __init__(self, _id, nombre, apellido, fecha_nacimiento) -> None:
        self._id = _id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    @staticmethod
    def json(id, nombre, apellido, fecha_nacimiento):
        return {'id': id, 'nombre': nombre, 'apellido': apellido, 'fecha_nacimiento': fecha_nacimiento}

    @classmethod
    def constructor(cls, nombre, apellido, fecha_nacimiento):
        return cls(None, nombre, apellido, fecha_nacimiento)
