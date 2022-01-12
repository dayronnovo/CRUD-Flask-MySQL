class Autor:

    __val_id = [
        (lambda x : type(x) == int, "No es del tipo correcto")
    ]
    __val_str = [
        (lambda x : type(x) == str, "No es del tipo correcto"),
        (lambda x: len(x.strip()) > 0, "No puede ser vacio")
    ]

    campos = {'id': (__val_id, True), 'nombre': (__val_str, True), 'apellido': (__val_str, True), 'fecha_nacimiento': (__val_str, True)}
    

    @staticmethod
    def json(id, nombre, apellido, fecha_nacimiento):
        return {'id': id, 'nombre': nombre, 'apellido': apellido, 'fecha_nacimiento': fecha_nacimiento}